from flask import render_template, Blueprint
from routes.admin.check_permission import get_database

HomePage_bp = Blueprint('home', __name__)


@HomePage_bp.route('/', methods=['POST','GET'])
def homepage():
    
    conn = get_database()
    cursor = conn.cursor()
    sql = 'select * from posts'
    cursor.execute(sql)
    posts = cursor.fetchall()
    
    return render_template('home/home.html', posts=posts)