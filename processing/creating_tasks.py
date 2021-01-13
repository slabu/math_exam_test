import random

from logic_algorithms.geometry import GeometrySolutions, Rectangle, Circle, Parallelepiped, Sphere
from logic_algorithms.algebra import QuadraticEquation, RoundationTasks, AlgebraicProgression
from models.tasks import TaskModel


class CreateTasks():
    
    def __init__(self, count_of_tasks_in_group):
        self.count_of_tasks_in_group = count_of_tasks_in_group

        self.tasks = CreateTasks.instance_creation(self.count_of_tasks_in_group)

    @classmethod
    def instance_creation(cls, count_of_tasks_in_group):
        tasks = []
        for task in range(count_of_tasks_in_group):

            #--------------------------------------------Geometry-----------------------------------------------------

            tasks.append(Rectangle(random.randint(1,20), random.randint(1,20)))
            tasks.append(Circle(random.randint(1,20)))
            tasks.append(Parallelepiped(random.randint(1,20), random.randint(1,20), random.randint(1,20)))
            tasks.append(Sphere(random.randint(1,20), random.randint(1,20)))

            #--------------------------------------------Algebra------------------------------------------------------


        return tasks

    # def task_parser(self):
        
    #     problem = []

    #     for task in self.tasks:
    #         new_task = []
    #         new_task.append(task.classSpecs['problem'])



    #         list_of_specs = [spec for spec in task.classSpecs['figure_specs'].keys()]
    #         temp = []

    #         while len(temp) < 4:
    #             new_spec = random.choice(list_of_specs)
    #             if new_spec not in temp:
    #                 temp.append(new_spec)
    #                 temp.append(task.classSpecs['figure_specs'][new_spec])
            
    #         for item in temp:
    #             new_task.append(item)

    #         new_task.append('Знайти: ')

    #         while len(temp) < 6:
    #             spec_to_find = random.choice(list_of_specs)
    #             if spec_to_find not in temp:
    #                 temp.append(spec_to_find)
    #                 temp.append(task.classSpecs['figure_specs'][spec_to_find])

    #         for item in temp[4:6]:
    #             new_task.append(item)
            
            
            
    #         temp.clear()
    #         temp.append(new_task[-1])

    #         for i in range(3):
    #             temp.append(str(float(new_task[-1]) + float(new_task[-1]) * (random.uniform(-100, 100)/100)))

    #         new_task.append(';'.join(temp))

    #         final_problem = []
    #         final_problem.append(' '.join(new_task[:7]))
            
    #         for item in new_task[7:]:
    #             final_problem.append(item)

            
    #         problem.append(tuple(final_problem))
    #         #problem.append(tuple(new_task))
            


    #     return problem


    def task_parser(self):
        
        problem = []

        for task in self.tasks:
            new_task = []
            new_task.append(task.classSpecs['problem'])



            list_of_specs = [spec for spec in task.classSpecs['figure_specs'].keys()]
            temp = []

            while len(temp) < 4:
                new_spec = random.choice(list_of_specs)
                if new_spec not in temp:
                    temp.append(new_spec)
                    temp.append(task.classSpecs['figure_specs'][new_spec])
            
            for item in temp:
                new_task.append(item)

            new_task.append('Знайти: ')

            while len(temp) < 6:
                spec_to_find = random.choice(list_of_specs)
                if spec_to_find not in temp:
                    temp.append(spec_to_find)
                    temp.append(task.classSpecs['figure_specs'][spec_to_find])

            for item in temp[4:6]:
                new_task.append(item)
            
            temp.clear()
            temp.append(new_task[-1])

            temp[0] = temp[0]

            for i in range(3):
                temp.append(str(round(float(new_task[-1]) + float(new_task[-1]) * (random.uniform(-100, 100)/100), 2)))

            print('TEEEEEEEEEMP----------------------------------------------')
            print(temp)
            random.shuffle(temp)
            new_task.append(temp)

            

            final_problem = []
            final_problem.append(' '.join(new_task[:7]))
            
            

            for item in new_task[7:8]:
                final_problem.append(item)

            for item in new_task[-1]:
                final_problem.append(item)
            
            print(final_problem)
            
            problem.append(tuple(final_problem))
            #problem.append(tuple(new_task))
            


        return problem

    @classmethod
    def output_task_parser(cls, tasks):
        
        parsed_tasks = []

        for task in tasks:
            task_dict = {}
            
            task_dict['task_id'] = task.task_id

            task_dict['task_text'] = task.task_text
            
            task_dict['task_answers'] = [str(round(int(answer), 2)) for answer in task.task_answers.split(';')]
            random.shuffle(task_dict['task_answers'])

            task_dict['correct_answer'] = str(round(int(task.task_correct_answer), 2))

            parsed_tasks.append(task_dict)
        
        return parsed_tasks


    @classmethod
    def results_parser(cls, results_dict):
        list_of_solved_tasks = []

        for key,value in results_dict.items():
            final_results = {}
            task = TaskModel.find_by_id(key)
            
            final_results['task_id'] = key
            final_results['task_text'] = task.task_text
            final_results['task_answer_1'] = task.answer_1
            final_results['task_answer_2'] = task.answer_2
            final_results['task_answer_3'] = task.answer_3
            final_results['task_answer_4'] = task.answer_4
            final_results['task_correct_answer'] = task.task_correct_answer
            final_results['task_chosen_answer'] = value
            
            if final_results['task_correct_answer'] == final_results['task_chosen_answer']:
                final_results['task_mark'] = 1
            else:
                final_results['task_mark'] = 0
            
            list_of_solved_tasks.append(final_results)
        
        return list_of_solved_tasks


