from .models import sessionLocal
from .models.car import Car
from .models.seller import Seller


def add_car():
    session = sessionLocal()
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter model year: "))
    condition = input("Enter car condition (new/used): ")
    price = int(input("Enter asking price: "))
    seller_name = input("Please enter your name: ")
    seller_contact = int(input("Please enter your contact number: "))
    seller_location = input("Please enter your location: ")


    seller = session.query(Seller).filter_by(name=seller_name).first()
    if not seller:
        seller = Seller(name=seller_name, contacts=seller_contact, location=seller_location)
        session.add(seller)
        session.commit()


    car = Car(make=make, model=model, year=year, condition=condition, price=price, seller_id=seller.id)
    session.add(car)
    session.commit()
    session.close()
    print("Your car has been uploaded successfully!")


def view_cars():
    session = sessionLocal()
    cars = session.query(Car).all()
    for car in cars:
        print(f"ID: {car.id}, Make: {car.make}, Model: {car.model}, Year: {car.year}, Condition: {car.condition}, Price: {car.price}")
        seller = session.query(Seller).filter_by(id=car.seller_id).first()
        print(f"Seller: {seller.name}, Contact: {seller.contacts}, Location: {seller.location}")
    session.close()



def delete_car():
    session = sessionLocal()
    car_id = int(input("Enter car ID to delete: "))
    car = session.query(Car).filter_by(id=car_id).first()
    if car:
        session.delete(car)
        session.commit()
        print("Car sold and deleted successfully!")
    else:
        print("Car not found.")
    session.close()



def update_car():
    session = sessionLocal()
    car_id = int(input("Enter car ID to update: "))
    car = session.query(Car).filter_by(id=car_id).first()
    if car:
        car.make = input(f"Enter new make (current: {car.make}): ") or car.make
        car.model = input(f"Enter new model (current: {car.model}): ") or car.model
        car.year = int(input(f"Enter new year (current: {car.year}): ") or car.year)
        car.condition = input(f"Enter new condition (current: {car.condition}): ") or car.condition
        car.price = int(input(f"Enter new price (current: {car.price}): ") or car.price)
        session.commit()
        print("Car details updated successfully!")
    else:
        print("Car not found.")
    session.close()   


def exit_program():
    print("Thank you for choosing CarBest!.Goodbye")
    exit()