from . import db
import datetime

class Student(db.Model):
    __tablename__ = 'student'
    studentId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.DateTime, nullable = False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
  
    def __repr__(self):
        return '<Student %r>' % self.studentId

class Tutor(db.Model):
    __tablename__ = 'tutor'
    tutorId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable = False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
   
    def __repr__(self):
        return '<Tutor %r>' % self.tutorId

class Subjects(db.Model):
    __tablename__ = "subjects"
    subjectId = db.Column(db.Integer, primary_key=True)
    tutorId = db.Column(db.Text, db.ForeignKey('tutor.tutorId'))
    className = db.Column(db.Text)
    countryName = db.Column(db.Text)
    language = db.Column(db.Text)
    duration = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
        return '<Subjects %r>' % self.subjectId
       
class Lecture(db.Model):
    __tablename__ = "lecture"
    lectureId = db.Column(db.Integer, primary_key="True")
    classId = db.Column(db.Integer, db.ForeignKey('subjects.subjectId'), nullable=False)
    title = db.Column(db.Text, nullable="False")
    file = db.Column(db.LargeBinary)
    contents = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
        return '<Lecture %r>' % self.lectureId