class CreateAlgebraTasks():
    
    def __init__(self, count_of_tasks_in_group):
        self.count_of_tasks_in_group = count_of_tasks_in_group

        self.tasks = CreateAlgebraTasks.instance_creation(self.count_of_tasks_in_group)

    @classmethod
    def chose_rank(cls, number):
        
        ranks = {
        'цілих':'0',
        'десятків':'-1',
        'сотень':'-2',
        'тисяч':'-3',
        'десятків тисяч':'-4',
        'сотень тисяч':'-5',
        'десятих':'1',
        'сотих':'2',
        'тисячних':'3',
        'десяткiв тисячних':'4',
        'сотень тисячних':'5'
            }

        avaliable_ranks = [int(len(item)) for item in str(number).split('.')]
        avaliable_ranks[0] = avaliable_ranks[0] * (-1)

        return random.randint(avaliable_ranks[0], avaliable_ranks[1])

    @classmethod
    def instance_creation(cls, count_of_tasks_in_group):
        tasks = []

        
        for task in range(count_of_tasks_in_group):

            #--------------------------------------------Algebra------------------------------------------------------

            #tasks.append(QuadraticEquation(random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)))

            #new_number = round(random.uniform(-10000, 10000), random.randint(-4, 4))

            new_number = 0

            while new_number < 100:
                new_number = round(random.uniform(-10000, 10000), 4)
                print(new_number)

                if new_number < 100:
                    pass
                else:
                    tasks.append(RoundationTasks(new_number, CreateAlgebraTasks.chose_rank(new_number)))
                    break
                    
            

            #tasks.append(RoundationTasks(new_number, CreateAlgebraTasks.chose_rank(new_number)))

            

        return tasks

    def roundation_task_parser(self):
        problem = []

        for task in self.tasks:
            new_problem = {}

            new_problem['task_text'] = task.classSpecs['problem']
            new_problem['task_correct_answer'] = task.rounded_number
            
            task_answers = []
            task_answers.append(new_problem['task_correct_answer'])

            list_of_ranks = []
            list_of_ranks.append(task.roundation_rank)

            while len(list_of_ranks) < 4:
                random_rank = random.randint(-4, 4)

                if random_rank in list_of_ranks:
                    pass
                else:
                    list_of_ranks.append(random_rank)
            
            print(list_of_ranks)

            for rank in list_of_ranks[1:]:
                task_answers.append(round(task.number, rank))    
            

            
            
            random.shuffle(task_answers)
            
            new_problem['answer_1'] = task_answers[0]
            new_problem['answer_2'] = task_answers[1]
            new_problem['answer_3'] = task_answers[2]
            new_problem['answer_4'] = task_answers[3]

            problem.append(new_problem)
        
        return problem




