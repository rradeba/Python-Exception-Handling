                 
#task 1-4 
#define function to request temp, convert, round and process errors 
while True:
        try: 
            enter_temp = float(input("Please enter the temperature(F): "))   
            temp_celsius = ((enter_temp - 32) * (5/9))
            rounded_temp_celsius = round(temp_celsius, 1)
        except ValueError:    
            print("Incorrect input, please type a number.")
        else: 
            print(f"{enter_temp} degrees F equals {rounded_temp_celsius} degrees C")
            break 
        finally: 
             print("Thank you for using Reid's Weather Application")


             
    



