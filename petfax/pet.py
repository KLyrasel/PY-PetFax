from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('pets/index.html', pets = pets)

@bp.route('/<int:pet_id>')
def one_pet(pet_id):
    pet = pets[pet_id-1]
    return render_template('pets/pet_page.html', pet=pet)