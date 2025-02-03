#Magic8Ball.py
#Name: Alex Hernandez Lopez
#Date: 2/2/25
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
 print("Magic 8 Ball")
  #Prompt the user for their question.
answers = ["As I see it, yes", "Ask again later", "Better not tell you now", 
             "Cannot predict now", "Concentrate and ask again", "Don't count on it",
             "It is certain", "It is decidedly so", "Most likely", "My reply is no"]
input("Ask a question: ")
  #Answer question randomly with one of the options from your earlier list.
length = len(answers)
r = random.random() *  length
r = int(r)
response = answers[r]
print(response)
if __name__ == '__main__':
  main()
