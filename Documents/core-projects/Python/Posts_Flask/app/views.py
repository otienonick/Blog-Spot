from operator import pos
from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_login import login_required,current_user
from .models import  Post,User,Comment
from . import db




views = Blueprint('views',__name__)

@views.route('/')
# @login_required
def index():
    posts = Post.query.all()

    return render_template('index.html',user = current_user,posts = posts)

@views.route('/create_post',methods = ['GET','POST'])
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

@views.route('/delete-post/<id>')
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash('post does not exist!', category='error')
  
    else:    
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted',category='success')

    return redirect(url_for('views.index'))

@views.route('/posts/<username>')
@login_required
def posts(username):
    user = User.query.filter_by(username = username).first()
    if not user:
        flash('No user with that username exists',category='error')
        return redirect(url_for('views.index'))
    posts = user.posts
    return render_template('posts.html',user = current_user,posts = posts,username = username)


@views.route('/create-comment/<post_id>',methods =['POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text')
    if not text:
        flash('Comment cannot be empty.',category='error')
    else: 
        post = Post.query.filter_by(id = post_id)
        if post:
            comment = Comment(text = text, author = current_user.id , post_id = post_id)
            db.session.add(comment)
            db.session.commit()
            flash('comment was added',category='success')

        else:
            flash('Post does not exist',category='error')    
    return redirect(url_for('views.index'))

@views.route('/delete-comment/<comment_id>')   
def  delete_comment(comment_id):
        comment = Comment.query.filter_by(id =comment_id).first()

        if not comment:
            flash('comment does not exist!', category='error')
  
        else:    
            db.session.delete(comment)
            db.session.commit()
            flash('Comment deleted',category='success')

        return redirect(url_for('views.index'))

