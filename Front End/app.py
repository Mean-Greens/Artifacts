from flask import Flask, render_template, request
from dotenv import load_dotenv



app = Flask(__name__)

load_dotenv()


#app.secret_key = os.getenv("SECRET")

#def get_db_connection():
 #   conn = psycopg2.connect(
  #      host=os.getenv("DB_HOST"),
   #     user=os.getenv("DB_USER"),
    #    password=os.getenv("DB_PASSWORD"),
     #   database=os.getenv("DB_DATABASE")
   # )
    #return conn
@app.route("/")
def home():
    return render_template("search.html")


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

if __name__ == "__main__":
    app.run(debug=True)
