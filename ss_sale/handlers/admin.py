from flask import Blueprint,render_template
from ss_sale.models import User,db,Server
admin = Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/server',methods=['POST','GET'])
def server_list():
    servers = Server.query.all()
    return render_template('/admin/server_list.html',servers=servers)

@admin.route('/user',methods=['POST','GET'])
def user_list():
    users = User.query.all()
    return render_template('/admin/user_list.html',users=users)
