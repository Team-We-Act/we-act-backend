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

    def __init__(self, className, subject):
        self.className = className
        self.subject = subject
    def toJSONString(self):
        return '{'+'className:'+self.className+',subject'+self.subject+'}'

class Lecture(db.Model):
    lectureId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=True)
    content = db.Column(db.String(500), nullable=True)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class Quiz(db.Model):
    quizId = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(50), nullable=True)
    answer = db.Column(db.String(50), nullable=True)
    response = db.Column(db.String(50), nullable=True)

    def __init__(self, question, answer, response):
        self.question = question
        self.answer = answer
        self.response = response