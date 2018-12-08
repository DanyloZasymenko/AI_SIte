from flask_login import UserMixin

from ai_site import login_manager


@login_manager.user_loader
def load_user(user_id):
    user = User()
    return user


class User(UserMixin):
    id = 1
    username = 'admin'
    # bCrypt.generate_password_hash(password).decode('utf-8')
    password = '$2b$12$/3ubZUjTw0H/g.TgMRcxt.3N8EzO9q.zi7f3LG7u1W9DARMMGL7Mi'
