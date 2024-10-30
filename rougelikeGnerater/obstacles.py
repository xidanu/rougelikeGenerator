import random

class ObstaclesCrete:#创建类
    def __init__(self,types,numer):
        self.type = types
        self.numer = numer

        return None
    
    def create(self):#创建障碍
        types_list = ["rock","crack","fire","poop","sticks","water"]
        self.numer = random.randint(8,18)
        i = random.randint(0,6)
        self.type = types_list[i]
        the_final_obstacles = self.type + self.numer
        print(f"You have added obstacles to your map. The data is {the_final_obstacles}")

        return None