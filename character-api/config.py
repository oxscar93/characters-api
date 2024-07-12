"""[General Configuration Params]
"""
from os import path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'characters.db')

load_dotenv(path.join(basedir, '.env'))
