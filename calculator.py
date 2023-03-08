

def Calculate():
        ask = input("Enter Symbol + - x / for required Operation ")
        result = 0
        x = 0
        y = 0
        con = "="

        if ask == "+":
            Add()
        elif ask == "-":
            Subtract()
        elif ask == "x":
            MultyPly()
        elif ask == "/":
            Devide()

        After()
    # con = ""
    # con = input("Enter = To Continue or Enter Another Character word to cancel")
    # if (con != "="):          
    #       break

    
    


def Add():
         #means Add
        x = int(input("Please Add First Number and Press Enter "))
        y = int (input("Please Add Secound Number and Press Enter "))
        result = x +y
        print(f"total is {result}")
        #After()

def Subtract():
        x = int(input("Please Add First Number and Press Enter "))
        y = int (input("Please Add Secound Number and Press Enter "))
        result = x -y
        print(f"Result After Subtraction is {result}")
        #After()


def MultyPly():
        x = int(input("Please Add First Number and Press Enter "))
        y = int (input("Please Add Secound Number and Press Enter "))
        result = x*y
        print(f"Result After Multyply is {result}")
       # After()


def Devide():
        x = int(input("Please Add First Number and Press Enter "))
        y = int (input("Please Add Secound Number and Press Enter "))
        result = x/y
        print(f"Result After Devide is {result}")
        


def After():
      con = input("Press I to Continue P to cancel ")
      if con.lower() =="i":
        Calculate()
      else:
            print("You Choose P To Cancle Program Aborted ")
            return

Calculate()



      


