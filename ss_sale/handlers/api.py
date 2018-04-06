from flask import Blueprint, render_template,redirect,url_for, request,current_app,flash,jsonify
from ss_sale.models import User,Server
from ss_sale.redis_all import get_data_json
from flask_login import login_user, logout_user, login_required,current_user
from ss_sale.forms import LoginForm, UserRegisterForm, UserEditForm
import redis
import requests
import json
from ss_sale.btc_price import get_btc_price
api = Blueprint('api',__name__,url_prefix='/api')


@api.route('/')
def all():
    return redirect(url_for('front.index'))

@api.route('/apikey')
def apikey():
    if current_user.is_authenticated:
        myid = current_user.get_id()
        user = User.query.filter_by(id=myid).first()
        return render_template('front/apikey.html',apikey=user.apikey)
    else:
        return render_template('front/apikey.html')


@api.route('/server',methods=['GET','POST'])
def server_data():
    list = Server.query.all()
    tmp = []
    for i in list:
        tmp.append(i.to_json())
    return jsonify(tmp)
#外部api接口
@api.route('/coin',methods=['GET','POST'])
def coin_data():
    coin_data = get_data_json()
    coin_data.sort(key=lambda x:x['f_id'])
    return jsonify(coin_data[0:50])

@api.route('/bitcoin',methods=['GET','POST'])
def bitcoin_data():
    data = get_btc_price()
    return json.dumps(data)





#go调用,内部api接口
@api.route('/go_coin',methods=['GET','POST'])
def get_coin():
    r = requests.get('http://127.0.0.1:8080/current_data')
    t = json.loads(r.text)
    return jsonify(t)





