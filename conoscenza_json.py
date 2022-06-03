import json


#tentativi di manipolazione di file json

#app = FastAPI()

#fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

data_pioggia='{id1="0","data":"20220603","pm": [30, 15, 60]},{id2="0","data": "20230612","pm": [15, 7.5, 30]}'
person = '{"name": "Bob", "languages": ["English", "French"]}'

data_pioggia_loads=json.loads(data_pioggia)

print(data_pioggia_loads)
#@app.get("/items/{anno}")
#async def read_item(anno):
#    for i in data_pioggia:
#        if 


 #   return fake_items_db[skip : skip + limit]




