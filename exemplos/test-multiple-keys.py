
import json
__cfg = {
    "aa": {
        "a": "test",
        "b": "--",
        "c": "tset"
    },
    "bb": [1, 2, 3],
    "cc": 33,
    "dd": "my--str",
    "ee": {
        "ff": {
            "d": True,
            "e": 4,
            "f": "5"
        },
        "gg": False,
        "hh": 99
    },
    "oi": "ultimo"
}

def log(dd):
    print('#'*20)
    msg = json.dumps(dd, indent=4)
    print(msg)


_mychange = {
    "aa:b": 22,
    "dd": "outra--str",
    "ee:ff:e": 777
}

def update_items(orig, changelist):
    for key, value in changelist.items():
        print(f'mychange: {key} , {value}')
        klist = key.split(':')
        ultimo = klist.pop()
        ddtmp = orig

        while len(klist):
            subkey = klist.pop(0)
            ddtmp = ddtmp[subkey]

        ddtmp[ultimo] = value



log(__cfg)
update_items(__cfg, _mychange)
log(__cfg)
