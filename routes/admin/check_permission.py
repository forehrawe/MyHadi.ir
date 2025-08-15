from flask import session
from get_database import get_database

def check_permission():
    token = session.get('token')
    email = session.get('email')
    
    result = False
    
    if token and email:
        conn = get_database()
        cursor = conn.cursor()
        sql = 'select token from admins where email = %s'
        cursor.execute(sql, (email,))
        select_result = cursor.fetchone()
        

        if select_result and select_result[0] == token:
            result = True
            
        else:
            result = False

    else:
        result = False
        
    return result