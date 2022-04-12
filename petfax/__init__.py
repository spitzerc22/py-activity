#here, we want to configure Flask and write the function that will create the instance of our app

#configurations
from flask import Flask

#application factory
def create_app():
    app = Flask(__name__)

    @app.route('/')

    def hello():
        return "Helloo, PetFax!"
    
    #register blueprint
    from petfax import pet
    app.register_blueprint(pet.bp)


    return app
