from flask_wtf import FlaskForm
import wtforms as ws
from app import app, Course
from datetime import date


class CourseForm(FlaskForm):
    course_name = ws.StringField('Наименование курса', validators=[ws.validators.DataRequired(), ])
    duration = ws.IntegerField('Длительность курса', validators=[ws.validators.DataRequired(), ])


class UserForm(FlaskForm):
    username = ws.StringField('имя пользователя', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=4, max=20)
    ])
    password = ws.PasswordField('Пароль', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=8, max=24)
    ])


class StudentForm(FlaskForm):
    name = ws.StringField('ФИО студента', validators=[ws.validators.DataRequired(), ])
    birth_date = ws.DateField('дата рождения', validators=[ws.validators.DataRequired(), ])
    phone_number = ws.StringField('Номер телефона', validators=[ws.validators.length(min=13, max=13)])
    course_id = ws.SelectField('Курс', choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.course_choices = []
        with app.app_context():
            for course in Course.query.all():
                self.course_choices.append((course.id, course.course_name))
        self._fields['course_id'].choices = self.course_choices

    def validate(self):

        if not super().validate():
            return False
        error_counter = 0

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        names_split = self.name.data.split(' ')
        if len(names_split) == 1:
            self.name.errors.append("ФИО не может состоять из одного слова")
            error_counter += 1
        for name in names_split:
            if not name.isalpha():
                self.name.errors.append('имя не должно содержать цифры и спец.символы')
                error_counter += 1
        for a in self.name.data.lower():
            if a in alphabet:
                self.name.errors.append('имя должно быть на кирилице')
                error_counter += 1
        if date.today().year - self.birth_date.data.year < 18:
            self.birth_date.errors.append('только старше 18лет')
            error_counter += 1
        if self.phone_number.data[0] != '+':
            self.phone_number.errors.append('неверно')
            error_counter += 1

        if error_counter == 0:
            return True
        else:
            return False
