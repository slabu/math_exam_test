import random

from flask import Flask, request, redirect, render_template, url_for, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


from models.user import UserModel
from models.tasks import TaskModel
from models.user_progress import ProgressModel

from logic_algorithms.geometry import GeometrySolutions, Rectangle, Circle, Parallelepiped, Sphere
from logic_algorithms.algebra import QuadraticEquation
from processing.creating_tasks import CreateTasks, CreateAlgebraTasks, CreateQuadraticEquationTasks, CreateArithmeticalProgressionTasks


app = Flask(__name__)

app.config['SECRET_KEY'] = 'another_one_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = LoginManager(app)

@manager.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)

#@app.before_first_request
#def create_tables():
#    db.create_all()

    #admin_user = UserModel(user_login='admin', user_password=generate_password_hash('admin'), user_access_level='admin')
    #admin_user.save_to_db()
    #expert_user = UserModel(user_login='expert', user_password=generate_password_hash('expert'), user_access_level='expert')
    #expert_user.save_to_db()


@app.route('/')
def index():

    new_try = QuadraticEquation(5, 3, 7)

    #print(new_try.diskrimenant)
    
    testing_tasks = CreateAlgebraTasks(5)

    
    


    cube_params = GeometrySolutions.cube(cube_edge=5)
    # print(cube_params)
    
    # print("----------------------------------Rectangle-----------------------------------------")
    # rectangle_params = Rectangle(2, 3)
    
    # print("Rectangle width: " + str(rectangle_params.rectangle_width))
    # print("Rectangle length: " + str(rectangle_params.rectangle_length))
    # print("Rectangle perimeter: " + str(rectangle_params.rectangle_perimeter))
    # print("Rectangle diagonal: " + str(rectangle_params.rectangle_diagonal))
    # print("Rectangle square: " + str(rectangle_params.rectangle_square))
    
    # print("----------------------------------Circle--------------------------------------------")
    # circle_params = Circle(5)
    # print("Circle radius: " + str(circle_params.circle_radius))
    # print("Circle length: " + str(circle_params.circle_length))
    # print("Circle square: " + str(circle_params.circle_square))
    
    # print("----------------------------------Parallelepiped------------------------------------")
    # parallelepiped_specs = Parallelepiped(5, 8, 10)
    # print("Parallelepiped length: " + str(parallelepiped_specs.parallelepiped_length))
    # print("Parallelepiped width: " + str(parallelepiped_specs.parallelepiped_width))
    # print("Parallelepiped height: " + str(parallelepiped_specs.parallelepiped_height))
    # print("Parallelepiped top side diagonal: " + str(parallelepiped_specs.parallelepiped_top_side_diagonal))
    # print("Parallelepiped front side diagonal: " + str(parallelepiped_specs.parallelepiped_front_side_diagonal))
    # print("Parallelepiped side diagonal: " + str(parallelepiped_specs.parallelepiped_side_diagonal))
    # print("Parallelepiped top side square: " + str(parallelepiped_specs.parallelepiped_top_side_square))
    # print("Parallelepiped front side square: " + str(parallelepiped_specs.parallelepiped_front_side_square))
    # print("Parallelepiped side square: " + str(parallelepiped_specs.parallelepiped_side_square))
    # print("Parallelepiped volume: " + str(parallelepiped_specs.parallelepiped_volume))


    # print("---------------------------------Sphere----------------------------------------------")
    # sphere_specs = Sphere(10, 2)
    # print("Sphere_radius: " + str(sphere_specs.sphere_radius))
    # print("Sphere_segment_height: " + str(sphere_specs.sphere_segment_height))
    # print("sphere_volume: " + str(sphere_specs.sphere_volume))
    # print("sphere_surface_square: " + str(sphere_specs.sphere_surface_square))
    # print("sphere_segment_surface_square: " + str(sphere_specs.sphere_segment_surface_square))
    # print("sphere_segment_volume: " + str(sphere_specs.sphere_segment_volume))


    print("-----------------------------------Test_creation-------------------------------------------------")

    test_tasks = CreateTasks(5)

    # for task in test_tasks.tasks:
    #     print(task.classSpecs)


    print("-----------------------------------PARSER-------------------------------------------------")

    #print(test_tasks.task_parser())

    #for problem in test_tasks.task_parser():
    #    print(problem)
    #    print(len(problem))
        
        #
        #adding tasks to db
        #  
        #task = TaskModel(*problem, user_id=1)
        #task.save_task_to_db()


    



    return render_template('index.html', cube_params=cube_params, user=UserModel(), validate_user=load_user(current_user.get_id()))


