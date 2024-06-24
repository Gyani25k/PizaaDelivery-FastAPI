from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine = create_engine('postgresql://postgres:root@localhost/pizza_database',
                       echo=True)

Base=declarative_base()
Session = sessionmaker()

