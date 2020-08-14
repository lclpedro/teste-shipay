#Dependencies
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from dotenv import load_dotenv

basedir = os.path.abspath(__file__)
load_dotenv(os.path.join(basedir, '.env'))

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f'config.Dev')

    '''Extensions'''
    db.init_app(app)

    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    '''Declared Models'''
    from shipay import models

    '''Declared routes'''
    from shipay.routers import estabelecimento
    estabelecimento.configure(app)

    @app.route('/')
    def hello():
        return jsonify(data='Hello')

    return app
