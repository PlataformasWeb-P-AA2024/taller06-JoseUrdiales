from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
from crear_base import Pais

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all()

paisesAsia = session.query(Pais).filter(Pais.continente=="AS").order_by(Pais.dial).all()
print(paisesAsia)
print("--------------------------------")