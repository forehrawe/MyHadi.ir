from flask import render_template, Blueprint, request, session, jsonify

HomePage_bp = Blueprint('home', __name__)


@HomePage_bp.route('/', methods=['POST','GET'])
def homepage():
    
    return render_template('home/home.html')