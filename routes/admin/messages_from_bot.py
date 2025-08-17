from flask import request, render_template, redirect, Blueprint
from get_database import get_database
from check_permission import check_permission


telebot_bp = Blueprint('telebot_bp', __name__)


@telebot_bp.route('/admin_management/telebot', methods=['GET','POST'])
def telebot():
    messages = None
    
    if not check_permission:
        return render_template('errPerm.html')
    
    conn = get_database()
    cursor = conn.cursor()
    cursor.execute('select * from telebot_messages')
    messages = cursor.fetchall()
    
    return render_template('messages_from_bot.html', messages=messages)




# create table telebot_messages(
#     id int primary key auto_increment,
#     nickname varchar(40),
#     message varchar(300)
# )