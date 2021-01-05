class hand:
    def func(self):
        print("inside func1")
        condition = True
        i = 1
        while condition:
            try:
                for i in range(-3, 3):
                    print(5/i)      
            except ZeroDivisionError:
                print("zero div found")
                print("do you wanna continue?")
                choice = input()
                if choice == "y" or choice == "Y":
                    condition = True
                else:
                    condition = False
                #if !condition :
                    
            finally:
                print("inside finally")

h = hand()
h.func()