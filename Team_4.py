from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description


class MainScreen(Screen):
    def __init__(self, name="Main"):
        super().__init__(name=name)

        layout = BoxLayout(orientation='vertical')

        start_btn = Button(text="Start", on_press=self.start_pressed)
        layout.add_widget(start_btn)

        history_btn = Button(text="History", on_press=self.history_pressed)
        layout.add_widget(history_btn)

        self.add_widget(layout)

    def start_pressed(self, instance):
        self.manager.current = "Convert Menu"

    def history_pressed(self, instance):
        self.manager.current = "History"


class ConvertMenu(Screen):
    def __init__(self, name="Convert Menu"):
        super().__init__(name=name)

        layout = BoxLayout(orientation='vertical')

        back_btn = Button(text="Back", on_press=self.back_pressed)
        layout.add_widget(back_btn)

        self.input_label = Label(text="Input spendings")
        layout.add_widget(self.input_label)

        self.spending_input = TextInput(text="", hint_text="Enter Spending")
        layout.add_widget(self.spending_input)

        enter_btn = Button(text="Enter", on_press=self.enter_pressed)
        layout.add_widget(enter_btn)

        # start_convert_btn = Button(text="Start Convert", on_press=self.convert_pressed)
        # layout.add_widget(start_convert_btn)

        self.add_widget(layout)

    def back_pressed(self, instance):
        self.manager.current = "Main"

    def convert_pressed(self, instance):
        pass

    def enter_pressed(self, instance):
        pass


class HistoryScreen(Screen):
    def __init__(self, name="History"):
        super().__init__(name=name)

        layout = BoxLayout(orientation='vertical')

        self.transaction_list = []
        self.transaction_label = Label(text="No transactions yet")
        layout.add_widget(self.transaction_label)

        self.add_widget(layout)

    def add_transaction(self, transaction):
        self.transaction_list.append(transaction)
        self.transaction_label.text = ""
        for t in self.transaction_list:
            self.transaction_label.text += f"{t.date}: {t.amount} - {t.category}\n"

    def clear_transactions(self, instance):
        self.transaction_list = []
        self.transaction_label.text = "No transactions yet"


class FinanceApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="Main"))
        sm.add_widget(ConvertMenu(name="Convert Menu"))
        sm.add_widget(HistoryScreen(name="History"))

        return sm


if __name__ == "__main__":
    FinanceApp().run()
