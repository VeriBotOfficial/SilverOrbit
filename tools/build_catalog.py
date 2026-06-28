#!/usr/bin/env python3
from pathlib import Path
import json

BASE_URL = "https://raw.githubusercontent.com/VeriBotOfficial/SilverOrbit/main/"
ROOT = Path(__file__).resolve().parents[1]
GAMES_DIR = ROOT / "games"
OUT_FILE = ROOT / "catalog.json"

apps = []
for game_json in sorted(GAMES_DIR.glob("*/game.json")):
    data = json.loads(game_json.read_text(encoding="utf-8"))
    game_dir = game_json.parent.as_posix().replace(str(ROOT.as_posix()) + "/", "")
    entry = {
        "id": data["id"],
        "name": data["name"],
        "shortDescription": data.get("shortDescription", ""),
        "description": data.get("description", ""),
        "version": data.get("version", ""),
        "author": data.get("author", "VeriBot"),
        "category": data.get("category", ""),
        "featured": bool(data.get("featured", False)),
        "icon": f"{BASE_URL}{data['icon'] if data['icon'].startswith('games/') else game_dir + '/' + data['icon']}",
        "banner": f"{BASE_URL}{data['banner'] if data['banner'].startswith('games/') else game_dir + '/' + data['banner']}",
        "screenshots": [
            f"{BASE_URL}{shot if shot.startswith('games/') else game_dir + '/' + shot}"
            for shot in data.get("screenshots", [])
        ],
        "apk": f"{BASE_URL}{data['apk'] if data['apk'].startswith('games/') else game_dir + '/' + data['apk']}",
    }
    apps.append(entry)

catalog = {
    "storeName": "SilverOrbit App Store",
    "creator": "VeriBot",
    "apps": apps
}

OUT_FILE.write_text(json.dumps(catalog, indent=2), encoding="utf-8")
print(f"Wrote {OUT_FILE} with {len(apps)} app(s).")
