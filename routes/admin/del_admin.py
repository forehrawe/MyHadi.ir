from flask import Blueprint, request, render_template
from routes.admin.check_permission import check_permission
from get_database import get_database
import mysql.connector

del_admin_bp = Blueprint('delAdmin', __name__)

@del_admin_bp.route('/admin_management/del-admin', methods=['POST', 'GET'])
def del_admin():
    result = None

    if not check_permission():
        return render_template('admin/errPerm.html')

    if request.method == 'POST':
        id = request.form.get('id')
        if not id:
            return render_template('admin/del_admin.html', result='Invalid ID.')

        conn = get_database()
        cursor = conn.cursor()

        try:
            # چک کردن وجود ادمین
            cursor.execute('SELECT 1 FROM admins WHERE id = %s', (id,))
            if cursor.fetchone() is None:
                result = 'No admin found with that ID.'
            else:

                cursor.execute('UPDATE accounts SET role = %s WHERE account_id = %s', ('user', id))
                cursor.execute('DELETE FROM admins WHERE id = %s', (id,))

                conn.commit()
                result = 'Successfully Deleted.'

        except mysql.connector.Error as e:
            conn.rollback()
            if e.errno == 1452:
                result = 'Invalid User Data.'
            elif e.errno in (1366, 1265):
                result = 'Invalid Inputs.'
            else:
                result = f'Error {e}'
        finally:
            cursor.close()
            conn.close()

    return render_template('admin/del_admin.html', result=result)
