import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Database connection string
SQLALCHEMY_DATABASE_URI = 'postgres://sskpjelmbyfoez:97ec88947080115361d69e93495c96ff3dd4499babf98dedf31fc044a1c1099f@ec2-52-87-22-151.compute-1.amazonaws.com:5432/d284mn0tbnns06'
# Supress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False