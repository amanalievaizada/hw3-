class Superhero:
 people = 'people'

 def __init__(self,name,nickname,superpower,
                health_points,catchphrase):
       self.name = name
       self.nickname = nickname
       self.superpower = superpower
       self.health_points = health_points
       self.catchphrase = catchphrase

 def get_name(self):
       return self.name

 def double_health(self):
       self.health_points *= 2

 def __str__(self):
    return f"Nickname:{self.nickname},Superpower:{self.superpower},Health:{self.health_points}"

 def __len__(self):
       return (
       len(self.catchphrase))
hero = Superhero("Iron Man","Toni Stark","Genius",100,"I am Iron Man")


print(hero.get_name())
hero.double_health()
print(hero)
print(len(hero))



class air(Superhero):
    fly = False
    def __double__health(self):
        self.health_point**=2
        self.fly = True

    def true_phrase(self):
        return 'It is a true_phrase'

class earth(Superhero):
    element = 'earth'
    damage = 50
    def double_health(self):
       self.health_points**=2
       self.fly = True
    def true_phrase (self):
        return 'it is a true_phrase'

class space (Superhero):
    location = "space"
    damage = 100

    def double_health(self):
        self.health_points**=2
        self.fly = True

    def true_phrase(self):
        return "it is a true_phrase"

class villain(space):
    people = 'monsters'

    def gen_x(self):
        pass
    def crit(self):
         self.damage**=2

air_obj = air ('Thor','Thor Odinson','thunderstorm',150,'I am Thor,the son of Odin')
earth_obj =  earth ('Hulk','Bruse Banner','streight',200,'I am Hulk')
space_obj = space ('Capitan Marvel','Carol Danvers','powerful',250,'Hiher,further,facter')


print(air_obj)
print(earth_obj)
print(space_obj)
villain_obj=villain('Thanos','Titan','superpower', 500,'I am inevitable')
villain_obj.crit()
print(villain_obj)
