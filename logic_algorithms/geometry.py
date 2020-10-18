from numpy import sqrt

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
    