from flask import Blueprint, render_template, jsonify
from TimeTracker.home.model.homeModel import AccountModel

def add_routes(app=None):
    blueprint_home = Blueprint('home', __name__,
                          static_url_path='/home/static',
                          static_folder='./static',
                          template_folder='./templates')

    @blueprint_home.route('/home', methods=['GET'])
    def get():

        # account = HomeService.create_account()
        account = AccountModel()
        account.first_name = 'Juan'
        account.last_name = 'Dela Cruz'
        account.user_id = '1123312'
        account.put()

        account2 = {'first_name':'Maria','last_name':'Dela Cruz','user_id':'123123'}

        accountType = type(account2)

        account = account
        return render_template('home.html', account2=account2, typeX=accountType, account=account)
        # return redirect('/')

    @blueprint_home.route('/home', methods=['POST'])
    def post():
        return render_template('home.post.html')

    app.register_blueprint(blueprint_home)
