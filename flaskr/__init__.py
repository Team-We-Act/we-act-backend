import os
import config

from flask import Flask, render_template, json, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_restplus import Api,Resource,fields
db = SQLAlchemy()
migrate = Migrate()
base_url = '/'
#flask_restx와 SWagger
# @app.route()

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(config)
    # ORM
  db.init_app(app)
  migrate.init_app(app, db)
  from . import models
  from . import views
  app.register_blueprint(views.bp)

  # a simple page that says hello
  @app.route('/')
  def hello():
      return render_template('index.html')

  @app.route('/register')
  def hello_register():
    return render_template('register.html')

  @app.route('/register_form_volunteer')
  def hello_register_volunteer():
    return render_template('register_form_volunteer.html')

  return app
