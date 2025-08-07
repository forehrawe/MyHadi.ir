from flask import request, render_template, Blueprint, redirect,session
import mysql.connector
from routes.admin.check_permission import get_database



profile_bp = Blueprint('profile', __name__)


def check_profile():

    conn = get_database()
    cursor = conn.cursor()
    result = None
    token = session.get('token')

    if token:
        sql = 'select * from profile where token = %s'
        val = (token,)
        cursor.execute(sql, val)
        rows = cursor.fetchone()
        if rows:
            result = {
                'phone_number':rows[1],
                'address':rows[2],
                'age':rows[3],
                'nationalcode':rows[4]
            }
        else:
            result = None

        conn.commit()
        conn.close()

    return result
    


@profile_bp.route('/profile', methods=['POST', 'GET'])
def profile():

    token = session.get('token')
    smsg = None

    if not token:
        return render_template('home/errlogin.html')

    if request.method == 'POST':
        
        pnum = request.form.get('phone_number')
        address = request.form.get('address')
        age = request.form.get('age')
        ncode = request.form.get('nationalcode')

        conn = get_database()
        cursor = conn.cursor()

        sqlid = 'select account_id from accounts where token = %s'
        valid = (token,)
        
        cursor.execute(sqlid, valid)
        listedid = cursor.fetchone()
        id = listedid[0]
        
        

        try:        
            sql = 'insert into profile(acc_id, phone_number, address, age, national_code, token) values(%s,%s,%s,%s,%s,%s)'
            val = (id, pnum, address, age, ncode, token)
            cursor.execute(sql,val)
            conn.commit()
            conn.close()
            return redirect('/')
        except mysql.connector.Error as e:
            if e.errno == 1062:
                sql = 'update profile set phone_number = %s, address = %s, age = %s, national_code = %s where token = %s'
                val = (pnum, address, age, ncode, token)
                cursor.execute(sql,val)
                conn.commit()
                conn.close()
                smsg = 'Your Data Updated.'

            else:
                smsg = 'Error'

        
        


    
    result = check_profile()

    return render_template('home/profile.html', result=result, smsg=smsg)