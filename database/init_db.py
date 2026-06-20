from database.base import Base, engine

import database.models


def init_db():
    Base.metadata.create_all(bind=engine)