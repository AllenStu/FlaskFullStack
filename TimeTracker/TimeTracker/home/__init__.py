from flask import Blueprint, render_template, jsonify
from TimeTracker.home.model.homeModel import AccountModel
from TimeTracker.home.model.homeService import AccountService

def add_routes(app=None):
    blueprint_home = Blueprint('home', __name__,
                          static_url_path='/home/static',
                          static_folder='./static',
                          template_folder='./templates')

    @blueprint_home.route('/home', methods=['GET'])
    def get():
        # account = jsonify(dict(AccountService.create(account2)))
        account = AccountService().create()
        my_key = str(account.key.urlsafe())
        return render_template('home.html', account=my_key)


    @blueprint_home.route('/home', methods=['POST'])
    def post():
        account = AccountService().create()
        my_key = str(account.key.urlsafe())
        return render_template('home.post.html')


    app.register_blueprint(blueprint_home)
