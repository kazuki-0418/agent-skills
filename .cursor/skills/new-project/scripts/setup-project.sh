#!/usr/bin/env bash
# Deterministic project scaffold: copy templates, git init, gh repo create.
# Usage: setup-project.sh [--root <projects-dir>] <project-name> <web-next|mobile-flutter> [private|public]
set -euo pipefail

usage() {
  echo "Usage: $0 [--root <projects-dir>] <project-name> <web-next|mobile-flutter> [private|public]" >&2
  exit 2
}

die() {
  echo "error: $*" >&2
  exit 1
}

ROOT=""
while [[ $# -gt 0 ]]; do
  case "${1}" in
    -h|--help)
      usage
      ;;
    --root)
      [[ $# -ge 2 ]] || die "--root requires a directory"
      ROOT="${2}"
      shift 2
      ;;
    --)
      shift
      break
      ;;
    -*)
      die "unknown option: ${1}"
      ;;
    *)
      break
      ;;
  esac
done

if [[ $# -lt 2 || $# -gt 3 ]]; then
  usage
fi

PROJECT_NAME="${1}"
TYPE="${2}"
VISIBILITY="${3:-private}"

if [[ -z "${PROJECT_NAME}" ]]; then
  die "project-name must be non-empty"
fi
if [[ "${PROJECT_NAME}" == *"/"* || "${PROJECT_NAME}" == *"\\"* ]]; then
  die "project-name must not contain path separators"
fi
if [[ "${PROJECT_NAME}" == *".."* ]]; then
  die "project-name must not contain '..'"
fi

if [[ "${TYPE}" != "web-next" && "${TYPE}" != "mobile-flutter" ]]; then
  die "type must be exactly 'web-next' or 'mobile-flutter'"
fi

if [[ "${VISIBILITY}" != "private" && "${VISIBILITY}" != "public" ]]; then
  die "visibility must be 'private' or 'public'"
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_ROOT="$(cd "${SCRIPT_DIR}/../templates" && pwd)"
COMMON_DIR="${TEMPLATE_ROOT}/common"
TYPE_DIR="${TEMPLATE_ROOT}/${TYPE}"

if [[ -z "${ROOT}" ]]; then
  ROOT="${NEW_PROJECT_ROOT:-$(pwd)}"
fi
if [[ ! -d "${ROOT}" ]]; then
  die "projects root does not exist: ${ROOT}"
fi
ROOT="$(cd "${ROOT}" && pwd)"
PROJECT_DIR="${ROOT}/${PROJECT_NAME}"

if [[ ! -d "${COMMON_DIR}" ]]; then
  die "missing template directory: ${COMMON_DIR}"
fi
if [[ ! -d "${TYPE_DIR}" ]]; then
  die "missing template directory: ${TYPE_DIR}"
fi
if [[ -e "${PROJECT_DIR}" ]]; then
  die "directory already exists: ${PROJECT_DIR}"
fi

mkdir -p "${PROJECT_DIR}"
cp -r "${COMMON_DIR}/." "${PROJECT_DIR}/"
cp -r "${TYPE_DIR}/." "${PROJECT_DIR}/"

while IFS= read -r src; do
  [[ -n "${src}" ]] || continue
  mv "${src}" "${src%.template}"
done < <(find "${PROJECT_DIR}" -type f -name '*.template' | LC_ALL=C sort)

PROJECT_NAME_ESCAPED="$(printf '%s' "${PROJECT_NAME}" | sed 's/[&\\/]/\\&/g')"
# Dart package `name` must be lowercase_snake (hyphens are invalid).
# npm `name` keeps the original (hyphens allowed).
DART_PACKAGE_NAME="$(printf '%s' "${PROJECT_NAME}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/_/g')"

replace_placeholder() {
  local file="$1"
  if sed --version >/dev/null 2>&1; then
    sed -i "s/{{PROJECT_NAME}}/${PROJECT_NAME_ESCAPED}/g" "${file}"
  else
    sed -i '' "s/{{PROJECT_NAME}}/${PROJECT_NAME_ESCAPED}/g" "${file}"
  fi
}

while IFS= read -r file; do
  [[ -n "${file}" ]] || continue
  replace_placeholder "${file}"
done < <(grep -rIl '{{PROJECT_NAME}}' "${PROJECT_DIR}" --exclude-dir=.git || true)

if [[ -f "${PROJECT_DIR}/pubspec.yaml" ]]; then
  awk -v dart="${DART_PACKAGE_NAME}" '
    BEGIN { done = 0 }
    /^name:/ && !done { print "name: " dart; done = 1; next }
    { print }
  ' "${PROJECT_DIR}/pubspec.yaml" > "${PROJECT_DIR}/pubspec.yaml.tmp" \
    && mv "${PROJECT_DIR}/pubspec.yaml.tmp" "${PROJECT_DIR}/pubspec.yaml"
fi

cd "${PROJECT_DIR}"

if git init -b main; then
  :
else
  git init
  git checkout -b main
fi

git add -A

if [[ -z "$(git config user.name || true)" || -z "$(git config user.email || true)" ]]; then
  echo "warning: git identity missing; setting local user.name/user.email for this repo only" >&2
  if [[ -z "$(git config user.name || true)" ]]; then
    git config --local user.name "${GIT_AUTHOR_NAME:-$(id -un)}"
  fi
  if [[ -z "$(git config user.email || true)" ]]; then
    git config --local user.email "${GIT_AUTHOR_EMAIL:-$(id -un)@users.noreply.localhost}"
  fi
fi

git commit -m "chore: initial scaffold from _template"

if ! command -v gh >/dev/null 2>&1; then
  die "gh CLI is required to create the GitHub repository"
fi
if ! gh auth status >/dev/null 2>&1; then
  die "gh is not authenticated. Run: gh auth login"
fi

export GH_PROMPT_DISABLED=1
export GIT_TERMINAL_PROMPT=0

gh repo create "${PROJECT_NAME}" \
  --source=. \
  --remote=origin \
  --push \
  "--${VISIBILITY}"

GITHUB_URL="$(gh repo view --json url -q .url)"

echo "PROJECT_PATH=${PROJECT_DIR}"
echo "GITHUB_URL=${GITHUB_URL}"
