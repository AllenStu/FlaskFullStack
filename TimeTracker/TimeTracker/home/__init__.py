from flask import Blueprint, render_template, redirect

def add_routes(app=None):
    blueprint_home = Blueprint('home', __name__,
                          static_url_path='/home/static',
                          static_folder='./static',
                          template_folder='./templates')

    @blueprint_home.route('/home', methods=['GET'])
    def get():
        # return render_template('home.html')
        return redirect('/')

    @blueprint_home.route('/home', methods=['POST'])
    def post():
        return render_template('home.post.html')

    app.register_blueprint(blueprint_home)
