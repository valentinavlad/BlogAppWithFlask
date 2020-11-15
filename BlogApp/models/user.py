from app import db
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    posts = db.relationship('Post', backref='users', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


    def __repr__(self):
        return '<Post %r>' % self.title

    def __repr__(self):
        return '<User %r>' % self.username


