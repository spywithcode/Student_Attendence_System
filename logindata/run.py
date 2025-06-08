# This script serves as a login page for the Online Student Attendance System.
    
from flask import Flask, request, jsonify, send_from_directory, render_template_string
import subprocess
import sys
import os
import logging

app = Flask(__name__, static_folder='web', static_url_path='/static')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Serve the login page
@app.route('/', methods=['GET'])
def login_page():
    try:
        # Serve the Login.html file from the web folder
        login_html_path = os.path.join(app.static_folder, 'Login.html')
        with open(login_html_path, 'r', encoding='utf-8') as f:
            login_html = f.read()
        return render_template_string(login_html)
    except Exception as e:
        logging.error(f"Failed to serve login page: {str(e)}")
        return jsonify({"status": "error", "message": "Failed to serve login page"}), 500

# Serve static files (CSS, JS)
@app.route('/<path:filename>')
def static_files(filename):
    try:
        return send_from_directory(app.static_folder, filename)
    except Exception as e:
        logging.error(f"Failed to serve static file: {str(e)}")
        return jsonify({"status": "error", "message": "Failed to serve static file"}), 500

# Handle login POST request
@app.route('/login', methods=['POST'])
def validate_login():
    try:
        data = request.get_json() or request.form
        email = data.get('email')
        password = data.get('password')
        if email == "shalu123@gmail.com" and password == "shalu@123":
            # Launch main.py after successful login with error handling
            try:
                main_py_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main.py'))
                subprocess.Popen([sys.executable, main_py_path])
                return jsonify({"status": "success", "message": "Login successful. Main application launched."})
            except Exception as e:
                logging.error(f"Failed to launch main application: {str(e)}")
                return jsonify({"status": "error", "message": "Login successful but failed to launch main application"}), 500
        else:
            return jsonify({"status": "error", "message": "Invalid email or password"}), 401
    except Exception as e:
        logging.error(f"Failed to validate login: {str(e)}")
        return jsonify({"status": "error", "message": "Failed to validate login"}), 500

if __name__ == '__main__':
    app.run(port=8001,debug=True)