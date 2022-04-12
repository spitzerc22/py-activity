from flask import Blueprint, render_template, json

pets = json.load(open('pets.json'))
print(pets)

#new instance of blueprint
bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')

def index():
    return render_template('index.html', pets=pets)

#^^ make sure to import and register blueprint in APP FACTORY