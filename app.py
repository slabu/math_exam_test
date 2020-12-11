from flask import Flask, redirect, render_template

from db import db
from logic_algorithms.geometry import GeometrySolutions, Rectangle, Circle, Parallelepiped, Sphere
from processing.creating_tasks import CreateTasks


app = Flask(__name__)

app.config['SECRET_KEY'] = 'another_one_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
    cube_params = GeometrySolutions.cube(cube_edge=5)
    print(cube_params)
    
    print("----------------------------------Rectangle-----------------------------------------")
    rectangle_params = Rectangle(2, 3)
    
    print("Rectangle width: " + str(rectangle_params.rectangle_width))
    print("Rectangle length: " + str(rectangle_params.rectangle_length))
    print("Rectangle perimeter: " + str(rectangle_params.rectangle_perimeter))
    print("Rectangle diagonal: " + str(rectangle_params.rectangle_diagonal))
    print("Rectangle square: " + str(rectangle_params.rectangle_square))
    
    print("----------------------------------Circle--------------------------------------------")
    circle_params = Circle(5)
    print("Circle radius: " + str(circle_params.circle_radius))
    print("Circle length: " + str(circle_params.circle_length))
    print("Circle square: " + str(circle_params.circle_square))
    
    print("----------------------------------Parallelepiped------------------------------------")
    parallelepiped_specs = Parallelepiped(5, 8, 10)
    print("Parallelepiped length: " + str(parallelepiped_specs.parallelepiped_length))
    print("Parallelepiped width: " + str(parallelepiped_specs.parallelepiped_width))
    print("Parallelepiped height: " + str(parallelepiped_specs.parallelepiped_height))
    print("Parallelepiped top side diagonal: " + str(parallelepiped_specs.parallelepiped_top_side_diagonal))
    print("Parallelepiped front side diagonal: " + str(parallelepiped_specs.parallelepiped_front_side_diagonal))
    print("Parallelepiped side diagonal: " + str(parallelepiped_specs.parallelepiped_side_diagonal))
    print("Parallelepiped top side square: " + str(parallelepiped_specs.parallelepiped_top_side_square))
    print("Parallelepiped front side square: " + str(parallelepiped_specs.parallelepiped_front_side_square))
    print("Parallelepiped side square: " + str(parallelepiped_specs.parallelepiped_side_square))
    print("Parallelepiped volume: " + str(parallelepiped_specs.parallelepiped_volume))


    print("---------------------------------Sphere----------------------------------------------")
    sphere_specs = Sphere(10, 2)
    print("Sphere_radius: " + str(sphere_specs.sphere_radius))
    print("Sphere_segment_height: " + str(sphere_specs.sphere_segment_height))
    print("sphere_volume: " + str(sphere_specs.sphere_volume))
    print("sphere_surface_square: " + str(sphere_specs.sphere_surface_square))
    print("sphere_segment_surface_square: " + str(sphere_specs.sphere_segment_surface_square))
    print("sphere_segment_volume: " + str(sphere_specs.sphere_segment_volume))


    print("-----------------------------------Test_creation-------------------------------------------------")

    test_tasks = CreateTasks(5)

    for task in test_tasks.tasks:
        print(task.classSpecs)


    print("-----------------------------------PARSER-------------------------------------------------")

    print(test_tasks.task_parser())



    return render_template('index.html', cube_params=cube_params)


@app.route('/tasks')
def solve_tasks():
    return render_template('solve_tasks.html')






if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)