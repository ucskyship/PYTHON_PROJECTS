import json
from pathlib import Path

# db = Path(__file__)
db = Path.cwd() / "db.json"

db.touch()


def read_db() -> list:
    with db.open(mode="r", encoding="utf-8") as file:
        return json.load(file)


def write_to_db(user_data: list) -> None:
    with db.open(mode="w", encoding="utf-8") as file:
        return json.dump(user_data, file, indent=2)
