from flask import render_template, Blueprint, request, session
from routes.admin.check_permission import get_database


registerposts_bp = Blueprint('registerposts', __name__)


@registerposts_bp.route('/add-post', methods=['GET', 'POST'])
def createPost():
    
    msg = None
    email = session.get('email')
    

    if request.method == 'POST':
        if email:
            title = request.form.get('titlepost')
            body = request.form.get('bodypost')

            conn = get_database()
            cursor = conn.cursor()

            sql = 'insert into posts(author_acc_email, post_title, post_body) values(%s,%s,%s)'
            val = (email, title, body)

            try:
                cursor.execute(sql, val)
                conn.commit()
                conn.close()
                msg = 'Posted'
            except:
                msg = 'Error'
        
        else:
            return render_template('home/errlogin.html')



    return render_template('posts/registerposts.html', msg=msg)