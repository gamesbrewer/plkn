from flask import Flask
import settings
from werkzeug import SharedDataMiddleware

UPLOAD_FOLDER = 'C:\\0gamesbrewer\\0plkn\\plkn\\upload'
PRINT_FOLDER = 'C:\\0gamesbrewer\\0plkn\\plkn\\printer'

application = Flask(__name__)
application.config.from_object('settings')
#application.config.from_object('plkn.settings')
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['PRINT_FOLDER'] = PRINT_FOLDER

application.add_url_rule('/uploads/<filename>', 'uploaded_file', build_only=True)
application.add_url_rule('/prints/<filename>', 'printed_file', build_only=True)
application.wsgi_app = SharedDataMiddleware(application.wsgi_app, {'/uploads':  application.config['UPLOAD_FOLDER'], '/prints':  application.config['PRINT_FOLDER']})

import views
application.register_blueprint(views.general)
application.register_blueprint(views.webservice)

if __name__ == '__main__':
    application.debug = True
    application.run(host = '0.0.0.0')