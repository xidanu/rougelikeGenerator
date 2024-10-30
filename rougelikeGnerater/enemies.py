import random
class EnemyCreate:
    def __init__(self,enemy_name,enemy_appearance,enemy_hp,enemy_move_logic,#这里是初始化敌人和boss的属性
                enemy_beated_rewward,enemy_special_ability,boss_name,boss_hp,
                boss_ability,boss_rank):
        self.enemy_name = enemy_name        
        self.enemy_appearance = enemy_appearance
        self.enemy_hp = enemy_hp
        self.enemy_move_logic = enemy_move_logic
        self.enemy_beated_reward = enemy_beated_rewward
        self.enemy_special_ability = enemy_special_ability
        self.boss_name = boss_name
        self.boss_hp = boss_hp
        self.boss_ability = boss_ability
        self.boss_rank = boss_rank
        
        return None
        
    def enemy_create(self):#创建敌人的函数
        reward_list = ["coin","key","card","bomb","stone","none","addit"]
        i = random.randint(0,7)
        reward = reward_list[i]
        self.enemy_beated_reward = reward_list[i]
        enemy_set = {
        "enemy_name" : self.enemy_name,
        "enemy_appearance" : self.enemy_appearance,        
        "enemy_hp" : self.enemy_hp,
        "enemy_move_logic" : self.enemy_move_logic,
        "enemy_beated_reward" : self.enemy_beated_reward,
        "enemy_special_ability" : self.enemy_special_ability
        }
        

        return enemy_set,reward

    def boss_create(self):#创建boss的函数
        q = random.randint(0,3)
        rank_list = ["easy","normal","difficult"]
        self.boss_rank = rank_list[q]
        boss_set = {
        "boss_name" : self.boss_name,
        "boss_hp" : self.boss_hp,
        "boss_ability" : self.boss_ability,
        "boss_rank" : self.boss_rank
        }

        # print(f"You have just created a boss,its data is {boss_set}")

        return boss_set
        