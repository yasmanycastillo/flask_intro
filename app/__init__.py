#  -*- encoding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .assets import assets
from .config import Config

# Creating the app entry point
app = Flask(__name__, static_folder='static')
app.config.from_object(Config)

# Initializing other functions
assets.init_app(app)
db = SQLAlchemy(app)

# import our blueprints and register them
from .site.routes import site
from .admin.routes import mod

app.register_blueprint(site)
app.register_blueprint(mod, url_prefix='/admin')
