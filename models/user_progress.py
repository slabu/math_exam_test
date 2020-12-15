from flask_login import UserMixin, current_user

from db import db

class ProgressModel(db.Model):
    __tablename__ = "user_progress"

    row_id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False, unique=True)
    task_text = db.Column(db.String(1000), nullable=False)
    task_correct_answer = db.Column(db.String(125), nullable=False)
    task_answer_1 = db.Column(db.String(200), nullable=False)
    task_answer_2 = db.Column(db.String(200), nullable=False)
    task_answer_3 = db.Column(db.String(200), nullable=False)
    task_answer_4 = db.Column(db.String(200), nullable=False)
    task_chosen_answer = db.Column(db.String(200), nullable=False)
    task_mark = db.Column(db.String(100), nullable=False)
    date_of_pass = db.Column(db.DateTime, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship('UserModel', backref=db.backref('progress_user', lazy=True))

    @classmethod
    def find_by_id(cls, task_id):
        return ProgressModel.query.filter_by(task_id=task_id).first()

    @classmethod
    def find_by_user(cls, user_id):
        return ProgressModel.query.filter_by(user_id=user_id).distinct(date_of_pass).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
