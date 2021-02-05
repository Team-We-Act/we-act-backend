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
    samples = [
      {'country': '필리핀', 'subject1': '아두이노 따라잡기', 'subject2': '포토샵 일러스트 도전해보기'},
      {'country': '우간다', 'subject1': 'MS Office 시작하기', 'subject2': '앱인벤터의 신비함'},
      {'country': '탄자니아', 'subject1': '아두이노 고급', 'subject2': 'AutoCAD란?'},
    ]
    target_sample = {
      'className': '쉽게 배우는 프로그래밍', 
      'countryName': '우간다',
      'language': '영어',
      'duration': '2021년 02월 ~ 2020년 05월',
      'subject': 'C++ 언어'
    };
    lectures_sample = [
      {'title': 'HTML 튜토리얼', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요!'},
      {'title': '자바스크립트 입문', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요! 으악 코딩 너무 힘들어요.....'},
      {'title': '타입스크립트 시작하기', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요!'},
      {'title': '리액트 프로그래밍 입문', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요!'},
      {'title': '리액트 프로그래밍 입문', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요!'},
      {'title': '리액트 프로그래밍 입문', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요!'},
            {'title': '리액트 프로그래밍 입문', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요!'},
      {'title': '리액트 프로그래밍 입문', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요!'},

    ]
    return render_template('volunteer_classes.html', 
      contents=samples, 
      target=target_sample,
      lectures=lectures_sample
      )

  @app.route('/recipient_classes')
  def hello_recipient_classes():
    return render_template('recipient_classes.html')


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
