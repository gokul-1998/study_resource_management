from flask_security import SQLAlchemyUserDatastore
from .models import db, User, Role
datastore = SQLAlchemyUserDatastore(db.session, User, Role)