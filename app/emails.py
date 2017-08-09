from flask_mail import Message 
from threading import Thread

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(to,subject,template,**kwargs):
    msg = Message(app.config['FLASKY_MAIL_SENDER'],+subject,sender=app.config['FLASK_MAIL_SENDER'],recipients=[to])
    msg.html=render_template(template+'.html',**kwargs)
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start() 
    return thr
