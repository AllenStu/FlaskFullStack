from flask import Flask, render_template
import admin
import home

# app = Flask(__name__,
#             template_folder='../templates',
#             static_folder="../static")

app = Flask(__name__)

@app.route("/")
def hello():
    # return 'Hello World'
    message = 'you are doing great so far'
    return render_template('index.html', message=message)

admin.add_routes(app)
home.add_routes(app)


if __name__ == '__main__':
    app.run()

    # go to http://allenbuckley.com/blog/setting-flask-blueprint/ for more useful codes
    # cd TimeTracker
    # cd env
    # source env/bin/activate