@app.route('/tasks')
def solve_tasks():

    tasks = TaskModel.get_all_tasks()
    
    #new_tasks = CreateTasks.output_task_parser(tasks)

    #print(tasks)

    #print(random.sample(tasks, 20))

    return render_template('solve_tasks.html', tasks=random.sample(tasks, 20), user=UserModel(), validate_user=load_user(current_user.get_id()))


@app.route('/solved_tasks', methods=['POST'])
def solved_tasks():

    answer_dict = {key:value for (key, value) in request.form.items()}

    #print(request.form)
    #print(answer_dict)

    finals = CreateTasks.results_parser(answer_dict)

    #print(finals)

    session['chosen_answers'] = finals

    if request.method == 'POST':
        return redirect(url_for('show_results'))


@app.route('/results')
def show_results():
    
    

    return render_template('results.html', chosen_answers=session['chosen_answers'], user=UserModel(), validate_user=load_user(current_user.get_id()))


@app.route('/user_page', methods=['GET'])
@login_required
def my_actions():
    
    return render_template('my_page.html', user=UserModel(), validate_user=load_user(current_user.get_id()))


@app.route('/save_results_to_db', methods=['POST'])
@login_required
def save_results_to_db():

    input_data = session['chosen_answers']
    date = datetime.now()
    
    for row in input_data:
        #print(row)    
        input_task = ProgressModel(
                                    task_id=row['task_id'],
                                    task_text=row['task_text'],
                                    task_correct_answer=row['task_correct_answer'],
                                    task_answer_1=row['task_answer_1'],
                                    task_answer_2=row['task_answer_2'],
                                    task_answer_3=row['task_answer_3'],
                                    task_answer_4=row['task_answer_4'],
                                    task_chosen_answer=row['task_chosen_answer'],
                                    task_mark=row['task_mark'],
                                    date_of_pass=date, 
                                    user_id=current_user.get_id()
                                )
        input_task.save_to_db()
    
    print('----------------------------------------------------------------------------')
    #print(input_data)

    return redirect(url_for('history'))

@app.route('/tries_history', methods=['GET', 'POST'])
@login_required
def history():

    count_of_tasks = ProgressModel.get_all_statistics(current_user.get_id())

    if request.method == 'GET':

        return render_template('history.html', history=count_of_tasks, user=UserModel(), validate_user=load_user(current_user.get_id()))

    elif request.method == 'POST':

        date_of_solve = request.form.get('important_date')

        return redirect(url_for('user_try', date_of_solve=date_of_solve))
        

@app.route('/user_try_for_<date_of_solve>', methods=['GET', 'POST'])
@login_required
def user_try(date_of_solve):

    date_of_solve = date_of_solve

    tasks = ProgressModel.get_all_tasks_by_user_date(user_id=current_user.get_id(), date_of_pass=date_of_solve)
    
    return render_template('history_user_try.html', user=UserModel(), history_of_user=tasks, date_of_solve=date_of_solve, validate_user=load_user(current_user.get_id()))



def permission_required(permission):
    def decorator(f):
        def decorated_function(*args, **kwargs):
            user = UserModel.find_by_id(current_user.get_id()).user_access_level
            #print(user)
            if user != permission:
                return redirect(url_for('login_page'))
                flash("You have no access!!!")
            else:
                return f(*args, **kwargs)
        return decorated_function
    return decorator


