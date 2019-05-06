from flask import render_template
import connexion

# Create the application instance:
# app = Flask(__name__, template_folder='templates')
app = connexion.App(__name__, specification_dir="./")

# Read the swagger.yml to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function responds to the browser URL localhost:5000/

    :return: The rendered template "home.html"
    """
    return render_template('home.html')


# If we're running in stand alone mode, run the application
if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

# To start the server: run, python server.py
