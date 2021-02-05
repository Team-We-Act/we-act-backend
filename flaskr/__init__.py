import os

from sqlalchemy import JSON

import config
from flask import Flask, render_template,json, request, jsonify, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import requests


db=SQLAlchemy()
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
  from .models import Lecture
  
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

  @app.route('/volunteer_classes')
  def hello_volunteer_classes():
    return render_template('volunteer_classes.html')

  @app.route('/recipient_classes')
  def hello_recipient_classes():
    return render_template('recipient_classes.html')







  ##post

  @app.route('/classes', methods=['POST'])
  def postClasses():

    # className=request.form.to_dict('className')
    className=request.json.get('className')
    subject=request.json.get('subject')
    country=request.json.get('country')
    language=request.json.get('language')
    # tutorId=request.json.get('tutorId')
    if not (className and subject ):
      return jsonify({'error':'No arguments'}), 400

    classObj=Classes(className,subject,country,language)
    # classObj.tutorId=tutorId

    classesList.append(classObj)
    return (classObj.toJSONString()), 201
    #todo: classesList를 db에 sync하는

  # @app.route(base_url+'classes')
  # quiz는 get
  @app.route('/lectures',methods=['POST'])
  def postLectureQuiz():
    title=request.json.get('title')
    content=request.json.get('content')
    className=request.json.get('className')
    lecturer=request.json.get('lecturer')
    if content:
      payload={'input':content}
      print(payload)
      response=requests.request("POST",url,data=payload)
      firstQA=""
      print(response)
      if not response.ok==False:
        obj=response.json()
        firstQA={'question':obj['question']['0'],
                 'answer':obj['answer']['0']
                 }
        print('여기까진 오니')

      if title :
        print('여기 오도니')
        new_lecture=Lecture(title,content,className,lecturer)
        db.session.add(new_lecture)
        db.session.commit()
        print('debug')
        # finalData = str.replace( "//""")
        return make_response(json.dumps({'lecture':new_lecture.toJSONString(),'quiz':firstQA}))



  return app

