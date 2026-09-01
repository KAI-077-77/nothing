print("------ ATM Management System ------")

pin = 1234
balance = 1000000

def login(correct_p):
    a = 0
    while a < 3:
        p = int(input(" Enter your 4-digit PIN : "))

        if p == correct_p:
            print("Login Successful")
            return True
        else:
            a += 1
            print("Wrong PIN. Attempts left:", 3 - a)

    print("Maximum login attempts exceeded.")
    return False

def show_menu():

    print("------ MENU ------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")
    
    c = int(input("Enter option number: "))
    return c

if login(pin):
    while True:
        c=show_menu()
        if c== 1:
            print("Your Balance: ₹", balance)
            
        elif c == 2:
            d = int(input("Enter the deposit amount: "))
            if d > 0:
                balance = balance + d
                print("₹", d, "Deposited Successfully")
                print("New Balance: ₹", balance)
            else:
                print("Invalid Amount. Must be greater than 0")
                
        elif c == 3:
            w = int(input("Enter the withdrawal amount: "))
            if w <= 0:
                print("Invalid Amount")
            elif w > balance:
                print("Insufficient Balance. Your Balance: ₹", balance)
            else:
                balance = balance - w
                print("₹", w, "Withdrawn Successfully")
                print("Remaining Balance: ₹", balance)
                
        elif c== 4:
            old_pin = int(input("Enter current PIN: "))
            if old_pin == pin:
                new_pin = int(input("Enter new 4-digit PIN: "))
                if len(str(new_pin)) == 4:
                    pin = new_pin
                    print("PIN Changed Successfully")
                else:
                    print("PIN must be 4 digits")
            else:
                print("Wrong Current PIN")
                
        elif c == 5:
            print("Exiting!")
            break
            
        else:
            print("Invalid Choice. Please enter choice between 1-5")
else:
    print("Exiting program.")