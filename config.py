import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Database connection string
SQLALCHEMY_DATABASE_URI = 'postgres://dnfqslluqepqxp:553bd7a9ff3b8ce448cba49b96bd0aac83441d97508e3a6807e9204a66e26787@ec2-54-157-234-29.compute-1.amazonaws.com:5432/da939c850dc00q'
# Supress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False