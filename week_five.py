class Super_Hero:
    def __init__(self, name, abilities):
        self.name = name
        self.abilities = abilities

    def flying(self):
        print("Flying high in the sky!")
    
    def super_strength(self):
        print("Lifting heavy objects with ease!")

class Super_Villain(Super_Hero):
    pass
    
super_man = Super_Hero("superman", ["flying", "super strength"])
print(super_man.name)
print(super_man.abilities)

super_man.flying()
super_man.super_strength()

super_villian = Super_Villain("lex luthor", ["intelligence", "wealth"])
print(super_villian.name)
print(super_villian.abilities)

super_villian.flying()
super_villian.super_strength()
