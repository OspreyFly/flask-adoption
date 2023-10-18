from models import Pet, db
from app import app

if __name__ == '__main__':
    # Create an application context
    with app.app_context():
        # Drop and recreate the database tables
        db.drop_all()
        db.create_all()

        pet1 = Pet(name="Dobby", species="dog", photo_url="https://highlandcanine.com/wp-content/uploads/2020/12/iStock-926735822.jpg", age="4", notes="Loves belly rubs", available=True)
        pet2 = Pet(name="Rooster", species="dog", photo_url="https://www.vidavetcare.com/wp-content/uploads/sites/234/2022/04/chihuahua-dog-breed-info.jpeg", age="5", notes="Loves treats", available=False)
        pet3 = Pet(name="Bilbo", species="dog", photo_url="https://cdn.britannica.com/07/234207-050-0037B589/English-bulldog-dog.jpg", age="3", notes="Beautiful cheeks", available=True)

        db.session.add(pet1)
        db.session.add(pet2)
        db.session.add(pet3)

        db.session.commit()

