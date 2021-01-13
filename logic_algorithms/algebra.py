from numpy import sqrt, power


class QuadraticEquation():
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.type_of_task = 'QuadraticEquation'

        if self.b > 0:
            self.text_b = str(f'+{self.b}')
        else:
            self.text_b = str(f'-{self.b}')

        if self.c > 0:
            self.text_c = str(f'+{self.c}')
        else:
            self.text_c = str(f'-{self.c}')
        

        self.diskrimenant = QuadraticEquation.diskr(self.a, self.b, self.c)

        if type(QuadraticEquation.solves(self.a, self.b, self.c, self.diskrimenant)) is not type([]) :
            self.root = QuadraticEquation.solves(self.a, self.b, self.c, self.diskrimenant)
        else:
            self.root_1 = QuadraticEquation.solves(self.a, self.b, self.c, self.diskrimenant)[0]
            self.root_2 = QuadraticEquation.solves(self.a, self.b, self.c, self.diskrimenant)[1]
        
        self.classSpecs = {
                    'type': 'Algebra',
                    'task': 'QuadraticEquation',
                    'problem': f'Дано квадратне рівняння: {self.a}x^2{self.text_b}x{self.text_c}=0. Знайти корені рівняння.'
                }

        

        

    @classmethod
    def diskr(cls, a, b, c):
        return power(b, 2) - 4*a*c
        
    @classmethod
    def solves(cls, a, b, c, d):
        
        if d < 0:
            return "Коренiв немає"
        
        elif d == 0:
            return (-b)/(2*a)
        
        else:
            roots = []

            roots.append((-b + sqrt(d))/(2*a))
            roots.append((-b - sqrt(d))/(2*a))

            return roots


class RoundationTasks():

    ranks = {
        '0':'цілих',
        '-1':'десятків',
        '-2':'сотень',
        '-3':'тисяч',
        '-4':'десятків тисяч',
        '-5':'сотень тисяч',
        '1':'десятих',
        '2':'сотих',
        '3':'тисячних',
        '4':'десяткiв тисячних',
        '5':'сотень тисячних'
    }
    
    def __init__(self, number, roundation_rank):
        self.number = number
        self.roundation_rank = roundation_rank

        self.text_roundation_rank = RoundationTasks.get_rank(self.roundation_rank)
        
        self.rounded_number = RoundationTasks.roundation_solver(self.number, self.roundation_rank)

        self.classSpecs = {
                    'type': 'Algebra',
                    'task': 'RoundationTasks',
                    'problem': f'Дано число {self.number} яке необхідно округлити до {self.text_roundation_rank}'
                }
        

    @classmethod
    def roundation_solver(cls, number, roundation_rank):
        return round(number, roundation_rank)

    @classmethod
    def count_of_signs(cls, number):
        list_of_signs = str(number).split('.')
        return [int(len(item)) for item in list_of_signs]

    @classmethod
    def get_rank(cls, rank):
        return cls.ranks[str(rank)]
        

class AlgebraicProgression():
    
    def __init__(self, first_member, step, index_of_member_to_find):
        self.first_member = first_member
        self.step = step
        self.index_of_member_to_find = index_of_member_to_find

        self.member_to_find = AlgebraicProgression.get_progression_member_by_number(self.first_member, self.step, self.index_of_member_to_find)

        self.classSpecs = {
                    'type': 'Algebra',
                    'task': 'AlgebraicProgression',
                    'problem': f'Дано арифметичну прогресiю з наступними характеристиками: перший член прогресiї = {self.first_member}, крок прогресiї = {self.step}. Знайти {self.index_of_member_to_find}-й член арифметичної прогресiї' 
                }

    
    @classmethod
    def get_progression_member_by_number(cls, first_member, step, needed_member_number):
        return first_member + step * (needed_member_number - 1)

    