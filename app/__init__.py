#  -*- encoding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .assets import assets
from .config import Config

# Defino el nombre de mi app principal
app = Flask(__name__, static_folder='static')
app.config.from_object(Config)
assets.init_app(app)
# Defino mi cursor de la base de datos
db = SQLAlchemy(app)

from .site.routes import site
from .admin.routes import mod

app.register_blueprint(site)
app.register_blueprint(mod, url_prefix='/admin')
