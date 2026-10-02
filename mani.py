from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Ellipse
from kivy.clock import Clock
import random

JARVIS_BLUE = (0, 0.8, 1, 1)
BLACK = (0, 0, 0, 1)

class JarvisHUD(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        with self.canvas.before:
            Color(*BLACK)
            self.rect = Ellipse(pos=(0,0), size=(100,100))
            
        self.status_label = Label(
            text="[ J.A.R.V.I.S. ONLINE - MARK 1 ]",
            font_size='22sp',
            color=JARVIS_BLUE,
            bold=True
        )
        self.add_widget(self.status_label)
        
        self.output_label = Label(
            text="Awaiting Command, Sir...",
            font_size='18sp',
            color=(1, 1, 1, 0.7)
        )
        self.add_widget(self.output_label)

        self.btn = Button(
            text="TAP TO SPEAK",
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5},
            background_color=(0, 0.5, 0.7, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        self.add_widget(self.btn)

class JarvisApp(App):
    def build(self):
        return JarvisHUD()

if __name__ == "__main__":
    JarvisApp().run()
