from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
posts =[
    {
        'title': 'First Post',
        'author': 'Soumya Sen',
        'content': 'This is first Post',
        'date_posted': '07 September, 2020'
    }, 
    {
        'title': 'Second Post',
        'author': 'Pranoy Das',
        'content': 'This is second Post',
        'date_posted': '07 September, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account is successfully created! You can login now.','success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "soumya@sen.com" and form.password.data == "password":
            flash(f'{form.email.data} is successfully logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful. Please check the username and password",'danger')
    return render_template('login.html', title="Register", form=form)