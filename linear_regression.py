class linear:
    def fit(self):
        print("Do you want to predict anything")
        a = int(input())
        if a in "yY":
            predict()
        
    def predict(self, a, b):
        x,y = 0,0
        print("enter the predictor for which the response to be predicted")
        x = int(input())
        y = a*x + b       
        print(y)                              

    def fit(self):
        pass


l1 = linear()