from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_base import Pais
import requests
import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')
Session = sessionmaker(bind=engine)
session = Session()


datos = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')
datos_json = datos.json()

for d in datos_json:
    print(d)
    print(len(d.keys()))
    p = Pais(nombre=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], \
            dial=d['Dial'], geoNameID=d['Geoname ID'], itu=d['ITU'], lenguaje=d['Languages'], independiente=d['is_independent'])
    session.add(p)

# confirmar transacciones

session.commit()
