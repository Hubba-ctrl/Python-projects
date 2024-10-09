from markupsafe import escape

from flask import Flask, url_for

app = Flask(__name__)

# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f"User {escape(username)}"

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'Post {post_id}'

# @app.route("/path/<path:subpath>")
# def show_subpath(subpath):
#     return f"Subpath {escape(subpath)}"

# @app.route("/projects/")
# def projects():
#     return "The project page"

# @app.route ("/status")
# def status():
#     return "The status page"

@app.route('/')
def sandra():
    return "Sandra Mobaraki är cool. hon är min syster och bror, hon kan ha mördat folk i sin dröm, men det var bara en dröm"

# @app.route('/login')
# def login():
#     return "login"
# @app.route('/user/<username>')
# def profile(username):
#     return f"{username}\'s profile" 



if __name__ == "__main__":
    # with app.test_request_context():
    #     print (url_for('index'))
    #     print (url_for('login'))
    #     print (url_for('login',next='/'))
    #     print (url_for('profile' ,username='John Doe'))
        
        
    
    app.run()