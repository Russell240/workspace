def validate_input_to_integer(userInput):
    while userInput!=int:
            try:
                value = int(input(userInput)) 
            except ValueError:
                print("Enter a valid integer not a decimal number : " )
                continue
            if value<0 or value>95 :
                print("Sorry, your response must not be negative and between 1 and 95: "  )
            
            else:
                break
    return value


def main():
    marks = validate_input_to_integer("Enter your marks: ")
    percentage= (marks/95)*100
    if marks>=90: 
        print("Excellent your percentage is %s this is a good percentage you achieved the top grade "%percentage )
    elif marks<90 and marks>=75: 
        print("""First Class your percentage is %s you need to get
        a  higher percentage  to get the best grade"""%percentage) 
    elif marks<75 and marks>=40: 
          print("Your Percentage Achieved in the exam is %s you need get atleast 75 marks to get a good grade "%percentage)
        
    else: 
        print("You Failed  Your Percentage Achieved in the exam is %s " %percentage) 
    
if __name__ == "__main__":
    main()