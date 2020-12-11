import random

from logic_algorithms.geometry import GeometrySolutions, Rectangle, Circle, Parallelepiped, Sphere


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

    def task_parser(self):
        
        problem = []

        for task in self.tasks:
            new_task = []
            new_task.append(task.classSpecs['problem'])



            list_of_specs = [spec for spec in task.classSpecs['figure_specs'].keys()]
            temp = []
            for i in range(0,2):

                new_spec = random.choice(list_of_specs)
                if new_spec not in temp:
                    temp.append(new_spec)
                    temp.append(task.classSpecs['figure_specs'][new_spec])

            for item in temp:
                new_task.append(item)
            

            new_task.append('Знайти: ')


            for i in range (len(task.classSpecs['figure_specs'].keys())):
                spec_to_find = random.choice(list_of_specs)
                if spec_to_find not in temp:
                    new_task.append(spec_to_find)
                    new_task.append(task.classSpecs['figure_specs'][spec_to_find])
                    break
                else:
                    pass


            problem.append(tuple(new_task))
            


        return problem


