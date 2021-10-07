from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
## import resources
from models.post import Post
from resources.post import Posts, PostSingular

app = Flask(__name__)
CORS(app)
api = Api(app)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/weather_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

# Resources
api.add_resource(Posts, '/posts')
api.add_resource(PostSingular, '/posts/<int:post_id>')


if __name__ == '__main__':
    app.run(debug=True)