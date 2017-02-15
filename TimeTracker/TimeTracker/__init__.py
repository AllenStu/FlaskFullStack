from flask import Flask, render_template
import admin
import home

# to specify the directory of static and template folder
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
