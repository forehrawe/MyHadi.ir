from flask import Flask
from datetime import timedelta
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.secret_key = '3v^m#A@1s!kLz8Qp$F##tUb2nWgEoJrYh'
    
    app.permanent_session_lifetime = timedelta(days=30)
    app.config.from_pyfile('config.py')
    mail.init_app(app)


    from routes.Auth.signup import signup_bp
    from routes.Auth.signin import signin_bp
    from routes.admin.admin_management import admin_mgmt_page_bp
    from routes.admin.add_new_admin import add_new_admin_bp
    from routes.admin.del_admin import del_admin_bp
    from routes.admin.show_admins import show_admin_bp
    from routes.home import HomePage_bp
    from routes.admin.show_users import show_users_bp
    from routes.profile import profile_bp
    from routes.posts.registerposts import registerposts_bp
    from routes.admin.del_post import del_post_bp
    from routes.messenger.messenger import messegner_bp
    from routes.messenger.create_conversation import create_conv_messenger_bp
    from routes.messenger.chat_url import chat_url_bp
    from routes.Auth.changepassword import changepass_bp
    from routes.admin.messages_from_bot import telebot_bp


    app.register_blueprint(signin_bp)
    app.register_blueprint(signup_bp)
    app.register_blueprint(admin_mgmt_page_bp)
    app.register_blueprint(add_new_admin_bp)
    app.register_blueprint(del_admin_bp)
    app.register_blueprint(show_admin_bp)
    app.register_blueprint(HomePage_bp)
    app.register_blueprint(show_users_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(registerposts_bp)
    app.register_blueprint(del_post_bp)
    app.register_blueprint(messegner_bp)
    app.register_blueprint(create_conv_messenger_bp)
    app.register_blueprint(chat_url_bp)
    app.register_blueprint(changepass_bp)
    app.register_blueprint(telebot_bp)


    return app
