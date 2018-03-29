from flask import Blueprint, render_template,redirect,url_for, request,current_app,flash
from ss_sale.models import User,Server
from flask_login import login_user, logout_user, login_required,current_user
from ss_sale.forms import LoginForm, UserRegisterForm, UserEditForm
import pymongo


front = Blueprint('front',__name__)


@front.route('/')
def index():
    return render_template('front/index.html')


@front.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        if current_user.is_admin:
            return redirect(url_for('admin.server_list'))
        else:
            return redirect(url_for('front.index'))
    return render_template('login.html',form=form)


@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out!','success')
    return redirect(url_for('.index'))

@front.route('/register',methods=['GET','POST'])
def userregister():
    form = UserRegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！','success')
        return redirect(url_for('.login'))
    return render_template('register.html',form=form)


@front.route('/freeserver')
def free_server():
    if current_user.is_authenticated:
        return render_template('front/free_server.html')
    else:
        flash('您还未注册,请注册后领免费代理!')
        return redirect(url_for('front.userregister'))


@front.route('/platform')
def get_platform():
    connection = pymongo.MongoClient('127.0.0.1')
    tdb = connection.alpha87
    post = tdb.test
    datas = post.find()
    return render_template('front/platform.html',datas=datas)
