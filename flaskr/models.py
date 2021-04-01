from . import db
import datetime

class Student(db.Model):
    __tablename__ = 'student'
    studentId = db.Column(db.Integer, primary_key=True)
    subjectId = db.Column(db.Text, db.ForeignKey('subject.subjectId'))
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable = False)
    created = db.Column(db.Text, nullable=False, default=datetime.datetime.now)
    subject = db.relationship("Subject", back_populates="student")
  
    def __repr__(self):
        return '<Student %r>' % self.studentId

class Tutor(db.Model):
    __tablename__ = 'tutor'
    tutorId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable = False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    subject = db.relationship("Subject", back_populates="tutor")
   
    def __repr__(self):
        return '<Tutor %r>' % self.tutorId

class Subject(db.Model):
    __tablename__ = "subject"
    subjectId = db.Column(db.Integer, primary_key=True)
    tutorId = db.Column(db.Text, db.ForeignKey('tutor.tutorId'))
    className = db.Column(db.Text)
    countryName = db.Column(db.Text)
    language = db.Column(db.Text)
    duration = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    student = db.relationship("Student", back_populates="subject")
    tutor = db.relationship("Tutor", back_populates="subject")
    lecture = db.relationship("Lecture", back_populates="subject")

    def __repr__(self):
        return '<Subjects %r>' % self.subjectId
       
class Lecture(db.Model):
    __tablename__ = "lecture"
    lectureId = db.Column(db.Integer, primary_key="True")
    subjectId = db.Column(db.Integer, db.ForeignKey('subject.subjectId'), nullable=False)
    title = db.Column(db.Text, nullable="False")
    file = db.Column(db.LargeBinary)
    contents = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    subject = db.relationship("Subject", back_populates="lecture")

    def __repr__(self):
        return '<Lecture %r>' % self.lectureId