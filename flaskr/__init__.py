import os
import config
from flask import Flask, redirect, render_template, json, request, jsonify, url_for, make_response, Response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import requests
# from flask_restplus import Api,Resource,fields
db = SQLAlchemy()
base_url = '.'


def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

  
## register_form_volunteer 등 라우팅 user.py로 옮김
  

    from . import views
    from . import user
    app.register_blueprint(views.bp)
    app.register_blueprint(user.bp)
    return app
