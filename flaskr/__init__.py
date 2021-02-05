import os

from flask import Flask, render_template

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
  )
  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  # a simple page that says hello
  @app.route('/')
  def hello():
      return render_template('index.html')

  @app.route('/hackathon')
  def return_hackathon():
    mentors = [
      {'id': 0, 'name': 'Barbara Coco', 'occupation': 'AI researcher', 'summary': 'Working for social equity since 2043'},
      {'id': 1, 'name': 'Inbar Amaliya', 'occupation': 'AI researcher', 'summary': 'Hello, world!'},
      {'id': 2, 'name': 'Jakab Norberto', 'occupation': 'AI developer', 'summary': 'Hello, aerok..!'},
      {'id': 3, 'name': 'Methodius Onesimos', 'occupation': 'Policy maker', 'summary': 'Let us do our best together! :)'}
    ]
    samples = [
      {'id': 0, 'title': 'Impressive Work 💎', 'author': 'author_0', 'url': 'static/images/sample1.png'},
      {'id': 1, 'title': 'Magnificent Work 🔥', 'author': 'author_1', 'url': 'static/images/sample2.png'},
      {'id': 2, 'title': 'Quintessential Work', 'author': 'author_2', 'url': 'static/images/sample3.png'},
      {'id': 3, 'title': 'Phenomenal Work', 'author': 'author_3', 'url': 'static/images/sample4.png'},
      {'id': 4, 'title': 'Hardworking :) 👷', 'author': 'author_4', 'url': 'static/images/sample5.png'},
      {'id': 5, 'title': 'Brilliant Work ✨', 'author': 'author_5', 'url': 'static/images/sample6.png'},
    ]
    print(mentors)
    return render_template('hackathon.html', mentors=mentors, samples=samples)

  return app
