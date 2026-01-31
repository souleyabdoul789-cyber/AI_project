from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from app import parler_ia

class IAInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.chat = Label(size_hint_y=None, text="")
        self.chat.bind(texture_size=self.chat.setter('size'))

        scroll = ScrollView()
        scroll.add_widget(self.chat)

        self.input = TextInput(size_hint_y=0.15, multiline=False)
        btn = Button(text="Envoyer", size_hint_y=0.15)
        btn.bind(on_press=self.envoyer)

        self.add_widget(scroll)
        self.add_widget(self.input)
        self.add_widget(btn)

    def envoyer(self, instance):
        message = self.input.text
        if message.strip() == "":
            return

        self.chat.text += f"\nToi : {message}\n"
        self.input.text = ""

        reponse = parler_ia(message)
        self.chat.text += f"IA : {reponse}\n"

class IAApp(App):
    def build(self):
        return IAInterface()

IAApp().run()