from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,login_required
from . import auth
from ..models import User,db
from .forms import LoginForm,RegistrationForm
from ..emails import send_email
from flask_login import current_user

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        print("a")
        if user is not None:
            print("b")
            if user.verify_password(form.password.data):
                print("c")
                login_user(user,form.remember_me.data)
                return redirect(request.args.get('next')  or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail(user.email,'Confirm Your Account','auth/email/confirm',usr=user,token=token)
        flash('A confirmation email has been sent to you by email')


        return redirect(url_for('auth.login'))
    return render_template('auth/login.html',form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('you have confirmed your account,Thanks!')
    else:
        flash('the confirmation link is invalid or has expired.')
        return redirect(url_for('main.index'))

@auth.before_app_request
def before_request():
    if current_user.is_authenticated() and not current_user.confirmed and request.endpoint[:5] != 'auth' and request.dendpoint !='static':
        return render_template('auth/unconfirmed.html')
@auth.route('/unconfirmed')
def unconfigred():
    if current_user.is_anonymous() or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.genrate_confirmation_token()
    send_email(current_user.email,'Confirm Your Account','auth/email/confirm',user=current_user,token=token)
    flash('A new confirmation email has been sent to you bu email;')
    return redirect(url_for('main.index'))


