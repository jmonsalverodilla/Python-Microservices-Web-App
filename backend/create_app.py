import os
from flask import Flask
from models import db
from flask_migrate import Migrate
#from pathlib import Path
#from dotenv import load_dotenv,find_dotenv
#dotenv_path = os.path.join(Path(__file__).parent.parent, '.env')
#load_dotenv(find_dotenv())

DBUSER=os.environ.get("POSTGRES_USER")
DBPASS=os.environ.get("POSTGRES_PASSWORD")
DBHOST=os.environ.get("POSTGRES_DB_HOST")
DBPORT=os.environ.get("POSTGRES_DB_PORT")
DBNAME=os.environ.get("POSTGRES_DB_NAME")

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # basedir = Path(__file__).parent
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(Path().joinpath(basedir, 'logger.sqlite3'))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}:{DBPORT}/{DBNAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    app.app_context().push()
    db.create_all()
    return app

app = create_app()

if __name__=='__main__':
    app.run()