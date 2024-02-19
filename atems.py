# atems.py
 
from flask import Flask
from extensions import db, login_manager, admin, migrate, init_app
from models.user import User




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




def create_app():
   
    app = Flask(__name__)
    
    # Set the database URI from environment variable
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://CLU:123!z2@localhost/ATEMS" 
    

    # Set the secret key from environment variable
    app.config["SECRET_KEY"] = "abc123"
    
    # Set the debug mode from environment variable
    app.config["DEBUG"] = "True"
    

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    init_app(app)
    return app



app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# Final newline added
