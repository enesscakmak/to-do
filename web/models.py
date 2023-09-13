from sqlalchemy import Date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())
    priority = db.Column(db.String(10), nullable=False)
    finish_by = db.Column(Date)  # Use Date column type
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, description, priority, finish_by, completed):
        self.title = title
        self.description = description
        self.priority = priority
        self.finish_by = finish_by
        self.completed = completed
