class Sample:
    def __init__(self):
        # Private variable
        self.__privateVar = 10

    # Private method
    def __privMeth(self):
        print("This is a private method.")

    # Public method
    def hello(self):
        # Accessing private variable
        print("Value of privateVar:", self.__privateVar)
        
        # Calling private method inside the class
        self.__privMeth()


# Creating object of the class
obj = Sample()

# Calling public method
obj.hello()
