from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, Required
from ss_sale.models import db,User
from flask_login import current_user



class UserRegisterForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    submit = SubmitField('提交')
    
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        user.role = 10
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username has been existed!')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email has been existed')



class UserEditForm(FlaskForm):
    username = StringField('用户名')
    email = StringField('邮箱')
    password = PasswordField('密码')
    repeat_password = PasswordField('重复密码')
    submit = SubmitField('保存')

    def edit_user(self,user):
        user.username = self.username.data
        user.email = self.email.data

        if self.password.data:
            user.password = self.password.data

        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(0,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('email has not been registered!')
    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('password error!')
