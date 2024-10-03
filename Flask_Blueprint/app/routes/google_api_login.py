from flask import Blueprint, redirect, request, session
from requests_oauthlib import OAuth2Session
from config import Config

login_bp = Blueprint('login', __name__)

GOOGLE_CLIENT_ID = Config.GOOGLE_OAUTH["GOOGLE_CLIENT_ID"]
SCOPE =  Config.GOOGLE_OAUTH["SCOPE"]
REDIRECT_URI =  Config.GOOGLE_OAUTH["REDIRECT_URI"]
AUTH_URI = Config.GOOGLE_OAUTH["AUTH_URI"]
TOKEN_URI = Config.GOOGLE_OAUTH["TOKEN_URI"]
GOOGLE_CLIENT_SECRET = Config.GOOGLE_OAUTH["GOOGLE_CLIENT_SECRET"]

@login_bp.route('/')
def index():
    google = OAuth2Session(GOOGLE_CLIENT_ID, scope=SCOPE, redirect_uri=REDIRECT_URI)
    authorization_url, state = google.authorization_url(AUTH_URI, access_type="offline", prompt="select_account")
    session['oauth_state'] = state
    return redirect(authorization_url)

@login_bp.route('/google_callback')
def callback():
    google = OAuth2Session(GOOGLE_CLIENT_ID, state=session['oauth_state'], redirect_uri=REDIRECT_URI)
    token = google.fetch_token(TOKEN_URI, client_secret=GOOGLE_CLIENT_SECRET, authorization_response=request.url)
    session['oauth_token'] = token
    return 'Autenticación completada.'