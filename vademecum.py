# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pandas as pd
import json

client = MongoClient('localhost', 27017)
# Se crea la base de datos
db = client.vademecum
db = client['vademecum']

# Lee el excel
analgesicos = pd.read_excel('analgesicos.xls').to_json(orient='records')

# Se pasa a json y luego se inserta
data = json.loads(analgesicos)
vademecum = db.vademecum
result = vademecum.insert(data)
