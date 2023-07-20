import random
import os
import asyncio
class Game:
    def __init__(self):
        self.user_count = 0
        self.comp_count = 0
        self.dic = {
            "rock": "🗿", #🗿
            "paper": "📄",  #📄
            "scissor": "✂️",  #✂️
        }
    def user(self):
        print("Type rock for 🗿 \nType paper for 📄 \nType scissor for ✂️")
        user_input = input("Enter your choice: ").lower()
        os.system("cls")
        # print(user_input)
        if user_input not in self.dic:
           return False
        else:
            return user_input

    def computer(self):
        finger_type = ["rock", "paper", "scissor"]        
        comp = random.choice(finger_type)
        return comp
        # print(u'\U0001f604')
    def validation(self):                
        user_choice = self.user()
        comp_choice = self.computer()
        # print(f"User - {self.user_count} Computer - {self.comp_count} ")
        if not user_choice:
            os.system("cls")
            print("Please enter a valid input")            
            self.validation()
        else:            
            print(f"User choice - {self.dic[user_choice]} Computer Choice - {self.dic[comp_choice]}")
            if user_choice == comp_choice:
                pass
            elif user_choice == "rock" and comp_choice == "scissor" or user_choice == "scissor"  and comp_choice == "paper" and user_choice == "paper" and comp_choice == "rock":
                self.user_count += 1
            else:
                self.comp_count += 1
            print(f"User count - {self.user_count} Computer count - {self.comp_count}")
            play_again = input("\n\nDo you want to play again - Type 1 for Yes or 0 for No : ")
            os.system("cls")
            if play_again == '1':
                self.validation()
            else:
                os.system("cls")
                if self.user_count > self.comp_count:
                    print("You Win : ",self.user_count)
                elif self.user_count < self.comp_count:
                    print("Computer Win : ",self.comp_count)
                else:
                    print(f"Tie ---> User : {self.user_count} Computer : {self.comp_count}" )
                
                input("Press any key to exit: ")

            
if __name__ == "__main__":
    os.system("chcp 65001")
    os.system("cls")
    # print(u'\U0001f604')
    obj = Game()
    
    obj.validation()
    # obj.user()
    # comp_res = obj.computer()
    # print(comp_res)