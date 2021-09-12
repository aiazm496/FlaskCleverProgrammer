import re
from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'  #sqlite stories db locally at location of app.py
db = SQLAlchemy(app)

#modeling the database - defining structure of db in a class 
class BlogPost(db.Model): #BlogPost inherited the db.Model class
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    author = db.Column(db.String(20), nullable = False, default = 'N/A')
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)


all_posts = [

    {
        'title': 'Post 1',
        'content': 'This is the content of post 1.lalala',
        'author' : 'travosky'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2. lalala '
    }

]

@app.route('/')
def index():
    return render_template('index.html') #it auto checks in templates folder
    #and renders the index.html on route '/'

@app.route('/posts')
def posts():
    return render_template('posts.html', posts = all_posts)
# we have defined variable posts here to store all_data
# now we have write code in html to display it on posts.html


#@app.route('/') #nothing in url it is like localhost:5000/
@app.route('/home/<string:name>')  # it is like localhost:5000/home
def hello(name):  #runs when above url is hit, currently both / and home will return Hello World
    return "Hello, " + name

@app.route('/home/users/<string:name>/posts/<int:id>')
def helloUser(name,id):
    return "Hello, " + name + ", your id is: " + str(id)

@app.route('/onlyget',methods = ['GET'])
def get_req():
    return "You can only get this webpage"


if __name__ == '__main__':  #to see messages in cmd
    app.run(debug=True) 




