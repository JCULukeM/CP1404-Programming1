
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

name_list = ['bob','jim','harry','mario','luke']


class DynamicLable(App):
    status_text = StringProperty()

    def build(self):
        self.title = "Dynamic label"
        self.root = Builder.load_file('DynamicLabel.kv')
        return self.root

    def create_widgets(self):
        for name in name_list:
            temp_button = Button(text=name)
            self.root.ids.entriesBox.add_widget(temp_button)


DynamicLable().run()
