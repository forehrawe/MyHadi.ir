from flask import request, Blueprint, Response
import telebot
from datetime import datetime

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/api-key')
def api_key():
    api = request.args.get('api')
    if api == '14b06e28-8366-11f0-b731-180373a6e88c':
        bot = telebot.TeleBot(TOKEN)
        now = datetime.now().strftime('%M/%D %H:%M:%S')
        bot.send_message(12315123, now)
        return Response(status=200)

    else:
        return Response(status=404)
    