import random
class Mapstructure:

    def __init__(self,floor_numer,room_numer,room_type1,room_type2,room_rank):#定义一个类，进行地图创建
        self.floor_numer = floor_numer#初始化的变量分别有层数，房间数，房间类型，房间难度
        self.room_numer = room_numer
        self.room_type1 = room_type1
        self.room_type2 = room_type2
        self.room_rank = room_rank
        return None
    
    def room_set(self):#创建房间
        room_type1_list = ["long","short","big","very big","narrow"]
        room_type2_list = ["normal room","puzzle room","reward room","shop","normal challenge",
        "boss challenge","sacrifice","boss room","devil room","god room","hiding room"]
        room_rank_list = ["easy","mormal","difficult"]
        i = random.randint(0,5)
        j = random.randint(0,11)
        q = random.randint(0,3)
        self.room_type1 = room_type1_list[i]
        self.room_type2 = room_type2_list[j]
        self.room_rank = room_rank_list[q]
        final_room_style = self.room_type1 + self.room_type2 + self.room_rank
        print(f"You have just created a {final_room_style} room")
        
        return None
        
    def map_set(self):#创建整个地图
        print(f"You have created {self.floor_numer} floors,
        {self.room_numer} rooms,")

        return None

