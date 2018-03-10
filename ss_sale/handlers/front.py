from flask import Blueprint, render_template,redirect,url_for, request,current_app
from ss_sale.models import User,Server
from flask_login import login_user, logout_user, login_required,current_user
front = Blueprint('front',__name__)


@front.route('/')
def index():
    return render_template('front/index.html')

