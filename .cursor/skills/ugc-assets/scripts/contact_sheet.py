#!/usr/bin/env python3
"""動画からフレームを抜いて横一列に並べた1枚を作る。

動画の中身を確認するのに1フレームずつ Read すると、往復が増えるうえに
時系列の変化（人物が入れ替わる、言語チップが違う、途中で画角が変わる）を
見落とす。並べて1枚にすると一度で分かる。

使い方:
    python3 contact_sheet.py <video> -o out.png [--times 0.5,2,4,6]
    python3 contact_sheet.py <video> -o out.png --count 6   # 等間隔で6枚

PIL (Pillow) と ffmpeg が要る。
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow が要る: pip install Pillow")

# 既定フォントは固定サイズで、縮小後に潰れて読めなくなる。
# フレーム幅に比例したサイズで system font を読む。
FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def load_font(size):
    for path in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def duration_of(video):
    out = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(video)],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        sys.exit(f"ffprobe が失敗した: {video}")
    return float(json.loads(out.stdout)["format"]["duration"])


def grab(video, t, dest):
    r = subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-ss", str(t), "-i", str(video),
         "-frames:v", "1", str(dest)],
        capture_output=True, text=True,
    )
    return dest.exists() and r.returncode == 0


def main():
    ap = argparse.ArgumentParser(description="動画のコンタクトシートを作る")
    ap.add_argument("video")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--times", help="秒をカンマ区切りで（例 0.5,2,4）")
    ap.add_argument("--count", type=int, default=5, help="等間隔で抜く枚数（既定 5）")
    ap.add_argument("--width", type=int, default=1800, help="出力の最大幅（既定 1800）")
    ap.add_argument("--no-label", action="store_true", help="秒数の焼き込みを省く")
    args = ap.parse_args()

    video = Path(args.video).expanduser()
    if not video.is_file():
        sys.exit(f"ファイルが無い: {video}")

    if args.times:
        times = [float(t) for t in args.times.split(",")]
    else:
        dur = duration_of(video)
        # 端は絵が決まっていないことが多いので、前後 4% を避けて等間隔に取る
        lo, hi = dur * 0.04, dur * 0.96
        n = max(args.count, 1)
        times = [lo] if n == 1 else [lo + (hi - lo) * i / (n - 1) for i in range(n)]

    frames = []
    with tempfile.TemporaryDirectory() as tmp:
        for i, t in enumerate(times):
            dest = Path(tmp) / f"f{i}.png"
            if grab(video, t, dest):
                frames.append((t, Image.open(dest).convert("RGB")))
            else:
                print(f"警告: {t:.2f}s のフレームが取れなかった", file=sys.stderr)
        if not frames:
            sys.exit("フレームを1枚も取れなかった")

        w, h = frames[0][1].size
        sheet = Image.new("RGB", (w * len(frames), h), "white")
        for i, (t, im) in enumerate(frames):
            if im.size != (w, h):
                im = im.resize((w, h))
            sheet.paste(im, (i * w, 0))
        # 先に縮小してからラベルを描く。逆順だと縮小で文字が潰れて読めない
        if sheet.width > args.width:
            sheet.thumbnail((args.width, args.width))
        if not args.no_label:
            cell = sheet.width / len(frames)
            font = load_font(max(14, int(cell * 0.11)))
            pad = max(6, int(cell * 0.03))
            d = ImageDraw.Draw(sheet)
            for i, (t, _) in enumerate(frames):
                label = f"{t:.1f}s"
                x, y = i * cell + pad, pad
                # 明暗どちらの画でも読めるよう、黒フチを回してから白で描く
                off = max(2, int(font.size * 0.12))
                for dx in (-off, 0, off):
                    for dy in (-off, 0, off):
                        d.text((x + dx, y + dy), label, fill="black", font=font)
                d.text((x, y), label, fill="white", font=font)
        out = Path(args.out).expanduser()
        out.parent.mkdir(parents=True, exist_ok=True)
        sheet.save(out)
        print(f"{out}  ({sheet.width}×{sheet.height}, {len(frames)}枚: "
              f"{', '.join(f'{t:.1f}s' for t, _ in frames)})")


if __name__ == "__main__":
    main()
