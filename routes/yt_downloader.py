from flask import Blueprint, render_template, request, jsonify
from pytube import YouTube

ytDownloader_bp = Blueprint('ytDownloader', __name__)

@ytDownloader_bp.route('/yt-downloader', methods=['GET', 'POST'])
def ytdownloader():
    msg = None

    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return jsonify(msg = 'Please provide a URL.')

        try:
            yt = YouTube(url)
            stream = yt.streams.filter(res='144p', progressive=True).first()

            if stream:
                filename = stream.default_filename
                stream.download('static/downloads')
                return jsonify(msg= f'Downloaded. <a href="/static/downloads/{filename}" target="_blank">Click here</a>')
            else:
                return jsonify(msg='No 144p stream found.')
        except Exception as e:
            return jsonify(msg=f'Error: {str(e)}')

    return render_template('home/yt_downloader.html')
