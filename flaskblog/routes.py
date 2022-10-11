from flaskblog.models import User, Post
from flaskblog import app
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
# with app.app_context():
#         db.create_all()
#         user_1 = User(username='zizhan', email='z@demo.com', password='password')
#         db.session.add(user_1)
# user_2 = User(username='xixi', email='xixi@demo.com', password='password')

posts = [
    {
        'author': 'Zizhan Zhou',
        'title': 'The last dance',
        'content': 'Best documentary ever',
        'date_posted': 'March 10, 2000'
    },
    {
        'author': 'JK Rowling',
        'title': 'Harry Potter',
        'content': 'Harry is a pretty cool guy',
        'date_posted': 'October 1st, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): 
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data  == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid login credentials, please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)