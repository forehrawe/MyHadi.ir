from flask import Blueprint, render_template, request, session, jsonify
from get_database import get_database
import hashlib


changepass_bp = Blueprint('changepass_bp', __name__)

@changepass_bp.route('/profile/change-password', methods=['GET', 'POST'])
def changepassword():
    
    if request.method == 'POST':
    
        cpass = request.form.get('cpass')
        npass = request.form.get('npass')
        conn = get_database()
        cursor = conn.cursor()
        email = session.get('email')
        sql = 'select * from accounts where email = %s limit 1'
        val = (email,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        
        hashed_cpass_in_db = result[2]
        
        cpass_hashed = hashlib.sha256(cpass.encode()).hexdigest()
        
        if not hashed_cpass_in_db == cpass_hashed:
            return jsonify(message='Incorrect Current Password')
        
        npass_hashed = hashlib.sha256(npass.encode()).hexdigest()
        
        sql = 'update accounts set password = %s where email = %s'
        val = (npass_hashed, email)
        
        try:
            cursor.execute(sql, val)
            conn.commit()
            conn.close()
            return jsonify(message='Your Password Updated')
        except:
            conn.close()
            return jsonify(message='Request Failed')
    
    
    
    return render_template('home/changepassword.html')