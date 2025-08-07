from flask import render_template, Blueprint
from routes.admin.check_permission import get_database


posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/posts')
def post():
    
    conn = get_database()
    cursor = conn.cursor()
    sql = 'select * from posts'
    cursor.execute(sql)
    posts = cursor.fetchall()

    return render_template('posts/posts.html', posts=posts)



# create table posts(
#     id int PRIMARY KEY AUTO_INCREMENT, 
#     author_acc_email varchar(35),
#     post_title varchar(30),
#     post_author varchar(20),
#     post_body varchar(1000)
#     FOREIGN KEY (author_acc_email) REFERENCES accounts(email)
#     )

