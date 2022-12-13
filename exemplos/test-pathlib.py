
import json
import pathlib

with open('myconfig.json') as file:
    myconfig = json.load(file)

msg = json.dumps(myconfig, indent=4)
print(msg)

imgcfg = myconfig['image-config']
path = pathlib.Path(imgcfg['img-path'])

if not path.exists():
    path.mkdir()

msg = str(path.resolve())
print(msg)
