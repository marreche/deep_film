import json
from bson.json_util import loads
from bson import json_util

def serialize(fn):
    def wrapper(*args,**kwargs):
        res = fn(*args,**kwargs)
        return (json.loads(json_util.dumps(res)))
    wrapper.__name__=fn.__name__
    return wrapper