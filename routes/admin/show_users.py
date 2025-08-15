from flask import request, render_template, Blueprint
from .check_permission import check_permission
from get_database import get_database


show_users_bp = Blueprint('show_users', __name__)


@show_users_bp.route('/admin_management/show_users', methods=['GET', 'POST'])
def showUsers():
    
    result = None

    if not check_permission():
        return render_template('admin/errPerm.html')
    
    if request.method == 'POST':
        
        action = request.form.get('action')
        if action == 'showone':
            email = request.form.get('email')
            conn = get_database()
            cursor = conn.cursor()
            sql = "select * from accounts where email = %s"
            val = (email,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result is None:
                result = ['No Data Available']
            return render_template('admin/show_users_data.html', result=result)
        
        if action == 'showall':
            conn = get_database()
            cursor = conn.cursor()
            sql = 'select * from accounts'
            cursor.execute(sql)
            result = cursor.fetchall()
            if result is None:
                result = ['No Data Available']
            return render_template('admin/show_users_data.html', result=result)

        

    return render_template('admin/show_users.html', result=result)