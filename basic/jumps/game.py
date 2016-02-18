import time
from random import randrange

class Game():

    PATH_LENGTH = 10
    TYPE_CHOICES = { 0:"PowerUp", 1:"Normal", 2:"Normal", 3:"Normal", 4:"Punishment"}
    
    def __init__(self):
        self.path = []
        last_type = ''
        for n in range(Game.PATH_LENGTH):
            value = 0
            spot_type = "Normal"
            if not n == 0 and not n == Game.PATH_LENGTH-1:
                if last_type == "Punishment" or last_type == "PowerUp":
                    spot_type = Game.TYPE_CHOICES[randrange(len(Game.TYPE_CHOICES)-1)]
                else:
                    spot_type = Game.TYPE_CHOICES[randrange(len(Game.TYPE_CHOICES))]
                if spot_type == "Punishment":
                    value = randrange(2)+2
                elif spot_type == "PowerUp":
                    value = 1
            last_type = spot_type
            spot = Spot(spot_type, value)
            self.path.append(spot)
        self.position = 0

    def print_path(self):
        path_string = ""
        position_string = ""
        for spot in self.path:
            path_string += Spot.TYPES[spot.spot_type]
        for n in range(Game.PATH_LENGTH):
            if n == self.position:
                position_string += "^"
            else:
                position_string += " "
        print ""
        print path_string
        print position_string
        
    def has_finished(self):
        has_finished = False if self.position < Game.PATH_LENGTH-1 else True
        if has_finished:
            self.position = Game.PATH_LENGTH-1
        return has_finished
        
    def execute_action(self, action):
        if action == "1" or action == "2":
            self.position += int(action)
            if self.position > Game.PATH_LENGTH-1:
                self.position = Game.PATH_LENGTH-1
        else:
            print "Need to select 1 or 2"
        self.check_if_powered()
            
    def check_if_powered(self):
        spot_type = self.path[self.position].spot_type
        value = self.path[self.position].value
        if spot_type == "PowerUp":
            print "Powered Up +"+str(value)
            self.position += value
            self.has_finished()
        elif spot_type == "Punishment":
            print "Powered Down -"+str(value)
            self.position -= value
            if self.position < 0:
                self.position = 0
        if not self.path[self.position].spot_type == "Normal":
            self.print_path()
            self.check_if_powered()
        elif self.has_finished():
            self.print_path()
            

class Spot():

    TYPES = {"Normal":"O", "PowerUp":">", "Punishment":"<"}

    def __init__(self, spot_type, value):
        self.spot_type = spot_type
        self.value = value
    
if __name__ == "__main__":
    game = Game()
    print "Path constructed"
    raw_input("Press a enter to start")
    start = time.time()
    while not game.has_finished():
        game.print_path()
        game.execute_action(raw_input("Jump?"))
    end = time.time()
    print ""
    print "Congratulations!! you have finish the game in: "+str(end - start)+" seconds"