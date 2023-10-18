from flask import Flask, render_template, redirect, flash, url_for
from models import db, connect_db, Pet
from forms import AddPet
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretKEY"
csrf = CSRFProtect(app)

connect_db(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

@app.route("/")
def homePage():
    pets = Pet.query.all()
    return render_template("home_page.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def addPetForm():
    form = AddPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        newPet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes, available=available)
        
        db.session.add(newPet)
        db.session.commit()

        flash(f"Added {name}")
        return redirect("/add")

    else:
        return render_template("add_pet_form.html", form=form)
    
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def showPet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet.name = name 
        pet.species = species
        pet.photo_url = photo_url
        pet.age = age
        pet.notes = notes
        pet.available = available
        
        db.session.commit()

        flash(f"Updated {name}")
        return redirect(url_for("showPet", pet_id=pet_id))
    else:
        return render_template("pet_detail.html", pet=pet, form=form)