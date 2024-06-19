from random import randint

class Knight:
    def __init__(self, knight_name):
        knight_name = knight_name
        with open('DATA/knights.txt') as knights_in:
            for raw_line in knights_in:
                line = raw_line.rstrip()
                name, title, color, quest, comment = line.split(':')
                if name == knight_name:
                    self._name = name
                    self._title = title
                    self._color = color
                    self._quest = quest
                    self._comment = comment

    @property
    def name(self):
        return self._name
    
    @property
    def title(self):
        return self._title
    
    @property
    def color(self):
        return self._color
    
    @property
    def quest(self):
        return self._quest
    
    @property
    def comment(self):
        return self._comment
    
    def joust(self, other_knight):
        winner = self if randint(0,1) else other_knight
        return winner.name