from flask import Blueprint,redirect
bp=Blueprint('user', __name__, url_prefix='/')

CLIENT_SECRETS_FILE='client_secret.json'
SCOPES=['https://www.googleapis.com/auth/drive.metadata.readonly']

@bp.route('/')
def loading():
    #form으로 안넘기고 세션에 정보 넣을 예정
    return render_template('loading.html')

  
@bp.route('/code_success', methods=['POST'])
def hello_code_creation_success():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        print("crud.py", data)
        code_value=data['type']
    return render_template('code_success.html', code_value=code_value)


@bp.route('/authorize')
def authorize():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,scopes=SCOPES
    )
    flow.redirect_uri = flask.url_for('oauth2callback',_external=True)
    authorization_url, state = flow.authorization_url(
      # Enable offline access so that you can refresh an access token without
      # re-prompting the user for permission. Recommended for web server apps.
      access_type='offline',
      # Enable incremental authorization. Recommended as a best practice.
      include_granted_scopes='true')

  # Store the state so the callback can verify the auth server response.
    flask.session['state'] = state

  return flask.redirect(authorization_url)


@bp.route('oauth2callback')
def oauth2callback(): 
    state = sessions['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store credentials in the session.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    credentials = flow.credentials
    flask.session['credentials'] = credentials_to_dict(credentials)
    return flask.redirect(flask.url_for('test_api_request'))