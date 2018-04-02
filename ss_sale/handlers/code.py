from flask import Blueprint, render_template,redirect,url_for, request,current_app,flash,jsonify
from flask_login import login_user, logout_user, login_required,current_user
import json
code = Blueprint('code',__name__,url_prefix='/code')





@code.route('/current_data')
def current_data():
    return render_template('code/current_data.html')


@code.route('/history_data')
def history_data():
    return render_template('/code/history_data.html')
