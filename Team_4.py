from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import datetime
import matplotlib.pyplot as plt
import numpy as np

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

        self.description_label = Label(text="Input description")
        layout.add_widget(self.description_label)

        self.description_input = TextInput(text="", hint_text="Enter Description")
        layout.add_widget(self.description_input)

        enter_btn = Button(text="Enter", on_press=self.enter_pressed)
        layout.add_widget(enter_btn)

        self.add_widget(layout)

    def back_pressed(self, instance):
        self.manager.current = "Main"

    def enter_pressed(self, instance):
        spending = self.spending_input.text
        description = self.description_input.text

        if spending and description:
            transaction = Transaction(datetime.datetime.now(), float(spending), "", description)
            history_screen = self.manager.get_screen("History")
            history_screen.add_transaction(transaction)

            self.spending_input.text = ""
            self.description_input.text = ""

class HistoryScreen(Screen):
    def __init__(self, name="History"):
        super().__init__(name=name)

        layout = BoxLayout(orientation='vertical')

        self.transaction_list = []
        self.transaction_label = Label(text="No transactions yet")
        layout.add_widget(self.transaction_label)

        stat_btn = Button(text="Statistics", on_press=self.show_statistics)
        layout.add_widget(stat_btn)

        back_btn = Button(text="Back", on_press=self.back_pressed)
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

        layout = BoxLayout(orientation='vertical')

        week_chart_btn = Button(text="Week Chart", on_press=self.show_week_chart)
        layout.add_widget(week_chart_btn)

        month_chart_btn = Button(text="Month Chart", on_press=self.show_month_chart)
        layout.add_widget(month_chart_btn)

        half_year_chart_btn = Button(text="Half Year Chart", on_press=self.show_half_year_chart)
        layout.add_widget(half_year_chart_btn)

        back_btn = Button(text="Back", on_press=self.back_pressed)
        layout.add_widget(back_btn)

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

        
        fig_canvas = FigureCanvasKivyAgg(plt.gcf())
        self.add_widget(fig_canvas)

       
        plt.clf()

    def show_month_chart(self, instance):
        
        x = np.arange(30)
        y = np.random.randint(10, 100, size=30)

        plt.figure()
        plt.plot(x, y)
        plt.xlabel('Days')
        plt.ylabel('Expenditure')
        plt.title('Monthly Expenditure')

       
        fig_canvas = FigureCanvasKivyAgg(plt.gcf())
        self.add_widget(fig_canvas)

       
        plt.clf()

    def show_half_year_chart(self, instance):
      
        x = np.arange(180)
        y = np.random.randint(10, 100, size=180)

        plt.figure()
        plt.plot(x, y)
        plt.xlabel('Days')
        plt.ylabel('Expenditure')
        plt.title('Half Year Expenditure')

        
        fig_canvas = FigureCanvasKivyAgg(plt.gcf())
        self.add_widget(fig_canvas) 
        plt.clf()

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

if __name__ == "__main__":
    FinanceApp().run()
