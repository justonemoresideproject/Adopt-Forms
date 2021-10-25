from flask import Flask, request, redirect, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

SECRET_KEY = 'abcdefg'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = SECRET_KEY

connect_db(app)
db.create_all()

@app.route('/')
def homepage():
    """Homepage for adoption site"""
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/newPet', methods=['GET', 'POST'])
def newPet():
    """ """
    title='Add a pet!'
    form = PetForm()
    if form.validate_on_submit():
        newPet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data,
            is_available = form.is_available.data
        )

        db.session.add(newPet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('pet.html', form=form, title=title)

@app.route('/editPet/<int:pet_id>', methods=['GET', 'POST'])
def editPet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    title = f'Edit {pet.name}'
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data,
        pet.species = form.species.data,
        pet.photo_url = form.photo_url.data,
        pet.age = form.age.data,
        pet.notes = form.notes.data,
        pet.is_available = form.is_available.data

        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet.html', form=form, title=title)
