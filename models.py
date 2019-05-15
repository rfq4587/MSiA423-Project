import os
import sys
import logging

from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import sqlalchemy
import config
import argparse

import pandas as pd

logging.basicConfig(level=logging.DEBUG, filename="logs.txt", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger('petition-models')

Base = declarative_base()

class Petition(Base):
    """Initialize the petition table that will contain data for modified KNN algorithm"""
    __tablename__ = 'petition'

    id = Column(String(25), primary_key=True, unique=True, nullable=False)
    status= Column(Integer, unique=False, nullable=False)
    industry = Column(String(25), unique=False, nullable=False)
    jobtitle = Column(String(25), unique=False, nullable=False)
    fulltime = Column(Integer, unique=False, nullable=False)
    pay = Column(Integer, unique=False, nullable=False)

    def __repr__(self):
        petition = "<Petition(id='%s', status='%d', industry='%s', jobtitle='%s', fulltime='%d', pay='%d', fulltime='%d')>"
        return petition % (self.id, self.status, self.industry, self.jobtitle, self.fulltime, self.pay)

# def _truncate_petition(session):
#     """Deletes tweet scores table if rerunning and run into unique key error."""
#
#     session.execute('''DELETE FROM tweet_score''')


def get_engine_string():
    """Get database engine path."""

    conn_type = "mysql+pymysql"
    user = config.MYSQL_USER
    password = config.MYSQL_PASSWORD
    host = config.MYSQL_HOST
    port = config.MYSQL_PORT
    DATABASE_NAME = 'msia423'

    engine_string = "{}://{}:{}@{}:{}/{}". \
        format(conn_type, user, password, host, port, DATABASE_NAME)
    logging.debug("engine string: %s"%engine_string)
    return  engine_string


def create_db(engine=None, engine_string=None):
    """Creates a database with the data models inherited from `Base` (Tweet and TweetScore).

    Args:
        engine (:py:class:`sqlalchemy.engine.Engine`, default None): SQLAlchemy connection engine.
            If None, `engine_string` must be provided.
        engine_string (`str`, default None): String defining SQLAlchemy connection URI in the form of
            `dialect+driver://username:password@host:port/database`. If None, `engine` must be provided.

    Returns:
        None
    """
    if engine is None:
    #    RDS = eval(args.RDS) # evaluate string to bool
    #    logger.info("RDS:%s"%RDS)
        engine = sqlalchemy.create_engine(get_engine_string())

    Base.metadata.create_all(engine)
    logging.info("database created")

    return engine


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create defined tables in database")

    engine = create_db()
    #
    #
    Session = sessionmaker(bind=engine)
    session = Session()
    #
    # test_row = Petition(id="0", status=0, industry="Computer",
    # jobtitle="Software Engineer", fulltime=1, pay=4)
    #
    # # use1 = Churn_Prediction(age="27",activeMember="1",numProducts="2",fromGermany="0",
    # #     gender="1",balance="500.89",hasCrCard="1",tenure="2",predicted_score="1")
    # session.add(test_row)
    # session.commit()
    #
    # logger.info("Data added")
    #
    query = "SELECT * FROM petition"
    df = pd.read_sql(query, con=engine)
    logger.info(df)
