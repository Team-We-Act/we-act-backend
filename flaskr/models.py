from . import db
import datetime

class User(db.Model):
    __tablename__ = 'user'

    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.Text, nullable=False)
    userType = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
        return '<User %r>' % self.userId

class Class(db.Model):
    __tablename__ = 'class'

    classId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.userId'))
    className = db.Column(db.Text)
    countryName = db.Column(db.Text)
    language = db.Column(db.Text)
    duration = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
        return '<Class %r>' % self.classId

class Lecture(db.Model):
    __tablename__ = "lecture"

    lectureId = db.Column(db.Integer, primary_key="True")
    classId = db.Column(db.Integer, db.ForeignKey('class.classId'), nullable=False)
    title = db.Column(db.Text, nullable="False")
    file = db.Column(db.LargeBinary)
    contents = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
        return '<Lecture %r>' % self.lectureId