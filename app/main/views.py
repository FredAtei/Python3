from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required



@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch Deck'

    return render_template('index.html', title = title) 