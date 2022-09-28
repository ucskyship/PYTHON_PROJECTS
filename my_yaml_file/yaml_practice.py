import pathlib
import yaml

# you aren't markUpLanguage

# this is to write to yaml file
file_path = pathlib.Path("./config.yaml").resolve()
# text = {'name': 'Boyo', 'age': 18, 'children': ["Odogwu", "Dorcas"]}
# with file_path.open(mode="w") as f:
#     yaml.dump(text, f, sort_keys=False)
# #   yaml.dump(text, f, default_flow_style=False)

# file takes in what you want to dump and where you are dumping it in
# load takes in the file and Loader=yaml.Loader

# this is to read from yaml file
with file_path.open(mode="r") as f:
    # text = {'name': 'Boyo', 'age': 18, 'children': ["Odogwu", "Dorcas"]}
    text = yaml.load(f, yaml.Loader)

print(text)
