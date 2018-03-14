from flask import Blueprint,render_template,redirect,url_for,flash
from flask_login import current_user

server = Blueprint('server',__name__,url_prefix='/server')

@server.route('/')
def serverlist():
    if current_user.is_authenticated:
        return render_template('front/server.html')
    else:
        flash('您还没有登录，登录后查看免费ss账号')
        return redirect(url_for('front.login'))
