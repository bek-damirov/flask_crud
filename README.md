# flask_crud
реализована регистрация администратора дающий права доступа для добавления студентов и обучающих курсов.
курсы и студенты, можно редактировать и удалять,
пароли хешируются, 
проект завернут в Docker с базой данных Postgres.

запуск докера:
docker-compose build,
docker-compose up -d,
docker-compose exec web python manage.py create_db.
