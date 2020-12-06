# mongodb extension module


## Installation

pip install mongomanager 

## Load data value
```py
import mongomanager
client = mongomanager.Client("mongodb://localhost:27017/")
db = client.db("test", "test").findjson({"name" : "decave"})
print(db)
```
Return in list or dict format

## Adding data
```py
import mongomanager
client = mongomanager.Client("mongodb://localhost:27017/")
db = client.db("test", "test")
db.commit({"test" : "sans", "name" : "decave"})
```
Can be added in dict or list format

