from flask_app import db

class Tweet(db.Model):
    __tablename__ = 'tweet'

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.Text())
    embedding = db.Column(db.PickleType())
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Tweet {self.id}"