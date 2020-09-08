from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='441419fab395443e1a8b5141d59f1c77'
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
        flash(f'Account is successfully created for {form.username.data} !!!','success')
        return redirect(url_for('home'))
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






if __name__ == "__main__":
    app.run(debug=True)