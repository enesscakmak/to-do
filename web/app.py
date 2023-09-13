# This to-do website created on 05.09.2023 by Enes Çakmak

import os

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired
from wtforms.fields import DateField
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
Bootstrap5(app)
db.init_app(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


class AddTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description')
    priority = IntegerField('Priority')
    finish_by = DateField('Finish by', format="%Y-%m-%d")
    completed = BooleanField('Complete')
    submit = SubmitField('Add')


class EditTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description')
    priority = IntegerField('Priority', validators=[DataRequired()])
    finish_by = DateField('Finish by', format="%Y-%m-%d")
    completed = BooleanField('Complete')
    submit = SubmitField('Update')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tasks')
def tasks():
    return render_template('tasks.html', tasks=Task.query.all())


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddTaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            finish_by=form.finish_by.data,
            completed=form.completed.data
            )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks'))
    return render_template('add.html', form=form)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Task.query.get(id)
    form = AddTaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.priority = form.priority.data
        task.finish_by = form.finish_by.data
        task.completed = form.completed.data
        db.session.commit()
        return redirect(url_for('tasks'))
    return render_template('edit.html', form=form)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks'))


@app.route('/details/<int:id>', methods=['GET', 'POST'])
def details(id):
    task = Task.query.get(id)
    return render_template('details.html', task=task)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
