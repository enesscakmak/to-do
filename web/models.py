from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    priority = db.Column(db.Integer, default=1)
    finish_by = db.Column(db.String(120), nullable=False)
    completed = db.Column(db.Boolean, default=False)