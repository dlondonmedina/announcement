from app import db

class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text())
    datetime = db.Column(db.DateTime())
    location = db.Column(db.String(200))

