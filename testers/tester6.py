while True:
    
    try:
        number = int(input("Enter a number : "))
        break
    
    except ValueError:
        print("You didn't enter a number")
    
    except:
        print("An unknown error has occurred")
        
print("Thank you for entering a number")
