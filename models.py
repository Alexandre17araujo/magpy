from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# Criei uma classe de projeto que é chamada no arquivo main.
class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    packages = db.relationship("Package", back_populates="project", cascade="all, delete-orphan")


# Criei uma classe de package que é chamada no arquivo main.
class Package(db.Model):
    __tablename__ = 'package'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    version = db.Column(db.String)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=False)
    project = db.relationship("Project", back_populates="packages")
