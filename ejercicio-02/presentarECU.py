from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
from crear_base import Pais

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all()

paisEc = session.query(Pais).filter(or_(Pais.nombre.like("%uador%"), Pais.capital.like("%ito%"))).all()
print(paisEc)