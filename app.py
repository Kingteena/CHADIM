import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialise flask app
app = Flask(__name__)

# Database stuff
app.secret_key = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    __tablename__ = "items"
    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search')
def search():
    pass


@app.route('/login')
def login():
    pass

@app.route('/update')
def update():
    pass


if __name__ == '__main__':
    # noinspection FlaskDebugMode
    app.run(debug=True)
