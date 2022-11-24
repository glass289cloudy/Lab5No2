class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_cords(self, x, y):
        self.__x = x
        self.__y = y

    def get_cords(self):
        return (self.__x, self.__y)

    def __repr__(self):
        return f"({self.__x}, {self.__y})"

class Figure:

    def __init__(self, points = []):
        self.__points = points

    def get_points(self):
        return self.__points

    def __repr__(self):
        pts_strs = list(map(str,self.__points))
        return f"Points: {pts_strs}".replace('[',']').replace("]","'").replace("'","")