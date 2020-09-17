import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    full_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(full_path)
    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                sender='soumya.devtest@gmail.com',
                recipients=[user.email])
    msg.body = f''' To reset the password, visit the following link:
{url_for('users.reset_password',token=token, _external=True)}

If you did not make this request, please ignore this email.
'''
    mail.send(msg)

def send_confirmation_email(user):
    token = user.get_reset_token()
    msg = Message('Email Confirmaiton ',
                sender='soumya.devtest@gmail.com',
                recipients=[user.email])
    msg.body = f''' To confirm the email address, please visit the following link:
{url_for('users.confirm_email',token=token, _external=True)}

If you did not make this request, please ignore this email.
'''
    mail.send(msg)