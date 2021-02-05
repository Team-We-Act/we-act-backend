import json

# import sys
# import os
# os.chdir()
from . import db

class Student(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20), nullable=False)

    def __init__(self, userName):
        self.userName = userName


class Tutor(db.Model):
    tutorId = db.Column(db.Integer, primary_key=True)
    tutorName = db.Column(db.String(20), nullable=False)

    def __init__(self, tutorName):
        self.tutorName = tutorName


class Classes(db.Model):
    classId = db.Column(db.Integer, primary_key=True)
    className = db.Column(db.String(20), nullable=True)
    subject = db.Column(db.String(20), nullable=True)
    country=db.Column(db.String(20),nullable=True)
    language=db.Column(db.String(30),nullable=True)

    def __init__(self, className, subject,country,language):
        self.className = className
        self.subject = subject
        self.country=country
        self.language=language
    def toJSONString(self):
        return json.dumps({'className':self.className,'subject':self.subject,'country':self.country,
                           'language':self.language})
        # return '{'+'"className":'+self.className+'\n,"subject":'+self.subject+'}'

class Lecture(db.Model):
    lectureId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=True)
    content = db.Column(db.String(500), nullable=True)
    className=db.Column(db.String(30),nullable=True)
    lecturer=db.Column(db.String(20),nullable=True)
    def __init__(self, title, content,className,lecturer):
        self.title = title
        self.content = content
        self.className=className
        self.lecturer=lecturer

    def toJSONString(self):
        return json.dumps({'lectureId':self.lectureId,'title':self.title,'content':self.content,'className':self.className,'lecturer':self.lecturer})


class Quiz(db.Model):
    quizId = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(50), nullable=True)
    answer = db.Column(db.String(50), nullable=True)
    response = db.Column(db.String(50), nullable=True)

    def __init__(self, question, answer, response):
        self.question = question
        self.answer = answer
        self.response = response

    def toJSONString(self):
        return json.dumps({'quizId':self.quizId,
                           'question': self.question,
                           'answer': self.answer,
                           'response':self.response})