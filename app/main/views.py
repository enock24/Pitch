from flask_login import login_required, current_user
from flask import render_template,request,redirect,url_for, abort
from ..models import Pitches,Role,User,Comments
from .. import db,photos
from . import main
from ..email import mail_message
from .forms import PitchForm,CommentForm,UpdateProfile


@main.route('/')
def index():
    '''
    Index page
    return
    '''
    message= "Welcome to Pitch Application!!"
    title= 'Pitch-app!'
    return render_template('index.html', message=message,title=title)


@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # Updated review instance
        new_review = Review(movie_id=movie.id,movie_title=title,image_path=movie.poster,movie_review=review,user=current_user)

        # save review method
        new_review.save_review()
        return redirect(url_for('.movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)