from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, PickleType

db = SQLAlchemy()


class Article(db.Model):
    __tablename__ = "articles"
    doi = Column(String(250), primary_key=True, nullable=False)
    link = Column(String(250), unique=True, nullable=False)
    category = Column(PickleType, nullable=False)
    year = Column(Integer)
    title = Column(String(250), unique=True, nullable=False)
    problem_description = Column(String(250), nullable=False)
    solution_description = Column(String(250), nullable=False)
    result = Column(String(250), nullable=False)
    problems = Column(String(250), nullable=False)
    additional_notes = Column(String(500), nullable=True)
    addition_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)
    analysis_author = db.relationship('User', backref='authored_articles')

    def to_dict(self):
        return {
            'link': self.link,
            'year': self.year,
            'category': self.category,
            'title': self.title,
            'problem_description': self.problem_description,
            'solution_description': self.solution_description,
            'result': self.result,
            'problems': self.problems,
            'additional_notes': self.additional_notes,
            'addition_date': self.addition_date.isoformat(),
            'analysis_author': self.analysis_author.username,
            'doi': self.doi,
        }


class Password(db.Model):
    __tablename__ = "passwords"
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(250))


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(250), unique=True, nullable=False)
    is_admin = Column(Integer, nullable=False, default=False)
    articles = db.relationship("Article", backref="user", lazy=True)
