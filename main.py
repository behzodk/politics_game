import time
import random

choices = [True, False]

class Gamer:
    def __init__(self):
        self.uname = 'default'

class Viking(Gamer):
    def __init__(self):
        super().__init__()
        self.uname = "Viking"
        
    def move(self, starter, loop, request):
        return False

class Dove(Gamer):
    def __init__(self):
        super().__init__()
        self.uname = "The Dove"
        
    def move(self, starter, loop, request):
        return True
    
class Optimist(Gamer):
    def __init__(self):
        super().__init__()
        self.uname = "Optimist"
        
    def move(self, starter, loop, request):
        if starter==True:
            return True
        else:
            return request

class Binary(Gamer):
    def __init__(self):
        super().__init__()
        self.uname = "Binary"
        
    def move(self, starter, loop, request):
        if loop%2==0:
            return True
        return False

class Komil(Gamer):
    def __init__(self):
        super().__init__()
        self.uname = "Komil"
        
    def move(self, starter, loop, request):
        return random.choice(choices)
    
class Game:
    def __init__(self, gamer_1, gamer_2):
        self.gamer_1 = gamer_1
        self.gamer_2 = gamer_2
        self.turn = 1
        self.move = None
        self.last_response_gamer_1 = None
        self.last_response_gamer_2 = None
        self.gamer_1_score=0
        self.gamer_2_score=0

    def start(self, rounds=10):
        for i in range(rounds):
            l_1 = self.last_response_gamer_1
            l_2 = self.last_response_gamer_2
            self.last_response_gamer_1 = self.gamer_1.move(i==0, i, l_2)
            self.last_response_gamer_2 = self.gamer_2.move(i==0, i, l_1)
            if self.last_response_gamer_1 and self.last_response_gamer_2:
                self.gamer_1_score+=3
                self.gamer_2_score+=3
                print("Friendship!")
            if not self.last_response_gamer_1 and self.last_response_gamer_2:
                self.gamer_1_score+=5
                print(f"{self.gamer_1.uname} wins!")
            if self.last_response_gamer_1 and not self.last_response_gamer_2:
                self.gamer_2_score+=5
                print(f"{self.gamer_2.uname} wins!")
            if not self.last_response_gamer_1 and not self.last_response_gamer_2:
                self.gamer_1_score+=1
                self.gamer_2_score+=1
                print("Enemies!")
            print(f"Round {i} ended! Total score: {self.gamer_1.uname} {self.gamer_1_score}:{self.gamer_2_score} {self.gamer_2.uname}")
            time.sleep(1)
        print(f"Game ended! Total score: {self.gamer_1.uname} {self.gamer_1_score}:{self.gamer_2_score} {self.gamer_2.uname}")

viking = Viking()
dove = Dove()
optimist = Optimist()
komil = Komil()
binary = Binary()

game = Game(komil, binary)
game.start()
