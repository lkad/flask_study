from flask import render_template
from . import auth

@auth.rout('/login')
def login():
    return render_template('auth/login.html')

