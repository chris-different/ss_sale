from flask import Blueprint, render_template,redirect,url_for, request,current_app,flash,jsonify
from ss_sale.models import User,Server
from flask_login import login_user, logout_user, login_required,current_user
from ss_sale.forms import LoginForm, UserRegisterForm, UserEditForm

api = Blueprint('api',__name__,url_prefix='/api')


@api.route('/')
def all():
    return redirect(url_for('front.index'))

@api.route('/server',methods=['GET','POST'])
def server_data():
    list = Server.query.all()
    tmp = []
    for i in list:
        tmp.append(i.to_json())
    return jsonify(tmp)

