from flask import render_template, Blueprint, request, session, jsonify

HomePage_bp = Blueprint('home', __name__)


@HomePage_bp.route('/', methods=['POST','GET'])
def homepage():
    if request.method == 'POST':
        operation = request.form.get('operation')
        if operation == 'logout':
            session.clear()
            return jsonify(message='Logged Out.')
    
    return render_template('home/home.html')