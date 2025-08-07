from flask import Blueprint, render_template, request
from routes.admin.check_permission import get_database, check_permission
import mysql.connector

add_new_admin_bp = Blueprint('NewAdminBP', __name__)



    
@add_new_admin_bp.route('/admin_management/add-admin', methods=['GET', 'POST'])
def add_admin():
    
    result = None
    
    if not check_permission():
        return render_template('admin/errPerm.html')
    
    if request.method == 'POST':
        
        email = request.form['email']
        acc_id = request.form['acc_id']
        token = request.form['token']
        
        conn = get_database()
        cursor = conn.cursor()
        
        sql = 'insert into admins(acc_id, email, token) values (%s,%s,%s)'
        val = (acc_id, email, token)

        sqlrole = 'update accounts set role = %s where account_id = %s'
        valrole = ('admin', acc_id)

        try:
            cursor.execute(sql, val)
            cursor.execute(sqlrole, valrole)
            conn.commit()
            result = 'Successfully Added.'
        except mysql.connector.Error as e:
            if e.errno == 1452:
                result = 'Invalid User Data.'
                
            elif e.errno == 1366:
                result = 'Invalid Inputs.'
                
            elif e.errno == 1265:
                result = 'Invalid Inputs.'

            else:
                result = f'Unknown Error : {e}'
            
        
    
    
    
    return render_template('admin/add_admin.html', result=result)
    
    
    
