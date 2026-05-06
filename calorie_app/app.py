from flask import Flask, render_template, request, redirect, url_for, session, flash
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = "super_secret_random_key" # Required to use sessions and flash messages

# --- MOCK DATABASE ---
# In a real app, you would use SQLAlchemy and a real database (SQLite, PostgreSQL)
users_db = {
    "admin": "password123",
    "user@example.com": "securepass"
}

# --- GOOGLE OAUTH SETUP ---
oauth = OAuth(app)
google = oauth.register(
    name='google',
    # Replace these with your actual credentials from Google Cloud Console
    client_id=os.environ.get("GOOGLE_CLIENT_ID", "YOUR_GOOGLE_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET", "YOUR_GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

# --- ROUTES ---

@app.route('/')
def login_page():
    # If the user is already logged in, skip the login page
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check against our mock database
    if username in users_db and users_db[username] == password:
        session['user'] = username # Log the user in via session
        return redirect(url_for('dashboard'))
    else:
        flash("Invalid username or password. Please try again.")
        return redirect(url_for('login_page'))

@app.route('/dashboard')
def dashboard():
    # Protect this route: kick unauthenticated users back to login
    if 'user' not in session:
        return redirect(url_for('login_page'))
    
    return render_template('dashboard.html', username=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None) # Remove user from session
    return redirect(url_for('login_page'))

# --- GOOGLE AUTH ROUTES ---

@app.route('/signup/google')
def google_signup():
    # Redirects the user to Google's consent screen
    redirect_uri = url_for('google_auth_callback', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/auth/google/callback')
def google_auth_callback():
    # Google sends the user back here with a token
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token, nonce=None)
    
    # Normally, you'd check if user_info['email'] exists in your DB, 
    # and create a new account if it doesn't. 
    # For now, we'll just log them straight into the session:
    session['user'] = user_info['email']
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    # Run the app
    app.run(debug=True, port=5000)