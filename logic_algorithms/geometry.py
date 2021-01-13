from numpy import sqrt, pi

class GeometrySolutions():
    
    @classmethod
    def square_square(cls, square_edge):
        return square_edge**2
    
    @classmethod
    def square_perimeter(cls, square_edge):
        return square_edge*4

    @classmethod
    def square_diagonal(cls, **kwargs):
        if square_edge in kwargs:
            return sqrt((square_edge**2)*2)

        elif square_square in kwargs:
            return sqrt((square_square*2))

    @classmethod
    def cube(cls, **kwargs):
        cube_specs = {'cube_edge': 0, 'cube_side_square': 0, 'cube_surface_square': 0, 'cube_volume': 0, 'cube_side_perimeter': 0}
        if 'cube_edge' in kwargs:
            cube_edge = kwargs['cube_edge']
            cube_specs['cube_edge'] = cube_edge
            cube_specs['cube_side_square'] = cls.square_square(cube_edge)
            cube_specs['cube_surface_square'] = cube_specs['cube_side_square']*6
            cube_specs['cube_volume'] = cube_edge**3
            cube_specs['cube_side_perimeter'] = cls.square_perimeter(cube_edge)
            return cube_specs
    

class Rectangle():
    
    RectangleSpecs = {'rectangle_length': 0, 'rectangle_width': 0, 'rectangle_square': 0, 'rectanlge_diagonal': 0, 'rectangle_perimeter': 0}


    def __init__(self, rectangle_length, rectangle_width):

        self.rectangle_length = rectangle_length
        
        if rectangle_width is None:
            self.rectangle_width = rectangle_length
        else:
            self.rectangle_width = rectangle_width
        
        #created specs

        self.rectangle_square = round(Rectangle.rectangle_square(self.rectangle_length, self.rectangle_width), 1)
        self.rectangle_diagonal = round(Rectangle.rectangle_diagonal(self.rectangle_length, self.rectangle_width), 1)
        self.rectangle_perimeter = Rectangle.rectangle_perimeter(self.rectangle_length, self.rectangle_width)

        self.classSpecs = {
                    'type': 'Geometry',
                    'figure': 'Rectangle',
                    'problem': 'Дано прямокутник з наступними характеристиками:',
                    'figure_specs': 
                                    {
                                        'довжина': str(round(self.rectangle_length, 2)),
                                        'ширина': str(round(self.rectangle_width, 2)),
                                        'площа': str(round(self.rectangle_square, 2)),
                                        'діагональ': str(round(self.rectangle_diagonal, 2)),
                                        'периметр': str(round(self.rectangle_perimeter, 2))
                    }
                }


    @classmethod
    def rectangle_square(cls, rectangle_length, rectangle_width):
        return rectangle_length*rectangle_width

    @classmethod
    def rectangle_diagonal(cls, rectangle_length, rectangle_width):
        return sqrt(rectangle_length**2 + rectangle_width**2)

    @classmethod
    def rectangle_perimeter(cls, rectangle_length, rectangle_width):
        return (rectangle_width + rectangle_length)*2


class Circle():
    def __init__(self, circle_radius):
        self.circle_radius = circle_radius
        
        #created specs

        self.circle_square = Circle.circle_square(self.circle_radius)
        self.circle_length = Circle.circle_length(self.circle_radius)

        self.classSpecs = {
                    'type': 'Geometry',
                    'figure': 'Circle',
                    'problem': 'Дано коло з наступними характеристиками:',
                    'figure_specs': 
                                    {
                                        'радіус кола': str(round(self.circle_radius, 2)),
                                        'площа кола': str(round(self.circle_square, 2)),
                                        'довжина кола': str(round(self.circle_length, 2))
                    }
                }


    @classmethod
    def circle_square(cls, circle_radius):
        return pi*(circle_radius**2)

    @classmethod
    def circle_length(cls, circle_radius):
        return 2*pi*circle_radius


class Ellipse():
    def __init__(self, ellipse_horizontal_half_axis, ellipse_vertical_half_axis):
        self.horizontal_half_axis = horizontal_half_axis
        self.vertical_half_axis = vertical_half_axis

        #created specs

        self.classSpecs = {
                    'type': 'Geometry',
                    'figure': 'Ellipse',
                    'problem': 'Дано Еліпс з наступними характеристиками:',
                    'figure_specs': 
                                    {
                                        'ellipse_horizontal_half_axis': str(round(self.horizontal_half_axis, 2)),
                                        'ellipse_vertical_half_axis': str(round(self.vertical_half_axis, 2))
                    }
                }

##########################################---3D---##########################################

