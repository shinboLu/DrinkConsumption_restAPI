from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
import json
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200))

    # def __init__(self, id, name, description):
    #     self.id = id
    #     self.name = name
    #     self.description = description

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'hello'


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return {'drinks': output}


@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return jsonify({"name": drink.name, "description": drink.description})


@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'],
                  description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {'error': 'not found'}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "deleted"}
