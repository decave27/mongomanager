import pymongo

class Client(pymongo.MongoClient):
    def __init__(self, url: str, *args, **kwargs):
        super().__init__(url, *args, **kwargs)
    
    def db(self):
        def __init__(self, **kwargs):
            self.db = kwargs.get('db')
            self.col = kwargs.get('col')
            mydb = self[self.db]
            mycol = mydb[self.col]
            self.dicter = mycol
            return mycol
        def findjson(self, key : dict) -> None:
            cols = self.dicter.find(key)
            data = dict()
            for i in cols:
                data.append(i)
            return data
        def commit(self, keys=None):
            if str(type(keys)) == "<class 'list'>":
                r = self.dicter.instert_many(keys)
            elif str(type(keys)) == "<class 'dict'>":
                r = self.dicter.insert_one(keys)
            return r
