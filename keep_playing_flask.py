# from markupsafe import escape

# from flask import Flask, url_for, request



# app = Flask(__name__)

""" Flask quickstart variable rules"""
# from markupsafe import escape

# from flask import Flask, url_for, request



# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f"User {escape(username)}"

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'Post {post_id}'

# @app.route("/path/<path:subpath>")
# def show_subpath(subpath):
#     return f"Subpath {escape(subpath)}"
""" Routing text quickstart flask  """
# from markupsafe import escape

# from flask import Flask, url_for, request



# @app.route("/projects/")
# def projects():
#     return "The project page"

# @app.route ("/status")
# def status():
#     return "The status page"

""" Quickstart flask test ur building """
# from markupsafe import escape

# from flask import Flask, url_for, request



# @app.route('/')
# def index():
#     return "index"
# @app.route('/login')
# def login():
#     return "login"
# @app.route('/user/<username>')
# def profile(username):
#     return f"{username}\'s profile" 

# with app.test_request_context():
#     print (url_for('index'))
#     print (url_for('login'))
#     print (url_for('login',next='/'))
#     print (url_for('profile' ,username='John Doe'))

""" quickstart http methods """
# from markupsafe import escape

# from flask import Flask, url_for, request



# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         return do_the_login()
#     else: 
#         return show_the_login_form()
    

""" static files """
# url_for("static", filename="style.css")

""" rendering templates"""

from markupsafe import Markup

from flask import render_template, Flask

app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)
