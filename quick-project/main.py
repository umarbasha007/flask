from flask import Flask
from routes.post_routes import post_routes
from routes.user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(post_routes)
app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run()
