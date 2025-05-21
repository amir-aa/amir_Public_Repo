import random
class Character:
    def __init__(self,name,health,attack_power):
        self.name=name
        self.health=health
        self.attack_power=attack_power
        self.is_alive=True
    def attack(self,target):
            damage=random.randint(self.attack_power-5,self.attack_power)
            target.take_damage(damage)
            print(f"{self.name} damaged {target.name} ::{damage}")
    def take_damage(self,damage):
            self.health-=damage
            if self.health <=0:
                self.health=0
                self.is_alive=False
                print(f"{self.name} Failed and Died!")
    def display_status(self):
            print(f"{self.name}:: Health:{self.health} AttackPower: {self.attack_power}")

class Warrior(Character):
    def __init__(self,name):
        super().__init__(name, health=100,attack_power=30)
        self.special_attack_power=40
        self.special_attack_charges=3
    def special_attack(self,target):
            if self.special_attack_charges>0:
                damage=random.randint(self.special_attack_power-10,self.special_attack_power)
                target.take_damage(damage)
                self.special_attack_charges-=1
                print(f"Warrior used Special Attack made damage to {target.name} : {damage}")
            else:
                print("You can not use special power anymore")
                self.attack(target)

class Enemy(Character):
    def __init__(self,name,health,attack_power):
        super().__init__(name,health,attack_power)
    def random_action(self,target):
        choice=random.randint(1,3)# ما در نظر گرفتیم انتخاب 1 افزودن جان(سلامت)است
        if choice==1:
            self.heal()
        else:
            self.attack(target)
        
    def heal(self):
        heal_amount=random.randint(10,30)
        self.health+=heal_amount
        print(f"{self.name} cured himself +{heal_amount}")


class Game():
    def __init__(self):
        self.player=None
        self.enemies=[]
        self.level=1
    def create_player(self):
        name=input("please enter the Warior name? \t")
        self.player=Warrior(name)
        print(f"{name} Ready to fight!!!")
    def generate_enemies(self):
        enemy_type=[("Wolf",20,15)
                        ,("Shadow",30,10),
                        ("ORC",35,10)]
        num_enemies=random.randint(self.level,self.level+3)
        for item in range(num_enemies):
            enemyname,enemyhealth,enemyattack= random.choice(enemy_type)
            self.enemies.append(Enemy(enemyname,enemyhealth,enemyattack))
    def player_turn(self):
        print("__Your Turn__")
        self.player.display_status()
        print(f"Special attack charge: {self.player.special_attack_charges}")
        alive_enemies= [enemy for enemy in self.enemies if enemy.is_alive]
        print([item.__dict__ for item in alive_enemies])
        attacktype= input("Choose attack type: 1.normal attack 2.special attack")
        if attacktype=="1":
            if alive_enemies :
                target = self.choose_target(alive_enemies)
                self.player.attack(target)
            else:
                print("You Won!")
        else:
            if alive_enemies :
                target = self.choose_target(alive_enemies)
                self.player.special_attack(target)
        
    def choose_target(self,enemies):
        choice = input(f"Please Enter a number between 1 to {len(enemies)}")
        return enemies[int(choice)-1]
    def enemies_turn(self):
        print("___This is Enemies turn___")
        alive_enemies= [enemy for enemy in self.enemies if enemy.is_alive]
        for enemy in alive_enemies:
            if self.player.is_alive:
                enemy.random_action(self.player)
            else:
                break
    
    def Check_game_status(self):
        if not self.player.is_alive:
            print("You are defeated! Bye!")
            return False
        alive_enemies= [enemy for enemy in self.enemies if enemy.is_alive]
        if not alive_enemies:
            print(f"You finished LEVEL {self.level}")
            self.level+=1
            return True
        return None
    def Start(self):
        print("START Play Game")
        self.create_player()
        playing=True
        while playing:
            self.generate_enemies()
            print(f"__LEVEL is {self.level}__")
            print(f"YOU ARE Fighting with {len(self.enemies)}")
            for enemy in self.enemies:
                enemy.display_status()
            while True: # for each Level
                self.player_turn()
                status=self.Check_game_status()
                if status is not None :
                    if status is False:
                        return
                    break 
                self.enemies_turn()
                status=self.Check_game_status()
                if status is not None :
                    if status is False:
                        return
                    break

                # heal for next level
            self.player.health=100
            self.player.special_attack_charges=3
            print("YOUR health is 100 again...")

            
    
g=Game()
g.Start()
