from game_art import LOGO
from game_art import VS
from accounts import accounts
import random
from replit import clear

class HigherLowerGame: 
   
    _should_play = False 
    _score = 0
 
    def __init__(self):

        self._should_pay = True
        self._score = 0

    
    def _assignAccount(self):
        return random.choice(accounts)


    def _resetGameState(self):
        self._should_play = True 
        self._score  = 0 
        clear()
        self._assignAccount()

    def _handleReplayGame(self):
        print("Wrong Answer!")
        print(f"Your final score {self._score}")
        ans = str(input("Do you want to play again ? Type Y if yes otherwise N: "))

        if ans == "Y":
           self._resetGameState()
        else:
           self._should_play = False
           print("Bye, See you again!")
           exit(0)

    def _compareFollower(self,account1, account2, userInput):
        ans = ""

        p1 = account1['followers']
        p2 = account2['followers']
        
        if p1 > p2:
           ans = account1['username'] 
        else:
           ans = account2['username'] 

        
        return ans == userInput
    

    def playGame(self):
        self._resetGameState()

        while self._should_play:
            self._score = 0
            guessing = True 
            while guessing : 
                clear()
                print(LOGO)
                account1  = self._assignAccount()
                account2 = self._assignAccount()

                if self._score > 0:
                   account1  = account2 
                   account2 = self._assignAccount()

                print(f"Username {account1['username']}")
                print(VS)
                print(f"Username {account2['username']}")
                
                print("---------------------------")
                print(f"Current score {self._score}")
                print("---------------------------")
            
                
                guess = str(input("Guess the username of person which high followers: "))

                if self._compareFollower(account1, account2, guess):
                    self._score += 1
                else: 
                    guessing = False

            self._handleReplayGame() 




if __name__ == "__main__":
    app = HigherLowerGame()
    app.playGame()


