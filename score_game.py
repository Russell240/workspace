def validate_input_to_integer(userInput): 
     while userInput!=int:
         try:
             value = int(input(userInput)) 
         except ValueError:
            print("Enter a valid int")
            continue
         if value<0 or value>= 100:
            print("Sorry, your response must not be negative and between 1 and 100: "  )
           
         else:
            break
     return value

def main():
    user1 = validate_input_to_integer(("Enter score of player 1: "))
    user2 = validate_input_to_integer(("Enter score of player 2: "))
    user3 = validate_input_to_integer(("Enter score of player 3: "))
    if(user1>user2) and (user1>user3): 
        print("User One scored Highest Score") 
        if(user2==user3):
            print("Score of user 2 and user 3 is equal")    
    if(user2>user1) and (user2>user3):  
        print("User Two scored Highest Score")
        if(user3==user1): 
            print("Score of User 1 and User 3  is equal") 
    if(user3> user2 ) and (user3> user1):
        print("User Three scored the highest score.")       
        if(user1==user2):
                print("Score of User 2 is the same as User1 ")
    elif(user1==user2) and (user2==user3) and (user3==user1):
        print("All scores are equal there was no winner ") 
    else: 
        print("error ") 
    
if __name__ == "__main__":
 main()