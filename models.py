from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)



class Pet(db.Model):
    """Department Model"""

    __tablename__ = "departments"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, unique=True)
    age = db.Column( db.Integer)
    notes = db.Column( db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)


    def __repr__(self):
        return f"<Department {self.dept_code} {self.dept_name} {self.phone} >"
