from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Screen ka background black kar dete hain VIP look ke liye
Window.clearcolor = (0, 0, 0, 1)

class ZeeshanVIPApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Title Label
        self.label = Label(
            text="[b][color=00FF00]ZEESHAN KHAN[/color][/b]\n[color=FFFFFF]THE HEARTLESS - VIP EDITION[/color]", 
            markup=True, 
            font_size='28sp',
            halign='center'
        )
        layout.add_widget(self.label)
        
        # Input Box
        self.pass_input = TextInput(
            hint_text="Enter Secret Password", 
            password=True, 
            multiline=False,
            size_hint_y=None,
            height='50dp'
        )
        layout.add_widget(self.pass_input)
        
        # Login Button
        btn = Button(
            text="ACTIVATE PROTOCOL", 
            background_color=(0, 1, 0, 1),
            size_hint_y=None,
            height='60dp',
            font_size='20sp'
        )
        btn.bind(on_press=self.check_login)
        layout.add_widget(btn)
        
        return layout

    def check_login(self, instance):
        if self.pass_input.text == "ZEESHAN786":
            self.label.text = "[b][color=00FF00]SYSTEM READY.\nWELCOME MASTER.[/color][/b]"
        else:
            self.label.text = "[b][color=FF0000]ACCESS DENIED![/color][/b]"

if __name__ == "__main__":
    ZeeshanVIPApp().run()
    
