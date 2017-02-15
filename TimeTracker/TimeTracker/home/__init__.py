from flask import Blueprint, render_template

def add_routes(app=None):
    blueprint_home = Blueprint('home', __name__,
                          static_url_path='/home/static',
                          static_folder='./static',
                          template_folder='./templates')

    @blueprint_home.route('/home')
    def home():
        return render_template('home.html')

    app.register_blueprint(blueprint_home)
