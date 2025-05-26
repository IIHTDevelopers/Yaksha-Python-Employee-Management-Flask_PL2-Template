from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# DB helper
def get_db_connection():
    """
    TODO: Implement database connection function
    - Connect to 'employees.db' database
    - Set row_factory to sqlite3.Row for dictionary-like access
    - Return the connection object
    """
    # TODO: Create connection to employees.db
    # TODO: Set row_factory to sqlite3.Row
    # TODO: Return connection
    return get_db_connection

# 1. Intro to Routes
@app.route('/')
def index():
    """
    TODO: Implement index route
    - Should render 'index.html' template
    - Template should contain welcome message and links to register/login
    """
    # TODO: Render index.html template
    return "index", 500

# 2. Route Methods + Register User
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    TODO: Implement user registration
    GET: Render registration form
    POST: 
    - Get username and password from form
    - Insert new user into users table
    - Redirect to login page after successful registration
    """
    if request.method == 'POST':
        # TODO: Get username and password from request.form
        # TODO: Connect to database
        # TODO: Insert user into users table with username and password
        # TODO: Commit and close connection
        # TODO: Redirect to login page
        return "Registration", 500
    # TODO: Render register.html template for GET request
    return "Register", 500

# 3. Login User
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    TODO: Implement user login
    GET: Render login form
    POST:
    - Get username and password from form
    - Check credentials against users table
    - If valid, store user_id in session and redirect to dashboard
    - If invalid, return error message
    """
    if request.method == 'POST':
        # TODO: Get username and password from request.form
        # TODO: Connect to database
        # TODO: Query users table for matching username and password
        # TODO: If user found, store user_id in session and redirect to dashboard
        # TODO: If user not found, return 'Invalid credentials'
        return "Login ", 500
    # TODO: Render login.html template for GET request
    return "Login ", 500

# 4. Dashboard with Employee List
@app.route('/dashboard')
def dashboard():
    """
    TODO: Implement dashboard route
    - Check if user is logged in (user_id in session)
    - If not logged in, redirect to login
    - If logged in, get all employees from database and render dashboard
    """
    # TODO: Check if 'user_id' is in session
    # TODO: If not in session, redirect to login
    # TODO: Connect to database and get all employees
    # TODO: Render dashboard.html with employees data
    return "Dashboard ", 500

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    """
    TODO: Implement add employee functionality
    - Check if user is logged in
    GET: Render add employee form
    POST: 
    - Get employee data from form (name, salary, age, address)
    - Insert into employees table
    - Redirect to dashboard
    """
    # TODO: Check if user is logged in, redirect to login if not
    if request.method == 'POST':
        # TODO: Get name, salary, age, address from request.form
        # TODO: Connect to database
        # TODO: Insert employee data into employees table
        # TODO: Commit and close connection
        # TODO: Redirect to dashboard
        return "Add employee", 500
    # TODO: Render add_employee.html template
    return "Add employee", 500

# 6. Route Variables & Edit
@app.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    """
    TODO: Implement edit employee functionality
    GET: Get employee by id and render edit form
    POST: Update employee data and redirect to dashboard
    """
    # TODO: Connect to database
    if request.method == 'POST':
        # TODO: Get updated employee data from form
        # TODO: Update employee record in database
        # TODO: Commit and close connection
        # TODO: Redirect to dashboard
        return "Edit employee", 500
    else:
        # TODO: Get employee by id from database
        # TODO: Render edit_employee.html with employee data
        return "Edit employee", 500

@app.route('/api/employee', methods=['POST'])
def add_employee_api():
    """
    TODO: Implement API endpoint to add employee
    - Get JSON data from request
    - Extract name, salary, age, address
    - Insert into employees table
    - Return JSON response with status
    """
    # TODO: Get JSON data from request
    # TODO: Extract name, salary, age, address from JSON
    # TODO: Connect to database
    # TODO: Insert employee data
    # TODO: Commit and close connection
    # TODO: Return JSON response with status and 201 status code
    return jsonify({"status": "e", "message": "Add employee "}), 500

@app.route('/employees', methods=['GET'])
def get_all_employees():
    """
    TODO: Implement API endpoint to get all employees
    - Connect to database and get all employees
    - Format as list of dictionaries with id, name, age, department, salary, address
    - Return JSON response with employees data
    - Handle exceptions and return error response if needed
    """
    try:
        # TODO: Connect to database
        # TODO: Execute SELECT query to get all employees
        # TODO: Format results as list of dictionaries
        # TODO: Return JSON response with success status and employees data
        return jsonify({"status": "e", "message": "Get employees"}), 500
    except Exception as e:
        # TODO: Return JSON error response with 500 status code
        return jsonify({"status": "error", "message": "E"}), 500

# 8. Logout
@app.route('/logout')
def logout():
    """
    TODO: Implement logout functionality
    - Remove user_id from session
    - Redirect to index page
    """
    # TODO: Remove 'user_id' from session
    # TODO: Redirect to index page
    return "Logout", 500

if __name__ == '__main__':
    app.run(debug=True)
