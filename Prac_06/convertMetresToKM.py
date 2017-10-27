
from kivy.app import App
from kivy.lang import Builder

memes = 1.609344


class ConvertMtoKM (App):
    def build(self):
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert.kv')
        return self.root

    def handle_convert(self):
        value = self.valid_input()
        result = value * memes
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        value = self.valid_input() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_convert()

    def valid_input(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0.0


ConvertMtoKM().run()