import os
from flask import Flask, session, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import psycopg2
import hashlib



app = Flask(__name__)

# ------------------------ Database connection stuff, but no dastabse so commented out to limit bugs for now ------------------------ #

#load_dotenv()


#app.secret_key = os.getenv("SECRET")

#def get_db_connection():
#    conn = psycopg2.connect(
#        host=os.getenv("DB_HOST"),
#        user=os.getenv("DB_USER"),
#        password=os.getenv("DB_PASSWORD"),
#        database=os.getenv("DB_DATABASE")
#    )
#    return conn

@app.route("/")
def home():
    return render_template("search.html")

@app.route("/wordlist")
def wordlist():
    return render_template("wordlist.html")

@app.route("/results")
def results():
    return render_template("results.html")
 
@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        return render_template('search.html')
    #once they search
    elif request.method == "POST":
        search_term = request.form['search_term']
        #results = get_results(search_term)
        #return render_template('results.html', results=results)
        return render_template('results.html')

@app.route("/filters", methods=['GET', 'POST'])
def filters():
    if request.method == "GET":
        return render_template('filters.html')
    #once they search
    elif request.method == "POST":
        search_term = request.form['search_term_1']
        #results = get_results(search_term)
        #return render_template('results.html', results=results)
        return render_template('results.html')

@app.route("/doc")
def doc():
    return render_template("doc.html")

@app.errorhandler(404)
def not_found(e):
    return "Page not found. Please check the URL.", 404

# Decorator used to exempt route from requiring login
def login_exempt(f):
    f.login_exempt = True
    return f

# ------------------------ Login stuff thats commented out for now since no database and I dont want problems ------------------------ #
# @app.route('/login', methods=['GET', 'POST'])
# @login_exempt
# def login():
#     # If user is signed in, redirect them to home
#     if 'userid' in session:
#         return redirect(url_for('home'))
#     # Render page for GET
#     if request.method == "GET":
#         return render_template('login.html')
#     # Handle login logic
#     elif request.method == "POST":
#         username = request.form['username']
#         password = request.form['password']

#         conn = get_db_connection()
#         cursor = conn.cursor()
#         try:
#             # Execute the SQL query to fetch the hashed password associated with the username
#             query = "SELECT passwordhash, salt, userid, emailaddress FROM users WHERE username = %s"
#             cursor.execute(query, (username,))
#             result = cursor.fetchone()
#             cursor.close()
#             conn.close()

#             # If no result found for the given username, return False
#             if not result:
#                 flash(f"Username or password is invalid", 'error')
#                 return render_template("login.html")
            
#             # Extract the salt and hashed password from the result
#             hashed_password_in_db, salt, userid, email = result[:4]

#             # Verify the password
#             if not verify_password(password, salt, hashed_password_in_db):
#                 flash("Username or password is invalid", 'error')
#                 return render_template("login.html")
            
#             # Set user as logged in
#             session["username"] = username
#             session["userid"] = userid
#             session["email"] = email

#             # Render home page
#             return redirect(url_for('home'))

#         # Handle errors
#         except Exception as err:
#             flash(f"Unknown error occured during login.", 'error')
#             return render_template("login.html")
#         finally:
#             conn.close()

# # Helper function to help verify password hash
# def verify_password(password, salt, hashed_password_in_db):
#     # Hash the provided password with the salt
#     hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), 100000)
#     # Compare the hashed passwords
#     return hashed_password.hex() == hashed_password_in_db

# # Log users out
# @app.route('/logout')
# @login_exempt
# def logout():
#     # Remove session variables
#     session.pop('email', None)
#     session.pop('username', None)
#     session.pop('userid', None)
#     return redirect(url_for('login'))

# # Handle user registration
# @app.route('/register', methods=['GET', 'POST'])
# @login_exempt
# def register():
#     # If user is signed in, send them to the index page
#     if 'userid' in session:
#         return redirect(url_for('home'))
#     # If user is trying to view the page, render the page
#     if request.method == "GET":
#         return render_template('register.html')
#     # Handle logic for user registration
#     elif request.method == "POST":
#         # Get form values
#         email = request.form['email']
#         username = request.form['username']
#         password = request.form['password']
#         confirm_password = request.form['confirmpassword']

#         # Confirm that passwords match
#         if password != confirm_password:
#             flash("Password and confirm password do not match", 'error')
#             return render_template("register.html")

#         # Hash the password
#         salt, hashed_password = hash_password(password)
        
#         # Insert
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         try:
#             cursor.execute("INSERT INTO users (emailaddress, username, passwordhash, salt) VALUES (%s, %s, %s, %s) RETURNING userid;", (email, username, hashed_password, salt))
#             conn.commit()
#             result = cursor.fetchone()
#             cursor.close()
#             conn.close()
#             if result == None:
#                 flash(f"Failed to insert user into database.", 'error')
#                 print("Failed to create new user in database.")
#                 return render_template("register.html")
#             session["userid"] = result[0]
#             session["username"] = username
#             session["email"] = email

#             # All done, send user home
#             return redirect(url_for('home'))
#         except Exception as err:
#             flash(f"Registration failed: unknown error occured.", 'error')
#             return render_template("register.html")
#         finally:
#             conn.close()

# # Helper function to hash passwords
# def hash_password(password, salt=None):
#     if salt is None:
#         salt = os.urandom(16)  # Generate a random 16-byte salt
#     else:
#         salt = bytes.fromhex(salt)  # Convert hex string salt back to bytes
    
#     hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
#     return salt.hex(), hashed_password.hex()

# ------------------------ END ROUTES ------------------------ #


if __name__ == "__main__":
    app.run(debug=True)
