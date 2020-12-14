from datetime import datetime

from db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True)
    task_text = db.Column(db.String(1000), nullable=False)
    task_correct_answer = db.Column(db.String(125), nullable=False)
    answer_1 = db.Column(db.String(200), nullable=False)
    answer_2 = db.Column(db.String(200), nullable=False)
    answer_3 = db.Column(db.String(200), nullable=False)
    answer_4 = db.Column(db.String(200), nullable=False)
    task_datetime_of_creation = db.Column(db.DateTime, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship('UserModel', backref=db.backref('user', lazy=True))

    def __init__(self, task_text, answer_1, answer_2, answer_3, answer_4, task_correct_answer, user_id):
        self.task_text = task_text
        self.task_correct_answer = task_correct_answer
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.answer_4 = answer_4
        self.task_datetime_of_creation = datetime.now()
        self.user_id = user_id

    @classmethod
    def find_by_id(cls, task_id):
        return TaskModel.query.filter_by(task_id=task_id).first()

    @classmethod
    def get_all_tasks(cls):
        return TaskModel.query.all()

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()
    
