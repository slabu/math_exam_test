from flask_login import UserMixin, current_user

from db import db

class ProgressModel(db.Model):
    __tablename__ = "user_progress"

    row_id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False)
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

    def __init__(self, task_id, task_text, task_correct_answer, task_answer_1, task_answer_2, task_answer_3, task_answer_4, task_chosen_answer, task_mark, date_of_pass, user_id):
        self.task_id = task_id
        self.task_text = task_text
        self.task_correct_answer = task_correct_answer
        self.task_answer_1 = task_answer_1
        self.task_answer_2 = task_answer_2
        self.task_answer_3 = task_answer_3
        self.task_answer_4 = task_answer_4
        self.task_chosen_answer = task_chosen_answer
        self.task_mark = task_mark
        self.date_of_pass = date_of_pass
        self.user_id = user_id

    @classmethod
    def find_by_id(cls, task_id):
        return ProgressModel.query.filter_by(task_id=task_id).first()

    @classmethod
    def find_date_by_user(cls, user_id):
        return ProgressModel.query.group_by(ProgressModel.date_of_pass).filter_by(user_id=user_id)

    @classmethod
    def get_all_statistics(cls, user_id):

        statistics = {}
    

        for date in ProgressModel.find_date_by_user(user_id):
            statistics[str(date.date_of_pass)] = {
                                        'count_of_tasks': '0',
                                        'count_of_skipped_tasks': 0,
                                        'count_of_correct_answers': 0,
                                        'mark': 0
            }

            statistics[str(date.date_of_pass)]['count_of_tasks'] = len(ProgressModel.query.filter_by(user_id=user_id, date_of_pass=date.date_of_pass).all())
            statistics[str(date.date_of_pass)]['count_of_skipped_tasks'] = len(ProgressModel.query.filter_by(user_id=user_id, date_of_pass=date.date_of_pass, task_chosen_answer='Завдання пропущено').all())
            statistics[str(date.date_of_pass)]['count_of_correct_answers'] = len(ProgressModel.query.filter_by(user_id=user_id, date_of_pass=date.date_of_pass, task_mark=1).all())
            statistics[str(date.date_of_pass)]['mark'] = f"{statistics[str(date.date_of_pass)]['count_of_correct_answers']} із {statistics[str(date.date_of_pass)]['count_of_tasks']}"

        return statistics
    
    @classmethod
    def get_all_tasks_by_user_date(cls, user_id, date_of_pass):
        return ProgressModel.query.filter_by(user_id=user_id, date_of_pass=date_of_pass).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
