from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
from crear_base import Pais

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all()

paisesAmericanos = session.query(Pais).filter(or_(Pais.continente=="NA", Pais.continente=="SA")).all()
print(paisesAmericanos)
