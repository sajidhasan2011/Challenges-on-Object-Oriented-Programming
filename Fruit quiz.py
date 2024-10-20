import random
class FruitQuiz:
    
    def __init__(self):
        
        self.fruit ={
            'apple':'red',

            'orange':'orange',

            'watermelon':'green',

            'banana':'yellow'
        }
        
    def quiz(self):
        while (True):
            
            fruit,color = random.choice(list(self.fruit.items()))
            
            print(f"What is the color of {fruit}?")
            user_answer = input()
            
            if(user_answer.lower()== color):
                print("Correct answer")
            else:
                print("Wrong Answer")
                
            option = int (input("enter 0, if you want to add another flashcard otherwise enter 1:"))
            if (option):
                break
            
print("welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()