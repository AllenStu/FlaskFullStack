from flask import Flask, render_template, redirect
from google.appengine.api import users
import admin
import home
import logging


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        # jinja
        # message = 'you are doing great so far'
        # return render_template('index.html', message=message)
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(nickname, logout_url)
            return render_template('index.html', message=logout_url,linkText='Sign Out',nickname=nickname)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
            return render_template('index.html', message=login_url,linkText='Sign In')


    @app.errorhandler(404)
    def page_not_found(e):
        return redirect('/')


    @app.errorhandler(500)
    def server_error(e):
        # Log the error and stacktrace.
        logging.exception('An error occurred during a request.')
        return 'An internal error occurred.', 500

    admin.add_routes(app)
    home.add_routes(app)

    return app