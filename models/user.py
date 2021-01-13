from flask_login import UserMixin, current_user

from db import db

class UserModel(db.Model, UserMixin):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(50), nullable=False, unique=True)
    user_password = db.Column(db.String(100), nullable=False)
    user_access_level = db.Column(db.String(50), nullable=False)

    def get_id(self):
        return(self.user_id)

    @classmethod
    def find_by_login(cls, login):
        return UserModel.query.filter_by(user_login=login).first()
    
    @classmethod
    def find_by_id(cls, user_id):
        return UserModel.query.filter_by(user_id=user_id).first()
    
    @classmethod
    def get_current_user(cls):
        username = UserModel.query.filter_by(user_id=current_user.get_id()).first()
        return username.user_login

    @classmethod
    def get_all_users(cls):
        return UserModel.query.all()

    @classmethod
    def delete_user(cls, user_id):
        UserModel.query.filter_by(user_id=user_id).delete()
        db.session.commit()
        return True

    def edit_user(self, new_access_level):
        self.query.filter(UserModel.user_id==self.user_id).update({'user_access_level': new_access_level})
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
