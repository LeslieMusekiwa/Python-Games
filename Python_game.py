# create a Python 
#take a look at it 
# feed them to increase health
# make them battle and decide for a winner

from random import randint

list_choice = ["rock", "paper", "scissors"]


class player:
    def _init_(self):
        self.choice = 'None'
        self.score = 0
        
        
    def get_input(self, choice, run):
       z = 0
       for x in range(3):
           if choice == list_choice[x]:
                z = 1
        
       if z == 0:
            print("wrong input")
            run = False
            return run
        
       if z == 1:
            print("input accepted")
            self.choice = choice
            return run
    
    def return_choice(self):
        return self.choice
    
    def check(self, computer_choice):
        if self.choice != "None":
            if self.choice == "rock" and computer_choice == "scissors":
                self.score = self.score + 1
            elif self.choice == "rock" and computer_choice == "paper":
                self.score = self.score -1
            if self.choice == "paper" and computer_choice == "rock":
                self.score = self.score +1
            elif self.choice == "paper" and computer_choice == "scissors":
                self.score = self.score -1
            if self.choice == "scissors" and computer_choice == "paper":
                self.score = self.score +1
            elif self.choice == "scissors" and computer_choice == "rock":
                self.score = self.score -1    
    
    def return_score(self):
        return self.score    
    
    

player = player()
    
run = True
while run:
    run = player.get_input(input("enter your choice: "), run)
    if run == True:
        computer_choice = list_choice[randint(0, 2)]
        print(f"the computer choice is {computer_choice}")
        player.check(computer_choice)
    print(player.return_score)
        