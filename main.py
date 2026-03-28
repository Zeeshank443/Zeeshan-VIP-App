from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import random

# Black Background for VIP look
Window.clearcolor = (0, 0, 0, 1)

class ZeeshanVIPApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Title Label
        self.label = Label(
            text="[b][color=00FF00]ZEESHAN KHAN[/color][/b]\n[color=FFFFFF]THE HEARTLESS - VIP TOOLKIT[/color]", 
            markup=True, 
            font_size='24sp',
            halign='center'
        )
        self.layout.add_widget(self.label)
        
        # Identity Display (Invisible at start)
        self.identity_label = Label(text="", markup=True, font_size='16sp', halign='left')
        self.layout.add_widget(self.identity_label)
        
        # Ghost Mode Button
        self.ghost_btn = Button(
            text="GENERATE GHOST IDENTITY", 
            background_color=(0, 0.5, 1, 1),
            size_hint_y=None, height='60dp'
        )
        self.ghost_btn.bind(on_press=self.generate_ghost)
        self.layout.add_widget(self.ghost_btn)
        
        # Reset Button
        reset_btn = Button(text="CLEAR DATA", size_hint_y=None, height='40dp')
        reset_btn.bind(on_press=self.clear_data)
        self.layout.add_widget(reset_btn)
        
        return self.layout

    def generate_ghost(self, instance):
        names = ["Agent_X", "Silent_Shadow", "Phantom_786", "Ghost_Z"]
        ips = [f"192.168.{random.randint(1,254)}.{random.randint(1,254)}" for _ in range(1)]
        locations = ["London Proxy", "Moscow Relay", "Dubai Tunnel", "Tokyo Vault"]
        
        identity = (
            f"[color=00FF00]NAME:[/color] {random.choice(names)}\n"
            f"[color=00FF00]FAKE IP:[/color] {ips[0]}\n"
            f"[color=00FF00]LOCATION:[/color] {random.choice(locations)}\n"
            f"[color=FFFF00]STATUS: INVISIBLE[/color]"
        )
        self.identity_label.text = identity
        self.label.text = "[b][color=00FF00]GHOST MODE ACTIVE[/color][/b]"

    def clear_data(self, instance):
        self.identity_label.text = ""
        self.label.text = "[b][color=FFFFFF]THE HEARTLESS - VIP TOOLKIT[/color][/b]"

if __name__ == "__main__":
    ZeeshanVIPApp().run()
    
