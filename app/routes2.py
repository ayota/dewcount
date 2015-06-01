import csv
import psycopg2
from sql_declarative import QCEW, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import Flask, request, g

app = Flask(__name__)

DATABASE = 'postgresql+psycopg2://ayo@localhost/mvp040115'

app.config.from_object(__name__)
if __name__ == '__main__':
  app.run()

def connect_to_database():
    engine = create_engine(DATABASE)
    c = engine.connect()
    return engine, c

def get_db():
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    return session

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()

def execute_query(query, args=()):
    cur = session.query(QCEW).filter(QCEW.area_fips == '01000' and QCEW.year == '2013')
    rows = cur.all()
    return rows

@app.route("/viewdb")
def viewdb():
    cur = session.query(QCEW).filter(QCEW.area_fips == '01000' and QCEW.year == '2013')
    rows = cur.all()
    return rows[0].annual_avg_emplvl

@app.route('/')
def viewdb():
    cur = session.query(QCEW).filter(QCEW.area_fips == '01000' and QCEW.year == '2013')
    rows = cur.all()
    return rows[0].annual_avg_emplvl