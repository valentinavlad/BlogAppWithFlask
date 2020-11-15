from app import db

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    owner =  db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    contents = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __init__(self, title, owner, contents):
        self.title = title
        self.owner = owner
        self.contents = contents

    def __repr__(self):
        return '<Post %r>' % self.title
