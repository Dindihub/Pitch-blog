
from unicodedata import category
from flask import render_template,url_for,redirect,flash
from . import main
from .forms import RegistrationForm,LoginForm,PitchForm
from .models import Pitch, User,Category
from app import db
from flask_login import login_user,current_user




@main.route('/')
def home():
    get_pitches=Pitch.query.all()
    return render_template('home.html',title='home',pitches=get_pitches)

@main.route('/about')
def about():
    return render_template('about.html',title='about')


@main.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    user_exist=User.query.filter_by(email=form.email.data).first() 
    if form.validate_on_submit() and user_exist is None: 
   
        user = User(username=form.username.data, email=form.email.data,
                password=form.password.data)

        print(form.username)
        db.session.add(user)
        db.session.commit()
        
        flash('Yaaaay! Thanks for registering!')

        return redirect(url_for('main.login'))
    flash('Username is taken')
    print('form invalid')
    print(form.username.data,form.email.data,form.password.data,form.confirm_password.data)
    return render_template('register.html',title='register',form=form)


@main.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user)
            flash('Thanks for logging in!')
        return redirect(url_for('main.pitch'))
    return render_template('login.html',title = 'login',form = form)


@main.route('/pitch',methods=['GET','POST'])
def pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, content=form.content.data,
                author=current_user.id,category=form.category.data)

        db.session.add(pitch)
        db.session.commit()

        flash('Thanks for your pitch!')
        return redirect(url_for('main.home'))
    return render_template('pitch.html',title = 'pitch',form = form)
    




