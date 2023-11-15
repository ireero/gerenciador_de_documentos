from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
app = Flask(__name__)

from calls import calls as calls_blueprint

app.register_blueprint(calls_blueprint)

from navigation import navigation as navigation_blueprint

app.register_blueprint(navigation_blueprint)

app.config['SECRET-KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///searchs.sqlite'

db.init_app(app)

with app.app_context():
    db.create_all()
    if __name__ == '__main__':
        app.run(debug=False)