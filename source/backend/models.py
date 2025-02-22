from server import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    watchlist = db.relationship('Movie', secondary='user_watchlist')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    rating = db.Column(db.Float)
    reviews = db.relationship('Review', backref='movie')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    review_text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20))

# Intermediate Table for User Watchlist
user_watchlist = db.Table('user_watchlist',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)

# Helper Method to Serialize Data
def to_dict(self):
    return {col.name: getattr(self, col.name) for col in self.__table__.columns}

User.to_dict = to_dict
Movie.to_dict = to_dict
Review.to_dict = to_dict

# Initialize Database
db.create_all()
