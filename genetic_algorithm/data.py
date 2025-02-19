# genetic_algorithm/data.py
import json


#Funcion para carga de datos los cuales podemos pasar en la funcion principal main.py
def load_data(json_path: str):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data
