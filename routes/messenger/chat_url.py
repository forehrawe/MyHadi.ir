from flask import render_template, request, session, Blueprint, url_for, redirect
from routes.admin.check_permission import get_database
from datetime import datetime, timezone

chat_url_bp = Blueprint('chat_url_bp', __name__)

@chat_url_bp.route('/messenger/chat/<conv_id>', methods=['GET', 'POST'])
def chat(conv_id):
    token = session.get('token')
    email = session.get('email')

    if not token:
        return render_template('home/errlogin.html')

    conn = get_database()
    cursor = conn.cursor()

    # check access
    check_sql = '''
        SELECT 1 FROM messenger WHERE conversation_id = %s AND (u1_email = %s OR u2_email = %s) LIMIT 1
    '''
    cursor.execute(check_sql, (conv_id, email, email))
    if not cursor.fetchone():
        conn.close()
        return "You don't have access to this conversation.", 403



    if request.method == 'POST':
        
        id_to_del = request.form.get('id')
        
        if id_to_del:
            sql = 'delete from messenger where id = %s'
            val = (id_to_del,)
            cursor.execute(sql,val)
            conn.commit()
            conn.close()


        text = request.form.get('text')

        if not text:
            conn.close()
            return redirect(url_for('chat_url_bp.chat', conv_id=conv_id))

        sql = 'SELECT u1_email, u2_email FROM messenger WHERE conversation_id = %s'
        cursor.execute(sql, (conv_id,))
        result = cursor.fetchall()

        other = None
        for row in result:
            if row[0] == email:
                other = row[1]
            elif row[1] == email:
                other = row[0]


        if not other:
            conn.close()
            return "You are not a participant in this conversation", 403


        date_utc = datetime.now(timezone.utc)
        u1, u2 = sorted([email, other])


        insert_sql = '''
            INSERT INTO messenger (u1_email, u2_email, content, date_time, conversation_id, sender)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''

        try:
            cursor.execute(insert_sql, (u1, u2, text, date_utc, conv_id, email))
            conn.commit()
        except:
            conn.rollback()
            conn.close()
        



    messages_sql = '''
        SELECT id, content, date_time, sender 
        FROM messenger 
        WHERE conversation_id = %s
        ORDER BY date_time ASC
    '''
    cursor.execute(messages_sql, (conv_id,))
    messages = cursor.fetchall()
    conn.close()

    return render_template('messenger/chats.html', messages=messages, conversation_id=conv_id, sender=email)
