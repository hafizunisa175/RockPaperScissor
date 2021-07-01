import random
def start():
   n= random.randint(1,3)
   print("Hi Welcome to Rock Paper Scissors...")
   print("This game was build by Hafizunisa")
   print("So the rules are: ")
   print("Type 1 for choosing Rock")
   print("Type 2 for choosing Paper")
   print("Type 3 for choosing Scissors")
   m=int(input("Enter your choice: "))
   if(m==n): 
      print("Opps There is a draw ")
      gameover()
   elif m==1:
      print("Yours: Rock")
      Rock(n)
   elif m==2:
      print("Yours: Paper")
      Paper(n)
   elif m==2:
      print("Yours: Scissors")
      Scissor(n)   
   else:
      print("Dont You know how to read the instructions")
      print("First read the instructions properly and then play!!") 
      gameover()


def gameover():
   print("Do you wanna play the game? Y/N: ")
   ch=input(">").upper()
   if(ch=='Y'): start()
   else: exit()

def Rock(n):
   if(n==2):
      print("Computers: Paper")
      print("Oops You lost!!")
      gameover()
   else:
      print("Computer: Scissors")
      print("Woohoo Nice you won")
      gameover() 

def  Paper(n):
   if(n==1):
      print("Computers: Rock")
      print("Woohoo Nice you won")
      gameover()
   else:
      print("Computer: Scissors")
      print("Oops You lost!!")
      gameover()

def Scissor(n):
   if(n==2):
      print("Computers: Paper")
      print("Woohoo Nice you won")
      gameover()
   elif(n==1):
      print("Computers: Rock")
      print("Oops You lost!!")
      gameover()
      
start()     