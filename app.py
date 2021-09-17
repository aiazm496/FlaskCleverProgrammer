import re
from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect

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

    def __repr__(self):             #like java toString
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

@app.route('/posts',methods = ['GET','POST'])
def posts():
    if request.method == 'POST':  #request is what is sent by form
        post_title = request.form['title']
        post_content = request.form['content']
        author = request.form['author']
        new_post = BlogPost(title = post_title, content = post_content,author = author)

        #adding to db from form
        db.session.add(new_post)
        db.session.commit()  #to add permanently
        return redirect('/posts')  #url to return back

    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all() #list of BlogPost object like BlogPost 1
        return render_template('posts.html', posts = all_posts)
# we have defined variable posts here to store all_data
#from app import db,BlogPost
# now we have write code in html to display it on posts.html
#from app import db,BlogPost
# get BlogPost object by id obj = BlogPost.query.get(1)  enter id number
#to filter list of BlogPost object -> BlogPost.query.filter_by(title = 'Modi').all()
#to get title  of id 1-> BlogPost.query.get(1).title  id is always primary key
#to change BlogPost.query.get(1).title = 'Narendra Modi' and db.session.commit()
#delete a object 
# db.session.delete(BlogPost.query.get(3)) then db.session.commit()

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)  #return BlogPost object
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>')
def edit(id):
    post = BlogPost.query.get_or_404(id)  #return BlogPost object
    

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

@app.route('/who/<string:name>')
def who(name):
    return "My name is " + name + "."  + " I am " + str(25) + " yrs old."

if __name__ == '__main__':  #to see messages in cmd
    app.run(debug=True) 




