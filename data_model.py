from flask_sqlalchemy import SQLAlchemy

# create a class instance
DB = SQLAlchemy()


# do OOP we did before

class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String, nullable=False)  # cannot be null

    def __repr__(self):
        return f'<User: {self.name}>'


class Tweet(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
