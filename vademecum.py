# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pandas as pd
import json


class ExcelMongo:
    def __init__(self, excel):
        self.excel = excel

    # Lee el excel
    @staticmethod
    def excel_to_mongo(excel):
        analgesicos = pd.read_excel(excel).to_json(orient='records')
        # Se pasa a json y luego se inserta
        data = json.loads(analgesicos)
        vademecum = db.vademecum
        result = vademecum.insert(data)
        return result

if __name__ == '__main__':
    # Conexion con la base de datos
    client = MongoClient('localhost', 27017)
    # Se crea la base de datos
    db = client.vademecum
    db = client['vademecum']
    analgesico = ExcelMongo('analgesicos.xls')
    analgesico.excel_to_mongo(analgesico.excel)

