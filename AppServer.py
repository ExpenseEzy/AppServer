from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ExpenseEzy.db'

db = SQLAlchemy(app)

class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    def __repr__(self):
        return '{}-{}'.format(self.username, self.email)

db.create_all()

@app.route('/signup', methods=["POST", "GET"])
def signup_user():
    if request.method == "POST":
        data = request.get_json()
        print data
        u = Users(data.get('username'), data.get('userId'), data.get('password'))
        db.session.add(u)
        db.session.commit()
        return jsonify({'signUpSuccess': 'true'})
    elif request.method == "GET":
        return 'Hello World!'

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)



