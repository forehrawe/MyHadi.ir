import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from __init__ import create_app

try:
    application = create_app()
except Exception as e:
    with open('/home/cp63888797157/flask_error.txt', 'w') as f:
        f.write(str(e))
    raise
