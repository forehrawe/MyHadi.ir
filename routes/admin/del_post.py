from flask import render_template, Blueprint, request
from routes.admin.check_permission import check_permission
from get_database import get_database

del_post_bp = Blueprint('del_post', __name__)


@del_post_bp.route('/admin_management/del-post', methods=['GET','POST'])
def delPost():

    if not check_permission():
        return render_template('admin/errPerm.html')
    
    msg = None
    
    if request.method == 'POST':
        conn = get_database()
        cursor = conn.cursor()
        id = request.form.get('id')
        sql = 'delete from posts where id = %s'
        val = (id,)
        try:
            cursor.execute(sql, val)
            conn.commit()
            conn.close()
            msg = 'Deleted Successfully'
        except:
            msg = 'Error'

    return render_template('admin/del_post.html', msg=msg)