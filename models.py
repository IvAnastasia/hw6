from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
  #  __table_args__ = {'sqlite_autoincrement': True}

    # имя колонки = специальный тип (тип данных, первичный ключ)
    id = db.Column('id', db.Integer, primary_key=True)
    born_year = db.Column('born_year', db.Integer)
    gender = db.Column('gender', db.Text)
    education = db.Column('education', db.Text)
   # db.PrimaryKeyConstraint('id')
    responses = relationship("Responses", back_populates="user")

class Responses(db.Model):

    __tablename__ = "responses"

    id = db.Column('id', db.Integer, ForeignKey('user.id'), primary_key=True)
    stress = db.Column('stress', db.Integer)
    happiness = db.Column('happiness', db.Integer)
    proudness = db.Column('proudness', db.Integer)
    labor = db.Column('labor', db.Integer)
    two_leaders = db.Column('two_leaders', db.Integer)
    rules = db.Column('rules', db.Integer)
    user = relationship("User", back_populates="responses")


class Questions(db.Model):

    __tablename__ = "questions"

    question_id = db.Column('question_id', db.Integer, primary_key=True)
    question = db.Column('question', db.Text)
