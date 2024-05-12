from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import datetime
import matplotlib.pyplot as plt
import numpy as np
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang import Builder
from kivy.uix.image import Image


class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

class MainScreen(Screen):
    def __init__(self, name="Main"):
        super().__init__(name=name)
        

        layout = BoxLayout(orientation='vertical', size_hint=(1, 1), pos_hint={'center_x': 0.775, 'center_y': 1}, spacing=20)
        
        start_btn = Button(text="Start", on_press=self.start_pressed, size_hint=(None, None), size=(200, 50), padding=(10, 10), background_color='#0000ff')
        layout.add_widget(start_btn)

        history_btn = Button(text="History", on_press=self.history_pressed, size_hint=(None, None), size=(200, 50), padding=(10, 10), background_color='#0000ff')
        layout.add_widget(history_btn)

        self.add_widget(layout)

    def start_pressed(self, instance):
        self.manager.current = "Convert Menu"

    def history_pressed(self, instance):
        self.manager.current = "History"

class ConvertMenu(Screen):
    def __init__(self, name="Convert Menu"):
        super().__init__(name=name)
        

        layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        
        back_btn = Button(text="Back", on_press=self.back_pressed, size_hint=(None, None), size=(150, 50), pos_hint={'x': 0.69, 'y': -1}, background_color='#0000ff')
        layout.add_widget(back_btn)

        self.input_label = Label(text="Input spendings", size=(200, 50), color=[1, 1, 1, 1])
        layout.add_widget(self.input_label)

        self.spending_input = TextInput(text="", hint_text="Enter Spending", foreground_color='#0f0f0f')
        layout.add_widget(self.spending_input)

        self.description_label = Label(text="Input description", color=[1, 1, 1, 1])
        layout.add_widget(self.description_label)

        self.description_input = TextInput(text="", hint_text="Enter Description", foreground_color='#0f0f0f')
        layout.add_widget(self.description_input)

        enter_btn = Button(text="Enter", on_press=self.enter_pressed, size_hint=(None, None), size=(450, 50), pos_hint={'x': 0, 'y': 0}, background_color='#0000ff')
        layout.add_widget(enter_btn)

        self.add_widget(layout)

    def back_pressed(self, instance):
        self.manager.current = "Main"

    def enter_pressed(self, instance):
        spending = self.spending_input.text
        description = self.description_input.text

        if spending and description:
            transaction = Transaction(datetime.datetime.now().strftime("%d.%m.%Y %H:%M"), float(spending), "", description)
            history_screen = self.manager.get_screen("History")
            history_screen.add_transaction(transaction)

            self.spending_input.text = ""
            self.description_input.text = ""

class HistoryScreen(Screen):
    def __init__(self, name="History"):
        super().__init__(name=name)
        

        layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
       

        self.transaction_list = []
        self.transaction_label = Label(text="No transactions yet", color='#E6E6FA')
        layout.add_widget(self.transaction_label)
        
        stat_btn = Button(text="Statistics", on_press=self.show_statistics, size_hint=(None, None), size=(150, 50), padding=(10, 10), background_color='#0000ff')
        layout.add_widget(stat_btn)

        back_btn = Button(text="Back", on_press=self.back_pressed, size_hint=(None, None), size=(150, 50), padding=(10, 10), background_color='#0000ff')
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def add_transaction(self, transaction):
        self.transaction_list.append(transaction)
        self.transaction_label.text = ""
        for t in self.transaction_list:
            self.transaction_label.text += f"{t.date}: {t.amount} - {t.category}: {t.description}\n"

    def clear_transactions(self, instance):
        self.transaction_list = []
        self.transaction_label.text = "No transactions yet"

    def back_pressed(self, instance):
        self.manager.current = "Main"

    def show_statistics(self, instance):
        self.manager.current = "Statistics"

class StatisticsScreen(Screen):
    def __init__(self, name="Statistics"):
        super().__init__(name=name)
        

        layout = BoxLayout(orientation='vertical', spacing=20)
       

        week_chart_btn = Button(text="Week Chart", on_press=self.show_week_chart, size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 10}, background_color='#0000ff')
        layout.add_widget(week_chart_btn)

        month_chart_btn = Button(text="Month Chart", on_press=self.show_month_chart, size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color='#0000ff')
        layout.add_widget(month_chart_btn)

        half_year_chart_btn = Button(text="Half Year Chart", on_press=self.show_half_year_chart, size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3}, background_color='#0000ff')
        layout.add_widget(half_year_chart_btn)

        back_btn = Button(text="Back", on_press=self.back_pressed, size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.1}, background_color='#0000ff')
        layout.add_widget(back_btn)
        image = Image(source='a.jpg', size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        layout.add_widget(image)

        self.add_widget(layout)

    def show_week_chart(self, instance):
        x = np.arange(7)
        y = np.random.randint(10, 100, size=7)

        plt.figure()
        plt.bar(x, y)
        plt.xlabel('Days')
        plt.ylabel('Expenditure')
        plt.title('Weekly Expenditure')
        plt.xticks(x, ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

        plt.show()

    def show_month_chart(self, instance):
        x = np.arange(30)
        y = np.random.randint(10, 100, size=30)

        plt.figure()
        plt.plot(x, y)
        plt.xlabel('Days')
        plt.ylabel('Expenditure')
        plt.title('Monthly Expenditure')

        plt.show()

    def show_half_year_chart(self, instance):
        x = np.arange(180)
        y = np.random.randint(10, 100, size=180)

        plt.figure()
        plt.plot(x, y)
        plt.xlabel('Days')
        plt.ylabel('Expenditure')
        plt.title('Half Year Expenditure')

        plt.show()

    def back_pressed(self, instance):
        self.manager.current = "History"

class FinanceApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="Main"))
        sm.add_widget(ConvertMenu(name="Convert Menu"))
        sm.add_widget(HistoryScreen(name="History"))
        sm.add_widget(StatisticsScreen(name="Statistics"))
    
        return sm

class MainApp(App):
     if platform != 'android''ios':
        Window.size = (350,600)
        Window.left = +500
        Window.top = 100

if __name__ == "__main__":
    FinanceApp().run()
