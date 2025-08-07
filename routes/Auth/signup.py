from flask import Blueprint, request, render_template, flash, redirect, url_for
import hashlib
import secrets
from routes.admin.check_permission import get_database
import mysql.connector


signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    result = None

    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        lastname = request.form['lastName']

        token = secrets.token_hex(16)


        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        conn = get_database()
        cursor = conn.cursor()
        
        try:
            sql = 'insert into accounts(username, password, email, name, lastname, role, token) values(%s,%s,%s,%s,%s,%s,%s)'
            val = (username, hashed_password, email, name, lastname, 'user', token)
            
            cursor.execute(sql,val)
            conn.commit()
            conn.close()
            result = 'Successfully Signed Up.'
            
            flash('successfully signed up.', 'success')
            return redirect(url_for('signin.signin'))

        
        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:
                result = 'This Username Or Email Exist'
            
            elif e.errno == 2003:
                result = 'Server Connection Error'
        
                
            elif e.errno == 1366:
                result = 'Invalid Values'
                
            
            else:
                result = f'Error: {e}'
                

        
        
        

    return render_template('Auth/SignUp.html', result=result)





