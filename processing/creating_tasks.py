import random

from logic_algorithms.geometry import GeometrySolutions, Rectangle, Circle, Parallelepiped, Sphere
from models.tasks import TaskModel


class CreateTasks():
    
    def __init__(self, count_of_tasks_in_group):
        self.count_of_tasks_in_group = count_of_tasks_in_group

        self.tasks = CreateTasks.instance_creation(self.count_of_tasks_in_group)

    @classmethod
    def instance_creation(cls, count_of_tasks_in_group):
        tasks = []
        for task in range(count_of_tasks_in_group):
            tasks.append(Rectangle(random.randint(1,20), random.randint(1,20)))
            tasks.append(Circle(random.randint(1,20)))
            tasks.append(Parallelepiped(random.randint(1,20), random.randint(1,20), random.randint(1,20)))
            tasks.append(Sphere(random.randint(1,20), random.randint(1,20)))
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

            for i in range(3):
                temp.append(str(float(new_task[-1]) + float(new_task[-1]) * (random.uniform(-100, 100)/100)))

            
            random.shuffle(temp)
            new_task.append(temp)

            final_problem = []
            final_problem.append(' '.join(new_task[:7]))
            
            for item in new_task[7:8]:
                final_problem.append(item)

            for item in new_task[-1]:
                final_problem.append(item)
            
            
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
            
            task_dict['task_answers'] = [answer for answer in task.task_answers.split(';')]
            random.shuffle(task_dict['task_answers'])

            task_dict['correct_answer'] = task.task_correct_answer

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

