from flask import Blueprint, render_template, request, redirect, session, jsonify
import hashlib
from get_database import get_database
from email_utils.sender import send_email
import random
from datetime import datetime, timedelta, timezone



signin_bp = Blueprint('signin', __name__)


@signin_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    session.permanent = True
    
    testResult = session.get('email')
    if testResult:
        return redirect('/')

    if request.method == 'POST':
        conn = get_database()
        cursor = conn.cursor()

        operation = request.form.get('operation')

        if operation == 'sendcode':
            email = request.form.get('email')
            characters = list("ABCDEFGHIJKLMNOPQRSXYZabcdefghijklmnopqrstuvwxyz0123456789")
            verification_code = ''.join(random.choices(characters, k=7))
            hashed_verification_code = hashlib.sha256(verification_code.encode()).hexdigest()

            try:
                message_body = f"""
                <div style="font-family: Arial, sans-serif; padding: 20px; background-color: #f7f7f7;">
                    <div style="max-width: 400px; margin: auto; background-color: #ffffff; padding: 30px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                        <h2 style="color: #333;">Verify</h2>
                        <p style="font-size: 16px; color: #555;">Your Verify Code Is: </p>
                        <div style="text-align: center; margin: 20px 0;">
                            <span style="display: inline-block; padding: 12px 24px; font-size: 24px; color: white; background-color: #4CAF50; border-radius: 6px;">
                                {verification_code}
                            </span>
                        </div>
                        
                    </div>
                </div>
                """
                
                send_email(email, 'Verify', message_body)

                session['verification_code'] = hashed_verification_code
                session['expire_time'] = (datetime.now(timezone.utc) + timedelta(minutes=1)).timestamp()

                return jsonify(message='Sent.')

            except:
                return jsonify(message='Error While Sending Code.')

        elif operation == 'login':
            expire = session.get('expire_time')
            in_session_code = session.get('verification_code')

            now_ts = datetime.now(timezone.utc).timestamp()

            if expire and now_ts > expire:
                session.pop('verification_code', None)
                session.pop('expire_time', None)
                return jsonify(message='Verification Code Expired.')

            entered_verify_code = request.form.get('vcode')
            if not entered_verify_code:
                return jsonify(message='Verification Code is required.')

            hashed_entered_code = hashlib.sha256(entered_verify_code.encode()).hexdigest()

            if in_session_code and in_session_code == hashed_entered_code:
                email = request.form.get('email')
                cursor.execute("SELECT email, password, role, token FROM accounts WHERE email = %s", (email,))
                userData = cursor.fetchone()

                password = request.form.get('password')
                hashed_entered_password = hashlib.sha256(password.encode()).hexdigest()

                if userData:
                    if userData[1] == hashed_entered_password:
                        session['token'] = userData[3]
                        session['email'] = email

                        session.pop('verification_code', None)
                        session.pop('expire_time', None)

                        return jsonify(message='Successfully Logged In')
                    else:
                        return jsonify(message='Incorrect username or password')
                else:
                    return jsonify(message='Incorrect user or password')
            else:
                return jsonify(message='Incorrect Verification Code.')
            

        else:
            return jsonify(message='Invalid operation'), 400

    # GET request
    return render_template('Auth/SignIn.html')




