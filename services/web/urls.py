from project import app
from views import *

app.add_url_rule('/', view_func=student_list, endpoint='students_list')
app.add_url_rule('/student/<int:id>', view_func=student_detail,
                 endpoint='student_detail')
app.add_url_rule('/student/create', view_func=student_create,
                 methods=['GET', 'POST'], endpoint='student_create')
app.add_url_rule('/student/<int:id>/update', view_func=student_update,
                 methods=['GET', 'POST'], endpoint='student_update')
app.add_url_rule('/student/<int:id>/delete', view_func=student_delete,
                 methods=['GET', 'POST'], endpoint='student_delete')


app.add_url_rule('/course/create', view_func=course_create, methods=['GET', 'POST'],
                 endpoint='course_create')
app.add_url_rule('/course/<int:id>/update', view_func=course_update,
                 methods=['GET', 'POST'], endpoint='course_update')
app.add_url_rule('/course/<int:id>/delete', view_func=course_delete,
                 methods=['GET', 'POST'], endpoint='course_delete')


app.add_url_rule('/register', view_func=register_view, methods=["GET", "POST"], endpoint='register')
app.add_url_rule('/login', view_func=login_view, methods=["GET", "POST"], endpoint='login')
app.add_url_rule('/logout', view_func=logout_view, endpoint='logout_view')
