from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
from crear_base import Pais

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all()

for s in paises:
    print("PAIS: %s\nLENGUAJES: %s" % (s.nombre, s.lenguaje))
    print("---------")