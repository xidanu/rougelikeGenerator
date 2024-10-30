import random

item_rank = [0,1,2,3,4]
room_location = ["shop","reward","normal","boss","hiding","devil","god"]#此处列表无用只是在提醒你有怎样的道具品质和怎样的房间位置


class TreasureDrop:
    def __init__(self,room_location):
        self.room_location = room_location
        
        return None

    def treasure_rank_judge(self):
            if self.room_location == "shop":
                treasure_rank = random.randint(1,5)
            elif self.room_location == "reward":
                treasure_rank = random.randint(0,5)
            elif self.room_location == "normal":
                treasure_rank = random.randint(0,5)
            elif self.room_location == "boss":
                treasure_rank = random.randint(1,5)
            elif self.room_location == "hiding":
                treasure_rank = random.randint(0,5)
            elif self.room_location == "devil":
                treasure_rank = random.randint(2,5)
            elif self.room_location == "god":
                treasure_rank = random.randint(2,5)
            else:
                treasure_rank = random.randint(0,5)

                return treasure_rank
        
    treasure_rank = treasure_rank_judge()
    
    def item_pick(self,treasure_rank):
            item0_list = [1,2,3,4,5,6,"..."]
            item1_list = [7,8,9,10,"...."]
            item2_list = [11,12,13,14,"....."]
            item3_list = [15,16,17,"."]
            item4_list = [18,19,".."]

            if treasure_rank == 0:
                i = random.randint(0,len(item0_list))
                treasure = item0_list[i]
            elif treasure_rank == 1:
                j = random.randint(0,len(item1_list))
                treasure = item1_list[j]
            elif treasure_rank == 2:
                p = random.randint(0,len(item2_list))
                treasure = item2_list[p]
            elif treasure_rank == 3:
                q = random.randint(0,len(item3_list))
                treasure = item3_list[q]
            elif treasure_rank == 4:
                o = random.randint(0,len(item4_list))
                treasure = item4_list[o]

            return treasure
