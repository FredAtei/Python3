from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
from ..models import Reviews, User



@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):

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