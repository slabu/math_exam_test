from flask import Flask, redirect, render_template

from db import db
from logic_algorithms.geometry import GeometrySolutions


app = Flask(__name__)

app.config['SECRET_KEY'] = 'another_one_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
    cube_params = GeometrySolutions.cube(cube_edge=5)
    print(cube_params)
    return render_template('index.html', cube_params=cube_params)






if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)