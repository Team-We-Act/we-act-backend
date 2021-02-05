import os
import config
from flask import Flask, render_template, json, request,jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import requests
# from flask_restplus import Api,Resource,fields
db = SQLAlchemy()
migrate = Migrate()
base_url = '.'

url = "https://master-question-generation-wook-2.endpoint.ainize.ai/generate"
classesList=[]

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(config)
    # ORM
  db.init_app(app)
  migrate.init_app(app, db)
  from .models import Classes
  from . import views
  app.register_blueprint(views.bp)



  @app.route('/test')
  def testQuiz():
    payload = {
      'input': 'Python is an interpreted, high-level and general-purpose programming language. Python\'s design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]  Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[31] '}
    response = requests.request("POST", url, data=payload)
    firstQA=""
    if not response.ok==False:
      obj=response.json()
      firstQA={'question':obj['question']['0'] ,
              'answer': obj['answer']['0']
            }


    return jsonify(firstQA)
  
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

  @app.route('/classes', methods=['POST'])
  def postClasses():

    # className=request.form.to_dict('className')
    className=request.json.get('className')
    subject=request.json.get('subject')
    tutorId=request.json.get('tutorId')
    if not (className and subject and tutorId):
      return jsonify({'error':'No arguments'}), 400

    classObj=Classes()
    classObj.className=className
    classObj.subject=subject
    classObj.tutorId=tutorId
    classesList.append(classObj)
    return jsonify(classObj),201

  # @app.route(base_url+'classes')
  # quiz는 get 

  return app
