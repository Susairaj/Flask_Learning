from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template , request ,redirect,url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://odoo:odoo@localhost/flaskmovie'
app.debug =True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self,username,email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/')
def index():
    myuser = User.query.all()
    oneitem = User.query.filter_by(username='Admin').first()
    return render_template('add_user.html', myuser = myuser, oneitem=oneitem)

if __name__ == '__main__':
    app.run()