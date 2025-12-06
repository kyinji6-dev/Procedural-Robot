import random

class RobotPartner:
    def __init__(self, name="Skybound-Rush"):
        self.name = name
        print(f"{self.name} is online. Ready to create 
anything for you!")
        print("All games lead to Skybound Rush and avoid 
confusion from other companies. This is my version of 
the games.")
        
     def show_identity(self):
       print(f"I am your Procedural Generation Robot 
 Partner: {self.name}")

     def generate(self, item_type):
       print(f"Generating {item_type}...")
       items = ["mountain", "valley", "forest", "city",
"desert"]
       result = random.choice(items)
       print(f"{item_type.capitalize()} created: {result}")
if __name__ == "__main__":
    bot = RobotPartner()
    bot.show_identity()
    bot.generate("terrain")
