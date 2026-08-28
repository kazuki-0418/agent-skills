#!/usr/bin/env python3
"""素材ディレクトリの棚卸し。

新しく素材を作る前に、いま何があるかを機械的に出す。目視だと
「似た名前の別テイク」「9:16 でない過去の失敗作」「音声の有無」を見落とす。

使い方:
    python3 probe_assets.py <dir> [--target 9:16] [--recursive] [--json]

出力: Markdown テーブル + 目標比率から外れているものの警告。
ffprobe (ffmpeg) が要る。画像は ffprobe があればそれで、無ければ sips で読む。
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

VIDEO_EXT = {".mp4", ".mov", ".m4v", ".webm", ".avi", ".mkv"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".heic", ".gif"}
AUDIO_EXT = {".mp3", ".wav", ".m4a", ".aac", ".flac"}


def run(cmd):
    """コマンドを実行して stdout を返す。失敗時は None（呼び出し側で分岐する）。"""
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def probe(path):
    """1ファイルの情報を dict で返す。読めなければ error を入れて返す。"""
    info = {
        "name": path.name,
        "kind": None,
        "w": None,
        "h": None,
        "aspect": None,
        "duration": None,
        "audio": None,
        "mb": round(path.stat().st_size / 1_048_576, 2),
        "error": None,
    }
    ext = path.suffix.lower()
    info["kind"] = (
        "video" if ext in VIDEO_EXT
        else "image" if ext in IMAGE_EXT
        else "audio" if ext in AUDIO_EXT
        else "other"
    )
    if info["kind"] == "other":
        return info

    raw = run([
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_format", "-show_streams", str(path),
    ])
    if raw:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            data = None
        if data:
            streams = data.get("streams", [])
            vs = next((s for s in streams if s.get("codec_type") == "video"), None)
            has_audio = any(s.get("codec_type") == "audio" for s in streams)
            if vs:
                info["w"] = vs.get("width")
                info["h"] = vs.get("height")
            dur = data.get("format", {}).get("duration")
            if dur:
                info["duration"] = round(float(dur), 2)
            # 静止画にも video ストリームが立つので、種別で音声欄を出し分ける
            info["audio"] = has_audio if info["kind"] != "image" else None
    elif info["kind"] == "image":
        # ffprobe が無い / 読めない画像は sips（macOS）で寸法だけ取る
        out = run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)])
        if out:
            for line in out.splitlines():
                if "pixelWidth:" in line:
                    info["w"] = int(line.split(":")[1])
                elif "pixelHeight:" in line:
                    info["h"] = int(line.split(":")[1])

    if info["w"] and info["h"]:
        info["aspect"] = round(info["w"] / info["h"], 4)
    elif info["kind"] != "audio":
        info["error"] = "寸法が読めない"
    return info


def parse_target(s):
    if ":" not in s:
        raise argparse.ArgumentTypeError("--target は 9:16 の形式で指定する")
    w, h = s.split(":", 1)
    return float(w) / float(h)


def main():
    ap = argparse.ArgumentParser(description="素材ディレクトリの棚卸し")
    ap.add_argument("directory")
    ap.add_argument("--target", default="9:16", help="目標アスペクト比 (既定 9:16)")
    ap.add_argument("--tolerance", type=float, default=0.02,
                    help="目標比率からの許容ずれ (既定 0.02)")
    ap.add_argument("--recursive", action="store_true")
    ap.add_argument("--json", action="store_true", help="Markdown ではなく JSON で出す")
    args = ap.parse_args()

    root = Path(args.directory).expanduser()
    if not root.is_dir():
        sys.exit(f"ディレクトリが無い: {root}")

    target = parse_target(args.target)
    paths = sorted(root.rglob("*") if args.recursive else root.glob("*"))
    files = [p for p in paths if p.is_file() and not p.name.startswith(".")]
    if not files:
        sys.exit(f"ファイルが無い: {root}")

    rows = [probe(p) for p in files]
    media = [r for r in rows if r["kind"] != "other"]

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return

    print(f"# 棚卸し: {root}")
    print(f"\n{len(files)} ファイル（メディア {len(media)}）／目標比率 {args.target}\n")
    print("| ファイル | 種別 | 解像度 | 比率 | 尺(s) | 音声 | MB |")
    print("|---|---|---|---|---|---|---|")
    for r in rows:
        dims = f"{r['w']}×{r['h']}" if r["w"] else "—"
        asp = f"{r['aspect']:.3f}" if r["aspect"] else "—"
        dur = f"{r['duration']:.2f}" if r["duration"] else "—"
        aud = "—" if r["audio"] is None else ("あり" if r["audio"] else "なし")
        print(f"| `{r['name']}` | {r['kind']} | {dims} | {asp} | {dur} | {aud} | {r['mb']} |")

    off = [r for r in media if r["aspect"] and abs(r["aspect"] - target) > args.tolerance]
    bad = [r for r in media if r["error"]]
    silent = [r for r in media if r["kind"] == "video" and r["audio"] is False]

    print()
    if off:
        print(f"## ⚠️ 目標比率 {args.target} から外れている（{len(off)}件）\n")
        for r in off:
            print(f"- `{r['name']}` — {r['w']}×{r['h']}（比率 {r['aspect']:.3f}）")
        print("\n合成で引き伸ばすか切るかの判断が要る。過去の失敗テイクが混ざっていないかも確認する。\n")
    if silent:
        print(f"## 音声トラックが無い動画（{len(silent)}件）\n")
        for r in silent:
            print(f"- `{r['name']}`")
        print("\n素材クリップとしては正常。完成版のつもりなら音が抜けている。\n")
    if bad:
        print(f"## 読めなかった（{len(bad)}件）\n")
        for r in bad:
            print(f"- `{r['name']}` — {r['error']}")
        print()
    if not (off or silent or bad):
        print("目立つ問題は無し。")


if __name__ == "__main__":
    main()
