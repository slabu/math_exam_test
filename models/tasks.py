from db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True)
    task_text = db.Column(db.String(1000), nullable=False)
    task_answers = db.Column(db.String(500), nullable=False)
    task_correct_answer = db.Column(db.String(125), nullable=False)
    task_datetime_of_creation = db.Column(db.DateTime, nullable=False)
    
    user_id = db.Column(db.Integer, db.Foreignkey('user.user_id'), nullable=False)
    user = db.relationship('UserModel', backref=db.backref('user', lazy=True))

    def __init__(self, task_text, task_answers, task_correct_answer, user_id):
        self.task_text = task_text
        self.task_answers = task_answers
        self.task_correct_answer = task_correct_answer
        self.user_id = user_id

    @classmethod
    def find_by_id(cls, task_id):
        return TaskModel.query.filter_by(task_id=task_id).first()

    def save_task_to_db():
        db.session.add(self)
        db.session.commit()
    
