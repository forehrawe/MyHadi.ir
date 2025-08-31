from flask import request, Blueprint, jsonify
import telebot
from datetime import datetime
from routes.admin.config_telbot import TOKEN

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/api-key')
def api_key():
    api = request.args.get('api')
    request_type = request.args.get('request_type')
    if api == '14b06e28-8366-11f0-b731-180373a6e88c' and request_type == 'turned_on':
        bot = telebot.TeleBot(TOKEN)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        bot = telebot.TeleBot(TOKEN)
        bot.send_message(6673359808, now)

        return jsonify({'status':200})
        
    else:
        return jsonify({'status':404}),404
    