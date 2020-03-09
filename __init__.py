from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from elasticsearch import Elasticsearch


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
es_client = Elasticsearch()
