# In[] Lets talk about objects first
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):
    def build(self):
        return LoginScreen()
MyApp().run()

# In[] What is a class
# a class is a blueprint of an objects

class FirstClass():
    pass

F = FirstClass()


# In[] the __init__ function and self

class Square():
    def __init__(self,side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length**2
    def getSidelength(self):
        return self.side_length

class Cat():
    def __init__(self,name,color):
        self.name = name
        self.color = color
        
    def meow(self):
        return self.name + " Meowed"
    
class Pencil():
    def __init__(self,manfname,mechanical,ID):
        self.m = manfname
        self.ismech = mechanical
        self.ID = ID
    

C = Cat("Walace","White and Orange")
    

# Make me a car with two inputs name and number of tires
# Give it one function called drive return [car name] drove


    



# In[]
S = Square(10)

# In[] other function types

class One():
    def __init__(self):
        pass
    def __add__(self,other):
        return 1+1
    
O = One()
print(O+O)
