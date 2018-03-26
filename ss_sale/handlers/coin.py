from flask import Blueprint,render_template,redirect,url_for,flash
from flask_login import current_user

coin = Blueprint('coin',__name__,url_prefix='/coin')

@coin.route('/')
def coin_price():
    return render_template('front/coin_price.html')

