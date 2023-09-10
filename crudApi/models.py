from crudApi import db

# Define the Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)    
    slack_username = db.Column(db.String(80), nullable=False)
    track = db.Column(db.String(80), nullable=False)

    def __init__(self, name, age, slack_username, track):
        self.name = name
        self.age = age
        self.slack_username = slack_username
        self.track = track
    

    def __repr__(self):
        return f'{self.name}'