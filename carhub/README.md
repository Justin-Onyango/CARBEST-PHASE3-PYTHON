# CarBest

## Brief Description
CarBest is an online car dealership aiming to connect buyers and sellers seamlessly and completely eradicate cases of shady dealers. Through it's easy to use platform, the users have an easy time navigating through the site.

## Set-up and Running
1. Open the terminal and run 'pipenv install' followed by 'pipenv shell'
2. Set up the database 'python setup_db.py'
3. Run 'python -m lib.cli' to start the session
4. There are five actions provided namely, Exit, Upload a car, Sell my car, Update my car details and View all cars

## Features
This is a CLI application that primarily relies on python
1. Upload a car.
        This enables the user to upload a new car to the database. There are several prompts that the user follows before successfully uploading the vehicle.
        This feature represents the CREATE functionality.
2. Sell my car.
        This feature enables the seller to delete the car from the database once it is sold.The seller has to enter the specific id of the car to avoid deleting unintentionally another car or worse, the whole database.
        The feature represents the DELETE functionality.
3. Update my car details.
        The feature allows the seller to update any information about the car that may have been captured incorrectly during the upload process.
        The feature represents the UPDATE functionality.
4. View all cars.
        When the user chooses this prompt, the whole database will be displayed with all the available cars. The seller details will also be displayed.
        The feature represents the READ functionality.