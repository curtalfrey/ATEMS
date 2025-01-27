from flask import Flask
from extensions import db, login_manager, admin, migrate, init_app
from models.user import User
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    
    # Configure logging
    logging.basicConfig(level=logging.DEBUG if os.getenv("DEBUG", "False").lower() == "true" else logging.INFO)
    logger = logging.getLogger(__name__)
    
    try:
        # Set the database URI from environment variable
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
        if not app.config["SQLALCHEMY_DATABASE_URI"]:
            raise ValueError("No SQLALCHEMY_DATABASE_URI set in environment variables.")
    except Exception as e:
        logger.error(f"Error setting database URI: {e}")
        raise

    # Set the secret key from environment variable
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    if not app.config["SECRET_KEY"]:
        raise ValueError("No SECRET_KEY set in environment variables.")
    
    # Set the debug mode from environment variable
    app.config["DEBUG"] = os.getenv("DEBUG", "False").lower() == "true"
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    init_app(app)
    
    logger.info("Application initialized successfully.")
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])
