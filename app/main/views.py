from flask import render_template,flash,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User,Pitch
from .. import db,photos
from .forms import UpdateProfile, AddPitch



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Pitch Deck'
    
    return render_template('index.html', title = title) 

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user) 

@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)   

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    

@main.route('/user/<pitchname>/pitch',methods = ['GET','POST'])
@login_required
def newpitch(pitchname):
    
    form = AddPitch()

    if form.validate_on_submit():
        
        pitch = Pitch(content=form.content.data,name=form.title.data)
        db.session.add(pitch)
        db.session.commit()


        flash('Your pitch has been posted!', 'success')
        return redirect(url_for('main.newpitch',pitchname=pitch.name))
    title = 'Add a new Pitch'
    return render_template('new_pitch.html',form =form)   

@main.route('/categories')
def categories():

    title = 'Pitches | Categories'

    return render_template('categories.html',title =title)            