@app.route('/create_tasks', methods=['GET', 'POST'])
@login_required
def create_pull_of_tasks():

    if request.method == 'POST':
        tasks_to_create = request.form.get('count')

        tasks = CreateTasks(int(tasks_to_create))
        roundation_tasks = CreateAlgebraTasks(int(tasks_to_create))
        quadratic_equation_tasks = CreateQuadraticEquationTasks(int(tasks_to_create))
        arithmetical_progression_tasks = CreateArithmeticalProgressionTasks(int(tasks_to_create))

        
        for problem in tasks.task_parser():
        #
        #adding tasks to db
        #  
            #print("PROBLEM-----------------------------")

            #print(problem)

            task = TaskModel(
                                task_text=problem[0], 
                                task_correct_answer=problem[1], 
                                answer_1=problem[2], 
                                answer_2=problem[3],
                                answer_3=problem[4],
                                answer_4=problem[5],
                                user_id=current_user.get_id())
            task.save_task_to_db()
        
        #print(roundation_tasks.roundation_task_parser())
        for problem in roundation_tasks.roundation_task_parser():
            task = TaskModel(   
                                task_text=problem['task_text'], 
                                task_correct_answer=problem['task_correct_answer'], 
                                answer_1=problem['answer_1'],
                                answer_2=problem['answer_2'],
                                answer_3=problem['answer_3'],
                                answer_4=problem['answer_4'],
                                user_id=current_user.get_id()
                                )
            task.save_task_to_db()

        for problem in quadratic_equation_tasks.quadratic_equation_task_parser():
            task = TaskModel(   
                                task_text=problem['task_text'], 
                                task_correct_answer=problem['task_correct_answer'], 
                                answer_1=problem['answer_1'],
                                answer_2=problem['answer_2'],
                                answer_3=problem['answer_3'],
                                answer_4=problem['answer_4'],
                                user_id=current_user.get_id()
                                )
            task.save_task_to_db()

        for problem in arithmetical_progression_tasks.arithmetical_progression_task_parser():
            task = TaskModel(   
                                task_text=problem['task_text'], 
                                task_correct_answer=problem['task_correct_answer'], 
                                answer_1=problem['answer_1'],
                                answer_2=problem['answer_2'],
                                answer_3=problem['answer_3'],
                                answer_4=problem['answer_4'],
                                user_id=current_user.get_id()
                                )
            task.save_task_to_db()

        
        return redirect(url_for('index'))
    
    elif request.method == 'GET':
        if UserModel.find_by_id(current_user.get_id()).user_access_level == 'admin':
            return render_template('create_pull_of_tasks.html', user=UserModel(), validate_user=load_user(current_user.get_id()))
        else:
            return redirect(url_for('index'))
            


@app.route('/add_task', methods=['GET', 'POST'])
def create_new_task():

    if request.method == 'POST':
        
        new_task = request.form

        #print(new_task.keys())

        task_to_add = TaskModel(
                                    task_text=request.form.get('new_task_description'), 
                                    task_correct_answer=request.form.get('new_correct_answer'),
                                    answer_1=request.form.get('new_answer_1'),
                                    answer_2=request.form.get('new_answer_2'),
                                    answer_3=request.form.get('new_answer_3'),
                                    answer_4=request.form.get('new_answer_4'),
                                    user_id=current_user.get_id())
        task_to_add.save_task_to_db()

        return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('create_new_task.html', user=UserModel(), validate_user=load_user(current_user.get_id()))


@app.route('/user_management')
def admin_user_management():

    #new_tasks = TaskModel(task_text='Дано квадратне рiвняння 5x^2 + 8x + 2 = 0. Знайти коренi рiвняння', task_correct_answer='x1 = -1.2 x2 = -0.3', answer_1='x1 = -1.2 x2 = -0.3', answer_2='x1 = 5.3 x2 = -8.1', answer_3='x1 = -2.1 x2 = 3', answer_4='Коренiв немає', user_id=1)
    #new_tasks.save_task_to_db()

    users = UserModel.get_all_users()

    return render_template('admin_user_management.html', users=users, user=UserModel(), validate_user=load_user(current_user.get_id()))


@app.route('/edit_user', methods=['GET', 'POST'])
def admin_edit_user():

    editable_user_id = request.args.get('user_id')

    

    if request.method == 'GET':
        
        user = UserModel.find_by_id(request.args.get('user_id'))




        return render_template('admin_user_edit.html', user_info=user, user=UserModel(), validate_user=load_user(current_user.get_id()))

    elif request.method == 'POST':

    
        print(request.form.get('access_types'))

        print(request.form.get('editable_user_id'))

        user =UserModel.find_by_id(request.form.get('editable_user_id'))

        user.edit_user(request.form.get('access_types'))

        return redirect(url_for('admin_user_management'))
        




@app.route('/delete_user', methods=['POST'])
def admin_delete_user():

    print(request.form.get('delete_user'))
    UserModel.delete_user(request.form.get('delete_user'))

    return redirect(url_for('admin_user_management'))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = UserModel.find_by_login(login)

        if user and check_password_hash(user.user_password, password):
            login_user(user)

            next_page = request.args.get('next')

            if next_page == None:
                return redirect(url_for('index'))
            return redirect(next_page)
        else:
            flash("Login or password is not correct!")
    else:
        flash("Please, fill login and password fields!")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not login or not password or not password2:
            flash("Please, fill all the fields!")
        elif password != password2:
            flash("Passwords are not equal!")
        else:
            hash_pwd = generate_password_hash(password)
            new_user = UserModel(user_login=login, user_password=hash_pwd, user_access_level='simple_user')

            new_user.save_to_db()

            return redirect(url_for('login_page'))
    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)
    return response

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)