from flask import Flask, json, request
from flask.views import MethodView


class UserView(MethodView):
    USERS = {}

    def get(self, name):
        if name in UserView.USERS:
            return {"data": f"My name is {name}"}, 200
        return {"errors": {"data": "There is no user with this name"}}, 404

    def post(self):
        data = json.loads(request.data)
        name = data.pop('name', None)
        if name is None:
            return {"errors": {"name": "This field is required"}}, 422
        UserView.USERS[name] = data
        return {"data": f"User {name} is created!"}, 201

    def patch(self, name):
        if not name in UserView.USERS:
            return {"errors": {"data": "There is no user with this name"}}, 404
        data = json.loads(request.data)
        new_name = data.pop('name', None)
        if new_name is None:
            return {"errors": {"name": "This field is required"}}, 422
        UserView.USERS[new_name] = UserView.USERS[name]
        del UserView.USERS[name]
        return {"data": f"My name is {new_name}"}, 200

    def delete(self, name):
        if not name in UserView.USERS:
            return {"errors": {"data": "There is no user with this name"}}, 404
        del UserView.USERS[name]
        return '', 204


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        user_view = UserView.as_view('user_view')
        app.add_url_rule('/user/', methods=['POST'],
                         view_func=user_view)
        app.add_url_rule('/user/<string:name>/',
                         methods=['GET', 'PATCH', 'DELETE'],
                         view_func=user_view)
