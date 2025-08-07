from flask import request, render_template, Blueprint
from routes.admin.check_permission import get_database, check_permission

show_admin_bp = Blueprint('show_admin', __name__)



@show_admin_bp.route('/admin_management/show_admins', methods=['GET', 'POST'])
def showAdmin():
    result = None
    
    if not check_permission():
        return render_template('admin/errPerm.html')
        
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'showone':
            conn = get_database()
            cursor = conn.cursor()
            email = request.form['email']
            sql = 'select * from admins where email = %s'
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            if result is None:
                result = ['No Data Available']
            return render_template('admin/show_admins_data.html', result=result)
            
        if action == 'showall':
            conn = get_database()
            cursor = conn.cursor()
            sql = 'select * from admins'
            cursor.execute(sql)
            result = cursor.fetchall()
            if result is None:
                result = ['No Data Available']
            return render_template('admin/show_admins_data.html', result=result)

            
            
            
    return render_template('admin/show_admin.html')
            
            