class Parallelepiped():

    parallelepiped_squares = {}
    parallelepiped_diagonals = {}

    def __init__(self, parallelepiped_length, parallelepiped_width, parallelepiped_height):
        self.parallelepiped_length = parallelepiped_length
        self.parallelepiped_width = parallelepiped_width
        self.parallelepiped_height = parallelepiped_height

        #created specs

        parallelepiped_squares = Parallelepiped.parallelepiped_sides_squares(self.parallelepiped_length, self.parallelepiped_width, self.parallelepiped_height)
        parallelepiped_diagonals = Parallelepiped.parallelepiped_sides_diagonals(self.parallelepiped_length, self.parallelepiped_width, self.parallelepiped_height)

        self.parallelepiped_top_side_square = parallelepiped_squares['parallelepiped_top_side_square']
        self.parallelepiped_front_side_square = parallelepiped_squares['parallelepiped_front_side_square']
        self.parallelepiped_side_square = parallelepiped_squares['parallelepiped_side_square']
        self.parallelepiped_top_side_diagonal = parallelepiped_diagonals['parallelepiped_top_side_diagonal']
        self.parallelepiped_front_side_diagonal = parallelepiped_diagonals['parallelepiped_front_side_diagonal']
        self.parallelepiped_side_diagonal = parallelepiped_diagonals['parallelepiped_side_diagonal']
        self.parallelepiped_volume = Parallelepiped.parallelepiped_volume(self.parallelepiped_length, self.parallelepiped_width, self.parallelepiped_height)

        self.classSpecs = {
                    'type': 'Geometry',
                    'figure': 'Parallelepiped',
                    'problem': 'Дано Параллелепіпед з наступними характеристиками:',
                    'figure_specs': 
                                    {
                                        'довжина': str(round(self.parallelepiped_length, 2)),
                                        'ширина': str(round(self.parallelepiped_width, 2)),
                                        'висота': str(round(self.parallelepiped_height, 2)),
                                        'площа верхньої сторони': str(round(int(self.parallelepiped_top_side_square), 2)),
                                        'площа передньої сторони': str(round(int(self.parallelepiped_front_side_square), 2)),
                                        'площа бокової сторони': str(round(int(self.parallelepiped_side_square), 2)),
                                        'діагональ верхньої сторони': str(round(int(self.parallelepiped_top_side_diagonal), 2)),
                                        'діагональ передньої сторони': str(round(int(self.parallelepiped_front_side_diagonal), 2)),
                                        'діагональ бокової сторони': str(round(int(self.parallelepiped_side_diagonal), 2)),
                                        'об\'єм': str(round(int(self.parallelepiped_volume), 2))
                    }
                }

    @classmethod
    def parallelepiped_sides_squares(cls, parallelepiped_length, parallelepiped_width, parallelepiped_height):
        parallelepiped_top_side_square = Rectangle.rectangle_square(parallelepiped_length, parallelepiped_width)
        parallelepiped_front_side_square = Rectangle.rectangle_square(parallelepiped_length, parallelepiped_height)
        parallelepiped_side_square = Rectangle.rectangle_square(parallelepiped_width, parallelepiped_height)

        return {'parallelepiped_top_side_square': str(parallelepiped_top_side_square), 
                'parallelepiped_front_side_square': str(parallelepiped_front_side_square), 
                'parallelepiped_side_square': str(parallelepiped_side_square)}
    
    @classmethod
    def parallelepiped_sides_diagonals(cls, parallelepiped_length, parallelepiped_width, parallelepiped_height):
        parallelepiped_top_side_diagonal = Rectangle.rectangle_diagonal(parallelepiped_length, parallelepiped_width)
        parallelepiped_front_side_diagonal = Rectangle.rectangle_diagonal(parallelepiped_length, parallelepiped_height)
        parallelepiped_side_diagonal = Rectangle.rectangle_diagonal(parallelepiped_width, parallelepiped_height)

        return {'parallelepiped_top_side_diagonal': parallelepiped_top_side_diagonal,
                'parallelepiped_front_side_diagonal': parallelepiped_front_side_diagonal,
                'parallelepiped_side_diagonal': parallelepiped_side_diagonal}

    @classmethod
    def parallelepiped_volume(cls, parallelepiped_length, parallelepiped_width, parallelepiped_height):
        return parallelepiped_length*parallelepiped_width*parallelepiped_height


class Sphere():
    
    def __init__(self, sphere_radius, sphere_segment_height):
        self.sphere_radius = sphere_radius
        self.sphere_segment_height = sphere_segment_height

        #creted specs

        self.sphere_volume = Sphere.sphere_volume(self.sphere_radius)
        self.sphere_surface_square = Sphere.sphere_surface_square(self.sphere_radius)
        self.sphere_segment_surface_square = Sphere.sphere_segment_surface_square(self.sphere_radius, self.sphere_segment_height)
        self.sphere_segment_volume = Sphere.sphere_segment_volume(self.sphere_radius, self.sphere_segment_height)

        self.classSpecs = {
                    'type': 'Geometry',
                    'figure': 'Sphere',
                    'problem': 'Дано Сферу з наступними характеристиками:',
                    'figure_specs': 
                                    {
                                        'радіус сфери': str(round(self.sphere_radius, 2)),
                                        'висота сегменту': str(round(self.sphere_segment_height, 2)),
                                        'об\'єм сфери': str(round(self.sphere_volume, 2)),
                                        'площа поверхні сфери': str(round(self.sphere_surface_square, 2)),
                                        'площа поверхні сегменту сфери': str(round(self.sphere_segment_surface_square, 2)),
                                        'об\'єм сегменту сфери': str(round(self.sphere_segment_volume, 2))
                    }
                }

    @classmethod
    def sphere_volume(cls, sphere_radius):
        return (4/3)*pi*(sphere_radius**3)

        #if diameter included, sphere_volume = (1/6)*pi(sphere_diameter**3)
    
    @classmethod
    def sphere_surface_square(cls, sphere_radius):
        return 4*pi*(sphere_radius**2)

        #if diameter included, sphere_surface_square = pi*(sphere_diameter**2)

    @classmethod
    def sphere_segment_surface_square(cls, sphere_radius, sphere_segment_height):
        return 2*pi*sphere_radius*sphere_segment_height

    @classmethod
    def sphere_segment_volume(cls, sphere_radius, sphere_segment_height):
        return (((sphere_segment_height**2)*pi)/3)*((3*sphere_radius)-sphere_segment_height)

