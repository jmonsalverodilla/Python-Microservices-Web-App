from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timedelta

db = SQLAlchemy()

class Predictions(db.Model):
    id = db.Column('ID',db.Integer, primary_key=True)
    OverallQual = db.Column(db.Integer,nullable=False)
    GrLivArea = db.Column(db.Integer, nullable=False)
    TotalBsmtSF = db.Column(db.Integer, nullable=False)
    CentralAir = db.Column(db.Text, nullable=False)
    FireplaceQu = db.Column(db.Text, nullable=True)
    BsmtFinSF1 = db.Column(db.Integer, nullable=False)
    LotArea = db.Column(db.Integer, nullable=False)
    GarageCars = db.Column(db.Integer, nullable=False)
    YearBuilt = db.Column(db.Integer, nullable=True)
    KitchenQual = db.Column(db.Text, nullable=True)
    Prediction = db.Column(db.Text, nullable=True)
    Time = db.Column(db.DateTime, default=datetime.now() + timedelta(hours=2))

    def __repr__(self):
        return '<ID %r>' % self.id