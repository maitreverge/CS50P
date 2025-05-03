class Vault:
    def __init__(self, gold=0, silver=0, bronze=0):
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
    
    def __str__(self):
        return f"{self.gold} gold coins, {self.silver} silver coins {self.bronze} bronze coins"
    
    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        bronze = self.bronze + other.bronze
        return Vault(gold, silver, bronze)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)