class CreateQuadraticEquationTasks():
    
    def __init__(self, count_of_tasks_in_group):
        self.count_of_tasks_in_group = count_of_tasks_in_group

        self.tasks = CreateQuadraticEquationTasks.instance_creation(self.count_of_tasks_in_group)


    @classmethod
    def instance_creation(cls, count_of_tasks_in_group):
        tasks = []
        for task in range(count_of_tasks_in_group):

            #--------------------------------------------Algebra------------------------------------------------------

            tasks.append(QuadraticEquation(random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)))

        return tasks

    def quadratic_equation_task_parser(self):
        problem = []

        for task in self.tasks:
            new_problem = {}

            new_problem['task_text'] = task.classSpecs['problem']

            task_answers = []

            if hasattr(task, 'root'):

                if task.root != 'Коренiв немає':
                    new_problem['task_correct_answer'] = round(task.root, 2)
                
                    task_answers.append(new_problem['task_correct_answer'])
                    
                    for i in range(3):
                        task_answers.append(str(round(float(task_answers[-1]) + float(task_answers[-1]) * (random.uniform(-100, 100)/100), 2)))

                else:
                    new_problem['task_correct_answer'] = task.root

                    task_answers.append(new_problem['task_correct_answer'])

                    final_roots = []

                    for i in range(3):

                        temp_roots = []

                        for i in range(0, int(random.randint(1, 2))):
                            temp_roots.append(f'x{i+1} = {random.randint(-20, 20)}')

                        if len(temp_roots) != 1:
                            final_roots.append(', '.join(temp_roots))
                        else:
                            final_roots.append(''.join(temp_roots))
                    
                    print(final_roots)
                    for item in range(3):
                        task_answers.append(final_roots[item])



            elif hasattr(task, 'root_1'):
                new_problem['task_correct_answer'] = f'x1 = {round(task.root_1, 2)}; x2 = {round(task.root_2, 2)}'

                task_answers.append(new_problem['task_correct_answer'])

                for i in range(3):
                    task_answers.append(f'x1 = {str(round(float(task.root_1) + float(task.root_1) * (random.uniform(-100, 100)/100), 2))} x2 = {str(round(float(task.root_2) + float(task.root_2) * (random.uniform(-100, 100)/100), 2))}')


            random.shuffle(task_answers)

            new_problem['answer_1'] = task_answers[0]
            new_problem['answer_2'] = task_answers[1]
            new_problem['answer_3'] = task_answers[2]
            new_problem['answer_4'] = task_answers[3]

            problem.append(new_problem)
        
        return problem
        



class CreateArithmeticalProgressionTasks():
    
    def __init__(self, count_of_tasks_in_group):
        self.count_of_tasks_in_group = count_of_tasks_in_group

        self.tasks = CreateArithmeticalProgressionTasks.instance_creation(self.count_of_tasks_in_group)

    @classmethod
    def instance_creation(cls, count_of_tasks_in_group):
        tasks = []
        for task in range(count_of_tasks_in_group):

            #--------------------------------------------Algebra------------------------------------------------------

            #tasks.append(QuadraticEquation(random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)))

            tasks.append(AlgebraicProgression(random.randint(1, 10), random.randint(1, 50), random.randint(2, 1000)))

            

        return tasks

    def arithmetical_progression_task_parser(self):
        problem = []

        for task in self.tasks:
            new_problem = {}

            new_problem['task_text'] = task.classSpecs['problem']
            new_problem['task_correct_answer'] = task.member_to_find
            
            task_answers = []
            task_answers.append(new_problem['task_correct_answer'])

            for i in range(3):
                task_answers.append(str(int(float(task_answers[-1]) + float(task_answers[-1]) * (random.uniform(-100, 100)/100))))
            
            random.shuffle(task_answers)
            
            new_problem['answer_1'] = task_answers[0]
            new_problem['answer_2'] = task_answers[1]
            new_problem['answer_3'] = task_answers[2]
            new_problem['answer_4'] = task_answers[3]

            problem.append(new_problem)
        
        return problem