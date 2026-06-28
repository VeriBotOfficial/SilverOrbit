# SilverOrbit App Store Repo

This repo is designed to be very easy to update.

## Add a new game
1. Copy the `games/example-game/` folder.
2. Rename it to your new slug, for example `games/my-new-game/`.
3. Replace the icon, banner, screenshots, and APK inside that folder.
4. Edit only `games/<your-game>/game.json`.
5. Run `python tools/build_catalog.py`.
6. Commit and push.

## Files the app reads
- `catalog.json` at the repo root

## Update flow
- `tools/build_catalog.py` scans every `games/*/game.json`
- It generates one easy-to-read `catalog.json`
- The app only needs to fetch `catalog.json`

## Example folder
- `games/example-game/`
