

class Game:
    count = 0
    def __init__ (self, name, rarityCount, rarities, charCount, cost):
        self.name = name
        self.rarityCount = rarityCount
        self.rarities = rarities
        self.charCount = charCount
        self.cost= cost
    

        

class Rarity:
    def __init__ (self,name, percentage):
        self.name = name
        self.percentage = percentage
