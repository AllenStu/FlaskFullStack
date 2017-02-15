from flask import Flask, render_template
import admin
import home
import logging

# to specify the directory of static and template folder
# app = Flask(__name__,
#             template_folder='../templates',
#             static_folder="../static")


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        # return 'Hello World'
        # jinja
        message = 'you are doing great so far'
        return render_template('index.html', message=message)

    @app.errorhandler(500)
    def server_error(e):
        # Log the error and stacktrace.
        logging.exception('An error occurred during a request.')
        return 'An internal error occurred.', 500

    admin.add_routes(app)
    home.add_routes(app)

    # if __name__ == '__main__':
    #     app.run()

    return app