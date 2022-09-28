import json
from pathlib import Path

file_path = Path("./json/twitter_users.json").resolve()
# searches the file directory from home

file_path.parent.mkdir(parents=True, exist_ok=True)
# creates the file folder and makes it the parent directory and that it exist

file_path.touch()
# creates file inside the current directory

twitter_users = dict(name="Abc", age=23, is_married=True, tweets=["I love my mum", "No be me"])
# dictionary to store the data

with file_path.open(encoding="utf-8", mode="w") as file:
    json.dump(twitter_users, file, indent=2)

# filename .dumps will dump the file to string while filename.dump will only dump the file to a json file
# filename. loads will
# pickle.dumps