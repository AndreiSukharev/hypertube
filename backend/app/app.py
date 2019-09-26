from flask import Blueprint, Flask, render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .config import Config, mail_settings
import os

from app.resources.Common.Base import Base
from app.resources.Users.Users import Users
from app.resources.Users.UserId import UserId
from app.resources.Users.Images import Images
from .resources.loginPage.SignUp import SignUp
from .resources.loginPage.SignIn import SignIn
from .resources.loginPage.LogOut import LogOut
from app.resources.Videos.Search import Search
from app.resources.Videos.Watch import Watch


#api
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#app
# template_dir = os.path.abspath('front_test')
# app = Flask(__name__, template_folder=template_dir)
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api_bp, url_prefix='/api')
app.config.update(mail_settings)
CORS(app, resources={r"/*": {"origins": "*"}}, headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)
jwt = JWTManager(app)

# Route
api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(LogOut, '/logout')
api.add_resource(Users, '/users')
api.add_resource(UserId, '/users/<user_id>')
api.add_resource(Images, '/images/<image_id>')
api.add_resource(Search, '/search')
api.add_resource(Watch, '/watch/<movie_id>')



# token revoke
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    sql = "SELECT token FROM token_revokes WHERE token = %s;"
    record = (jti,)
    token = Base.base_get_one(sql, record)
    if not token:
        return False
    return True


@app.route('/')
def index():
    return render_template('index.html')


