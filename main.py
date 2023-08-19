#Welcome message
print("Welcome to the Love Calculator!")

#Ask for input
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


#Convert the names to lowercase
name1=name1.lower()
name2=name2.lower()
#Join the two names together for counting
names=name1+name2
#Check for the number of times the letters in the word TRUE occurs. 
true_count=str(names.count("t")+names.count("r")+names.count("u")+names.count("e"))
#Check for the number of times the letters in the word LOVE occurs. 
love_count=str(names.count("l")+names.count("o")+names.count("v")+names.count("e"))
#Combine these numbers to make a 2 digit number.
result=true_count+love_count
result=int(result)
#For Love Scores less than 10 or greater than 90:
if result <10 or result>90:
    print(f"Your score is {result}, you go together like coke and mentos.")
#For Love Scores between 40 and 50:
elif result >= 40 and result <=50:
        print(f"Your score is {result}, you are alright together.")
#Otherwise, just display score
else:
    print(f"Your score is {result}")
