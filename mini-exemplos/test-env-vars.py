
import json
import os

dd = dict(os.environ)
msg = json.dumps(dd, indent=4)
print(msg)
