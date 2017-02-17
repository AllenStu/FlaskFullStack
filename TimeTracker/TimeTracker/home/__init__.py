from flask import Blueprint, render_template, jsonify, request
from TimeTracker.home.model.homeModel import AccountModel
from TimeTracker.home.model.homeService import AccountService


def add_routes(app=None):
    blueprint_home = Blueprint('home', __name__,
                          static_url_path='/home/static',
                          static_folder='./static',
                          template_folder='./templates')

    @blueprint_home.route('/home', methods=['GET'])
    def get():
        return render_template('home.html')


    @blueprint_home.route('/home', methods=['POST'])
    def post():
        account = AccountService().create(request)
        my_key = str(account.key.urlsafe())
        return render_template('home.post.html', account=my_key)

    app.register_blueprint(blueprint_home)
