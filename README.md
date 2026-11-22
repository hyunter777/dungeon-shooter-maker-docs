# Dungeon Shooter Maker

English manual, quick start and public support resources for **Dungeon Shooter Maker**, a Unity toolkit for making
top-down, room-by-room dungeon shooters from data.

- Documentation: https://hyunter777.github.io/dungeon-shooter-maker-docs/
- Quick start: https://hyunter777.github.io/dungeon-shooter-maker-docs/quick-start/
- Editors: https://hyunter777.github.io/dungeon-shooter-maker-docs/editors/
- Q&A: https://github.com/hyunter777/dungeon-shooter-maker-docs/discussions/categories/q-a
- Bug reports: https://github.com/hyunter777/dungeon-shooter-maker-docs/issues
- Publisher website: https://www.flycat.co.kr

This repository contains documentation and support templates. The Unity project, the sample game's content, the
product implementation, packages, paid assets and font files are excluded. The manual is maintained prose taken from
the package's `Documentation/UserGuide.md`; building it does not require Unity or product source.

## Build and preview

Use Python 3.12 and a local virtual environment. Run from the directory containing this README and `mkdocs.yml`:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe scripts/build.py
.venv/Scripts/python.exe -m mkdocs serve
```

On Linux/macOS use `.venv/bin/python`. The build runs `mkdocs build --strict` and checks the public file allowlist,
local links and anchors. Output `site/`, `.venv/`, `.build/` and Python caches are ignored. No global packages are
changed. `--output` selects a directory outside the documentation source.

## Support

See [SUPPORT.md](SUPPORT.md). Use Q&A for usage questions and Issues for reproducible bugs. Do not post the purchased
package or private information.

## Publication

**Prepared locally; publication awaits publisher approval.** The links above are intended destinations; a local build
does not prove that they are online. Creating `hyunter777/dungeon-shooter-maker-docs`, enabling Pages, setting the
Homepage and turning on Discussions require that approval.

The intended Pages source is **`gh-pages` at `/`**, with Homepage set to the documentation URL.
`deployment/pages-workflow.yml` is a dormant manual workflow template kept outside `.github/workflows`. Do not
activate it before approval. `deployment/welcome.md` is the prepared Discussions announcement.

Copyright (c) 2026 FlyCat. See [LICENSE](LICENSE) and the manual's [support and licenses](docs/en/support.md). The
site uses system fonts with `font: false` and ships no font files.

## Screenshots

The pages carry `TODO(screenshot)` comments naming where a capture belongs. Add the PNG under
`docs/en/assets/images/` and replace the comment with an image reference when the screenshots are ready.
