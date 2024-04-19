from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label




class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description


class mainscreen(Screen):
    def __init__(self, name="Main"):
        super(mainscreen, self).__init__(name=name)
        t=TextInput()

        btn=Button(text="Start", on_press=self.switch_1)
        btn2=Button(text="History", on_press=self.switch_2)

        t.add_widget(btn)
        t.add_widget(btn2)
        self.add_widget(t)



def switch_1(self):
    self.sm.current = "Convert Menu"


def switch_2(self):
    self.sm.current = "History"


class ConvertMenu(Screen):
    def __init__(self, name="Convert Menu"):
        super(ConvertMenu, self).__init__(name=name)
        t=TextInput(orientation='vertical')
        back_btn=Button(text="Back", on_press=self.switch_back)
        input=TextInput()
        self.txt=Label(text="Input spendings")

