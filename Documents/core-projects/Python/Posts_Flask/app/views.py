from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask.globals import request
from flask_login import login_required,current_user
from .models import Post
from . import db




views = Blueprint('views',__name__)

@views.route('/')
# @login_required
def index():
    posts = Post.query.all()

    return render_template('index.html',user = current_user,posts = posts)

@views.route('/create-post',methods = ['GET','POST'])
@login_required
def create_post():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            flash('Post cannot be empty',category='error' )
        elif len(text) < 5:
            flash('Post is too short', category='error')    
        else:
            post = Post(text = text,author =current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created',category='success')  
            return redirect(url_for('views.index'))  

    return render_template('create_post.html',user = current_user)    