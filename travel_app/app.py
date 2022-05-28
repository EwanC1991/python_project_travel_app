from flask import Flask, render_template
from controllers.country_controller import countries_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)

if __name__ == '__main__':
    app.run(debug=True)