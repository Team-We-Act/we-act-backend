import os
import config
from flask import Flask, redirect, render_template, json, request, jsonify, url_for, make_response, Response
import pyrebase
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import requests
# from flask_restplus import Api,Resource,fields
db = SQLAlchemy()
base_url = '.'

fb_config = {
  "apiKey": "AIzaSyD_Ysrphhvywk9NQfeVAuQpmZWHoCoCg4M",
  "authDomain": "we-act-hackathon.firebaseapp.com",
  "databaseURL": "https://we-act-hackathon-default-rtdb.firebaseio.com",
  "projectId": "we-act-hackathon",
  "storageBucket": "we-act-hackathon.appspot.com",
  "messagingSenderId": "747322680880",
  "appId": "1:747322680880:web:6d3d2ebd784185d4adaff5",
  "measurementId": "G-X163Z3D0Z8"
}
url = "https://master-question-generation-wook-2.endpoint.ainize.ai/generate"
classesList=[]

def create_app(test_config=None):
  app = Flask(__name__,instance_relative_config=True)
  app.config.from_object(config)
    # ORM
  db.init_app(app)

  with app.app_context():
    db.create_all()

  # firebase = pyrebase.initialize_app(fb_config)
  # firebase_db = firebase.database()

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
    
  @app.route('/register_form_recipient')
  def hello_register_participant():
    return render_template('register_form_recipient.html')
  
  @app.route('/code_success', methods=['POST'])
  def hello_code_creation_success():
    if request.method == 'POST':
      data = request.form.to_dict(flat=True)
      print("crud.py", data)
      code_value=data['type']
    return render_template('code_success.html', code_value=code_value)

  from . import views
  app.register_blueprint(views.bp)

  return app