from app import  app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

    admin_user = UserModel(user_login='admin', user_password='admin', user_access_level='admin')
    admin_user.save_to_db()