from flask import Blueprint, render_template, request, session, redirect
from get_database import get_database
from datetime import datetime, timezone
import secrets
import mysql.connector


create_conv_messenger_bp = Blueprint('messenger_creator' , __name__)


@create_conv_messenger_bp.route('/messenger/create-conv', methods=['POST', 'GET'])
def messenger():
    msg = None
    token = session.get('token')

    if not token:
        return render_template('home/errlogin.html')
    
    if request.method == 'POST':

        conn = get_database()
        cursor = conn.cursor()

        u1_email = session.get('email')
        u2_email = request.form.get('email')
        

        if u1_email == u2_email:
            msg = 'You Cant Send Message Your Self.'
            return render_template('messenger/create_conversation.html', msg=msg)
        
        
        
        u1, u2 = sorted([u1_email, u2_email])
        date_utc = datetime.now(timezone.utc)
        
        conv_id = secrets.token_hex(5)
        
        check_sql = 'SELECT * FROM messenger WHERE u1_email = %s AND u2_email = %s LIMIT 1'
        cursor.execute(check_sql, (u1, u2))
        existing = cursor.fetchone()



        if existing:
            msg = 'Conversation Exist.'
            conn.close()
            return render_template('messenger/create_conversation.html', msg=msg)
        
        

        sql = 'insert into messenger(u1_email, u2_email, content, date_time, conversation_id) values(%s,%s,%s,%s,%s)'
        val = (u1, u2, 'Hello', date_utc, conv_id)

        try:
            cursor.execute(sql,val)
            conn.commit()
            conn.close()
            return redirect('/messenger')
        except mysql.connector.Error as e:
            if e.errno == 1452:
                msg = 'This Email Doesnt Exists'
            
            else: 
                msg = 'Error'
                
            conn.rollback()
            conn.close()
    

    return render_template('messenger/create_conversation.html', msg=msg)



