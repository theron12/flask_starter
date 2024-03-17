from . import db
#from werkzeug.security import generate_password_hash

class Property(db.Model):
    __tablename__="property"

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(220))
    description=db.Column(db.Text())
    rooms=db.Column(db.String(4))
    bathrooms=db.Column(db.String(4))
    price=db.Column(db.String(15))
    ptype=db.Column(db.String(10))
    location=db.Column(db.String(255))
    photourl=db.Column(db.String(255))

    def __init__(self,title,desc,rooms,bathrooms,price,ptype,location,url):
        self.title=title
        self.description=desc
        self.rooms=str(rooms)
        self.bathrooms=bathrooms
        self.price=price
        self.ptype=ptype
        self.location=location
        self.photourl=url

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
