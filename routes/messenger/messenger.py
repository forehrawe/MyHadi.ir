from flask import Blueprint, render_template, session, request
from routes.admin.check_permission import get_database
from datetime import datetime, timezone


messegner_bp = Blueprint('messenger' , __name__)


@messegner_bp.route('/messenger')
def messenger():
    
    token = session.get('token')
    email = session.get('email')
    conversations = None

    if not token:
        return render_template('home/errlogin.html')
    
    conn = get_database()
    cursor = conn.cursor()
    
    sql = 'SELECT * FROM messenger WHERE u1_email = %s OR u2_email = %s'
    val = (email, email)
    
    cursor.execute(sql, val)
    result = cursor.fetchall()
    conn.close()
    
    
    
    conversations_dict = {}
    
    if result:
        for row in result:
            conv_id = row[5]
            if conv_id not in conversations_dict:
                if row[1] == email:
                    conversations_dict[conv_id] = row[2]
                else:
                    conversations_dict[conv_id] = row[1]

                
                
        conversations = [{'conversation_id': cid, 'other_user': other} for cid, other in conversations_dict.items()]
    
    

    return render_template('messenger/messenger.html', conversations=conversations)






# create table messenger(
#     id int PRIMARY KEY AUTO_INCREMENT,
#     u1_email varchar(35),
#     u2_email varchar(35),
#     content varchar(500),
#     date_time varchar(15),
#     conversation_id varchar(10),
#     FOREIGN KEY (u1_email) REFERENCES accounts(email),
#     FOREIGN KEY (u2_email) REFERENCES accounts(email)
#     )