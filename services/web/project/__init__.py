from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import UserMixin
from sqlalchemy import UniqueConstraint


app = Flask(__name__)

app.config.from_object("project.config.Config")
app.config['SECRET_KEY'] = 'superkey'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String)
    duration = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.course_name}-{self.duration}'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birth_date = db.Column(db.Date)
    phone_number = db.Column(db.String)
    course = db.relationship(Course, backref=db.backref('students', lazy='dynamic'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    __table_args__ = (UniqueConstraint('name', 'phone_number',
                                       name='_question_answer_uc'),
                      )

    def __repr__(self):
        return self.name


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.username

    @property
    def password(self):
        return None

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
