import random
import os
class Game:
    def __init__(self):
        self.dic = {
            "rock": "🗿", #🗿
            "paper": "📄",  #📄
            "scissor": "✂️",  #✂️
        }
    def user(self):
        print("Type rock for 🗿 \n Type paper for 📄 \n Type scissor for ✂️")
        user_input = input("Enter your choice: ").lower()
        print(user_input)
        print( self.dic[user_input])

    def computer(self):
        finger_type = ["rock", "paper", "scissor"]        
        comp = random.choice(finger_type)
        print(self.dic[comp])
        # print(u'\U0001f604')
    

if __name__ == "__main__":
    os.system("chcp 65001")
    os.system("cls")
    # print(u'\U0001f604')
    obj = Game()
    obj.user()
    comp_res = obj.computer()
    # print(comp_res)