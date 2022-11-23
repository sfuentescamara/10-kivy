from kivy.lang import Builder

from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem


class Test(MDApp):

    container = MDList()
    def build(self):
        kv = Builder.load_file("test.kv")
        
        return kv

    def on_start(self):
        for i in range(20):
            self.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )

Test().run()