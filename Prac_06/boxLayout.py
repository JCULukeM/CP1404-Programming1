
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('boxy_layout.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.my_label.text = "Hello " + self.root.ids.input_name.text
        print('greet')

    def clear_input(self):
        self.root.ids.input_name.text = ""
        self.root.ids.my_label.text = "Enter your name"



BoxLayoutDemo().run()
