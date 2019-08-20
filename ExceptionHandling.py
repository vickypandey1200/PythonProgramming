class ExceptionHandler:
    result=0
    def __init__(self, value):
        self.value=value
    def compute(self):
        try:
            result = value/0
        except ZeroDivisionError:
                print("Do not divide by zero")
    print("result is " + str(result))

value=5
exHandle=ExceptionHandler(value)
exHandle.compute()
        
