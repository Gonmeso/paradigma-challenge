from people import db

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    is_alive = db.Column(db.Boolean)
    place_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Place {}>, {}'.format(self.name)