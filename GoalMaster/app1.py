from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.image import Image
from kivy.lang import Builder

kv = """
Screen:

    MDNavigationDrawer:
        NavigationDrawerHeaderBase:
            Image:
                source: 'your_logo.png'  # Replace with your logo
                size_hint_y: None
                height: dp(80)

        BoxLayout:
            orientation: 'vertical'

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)

                MDLabel:
                    text: "GoalMaster: Aim High"
                    font_style: 'H4'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: username
                    hint_text: "User ID"
                    size_hint_x: None
                    width: 300
                    pos_hint: {'center_x': 0.5}
                
                MDTextField:
                    id: password
                    hint_text: "Password"
                    size_hint_x: None
                    width: 300
                    password: True
                    pos_hint: {'center_x': 0.5}

                MDRoundFlatButton:
                    text: "Forgot User ID or Password"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': 0.5}

                MDRoundFlatButton:
                    text: "Don't have an account yet? Sign up now!"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': 0.5}

                Image:
                    source: 'face_id_logo.png'
                    size_hint_y: None
                    height: 50
                    pos_hint: {'center_x': 0.5}

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)

                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: "User's Profile"
                            on_release: app.show_section('User Profile')

                        OneLineListItem:
                            text: "Goal Creation"
                            on_release: app.show_section('Goal Creation')

                        OneLineListItem:
                            text: "Expense Tracking"
                            on_release: app.show_section('Expense Tracking')

                        OneLineListItem:
                            text: "Savings Monitoring"
                            on_release: app.show_section('Savings Monitoring')

                        OneLineListItem:
                            text: "Reviewing History"
                            on_release: app.show_section('Reviewing History')

                        OneLineListItem:
                            text: "Sign Out"
                            on_release: app.sign_out()

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: "GoalMaster"
            elevation: 10
            left_action_items: [["menu", lambda x: app.root.toggle_nav_drawer()]]

        ScreenManager:
            id: screen_manager
            Screen:
                name: 'User Profile'
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(10)
                    spacing: dp(10)
                    MDLabel:
                        text: 'User Profile Section'
            Screen:
                name: 'Goal Creation'
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(10)
                    spacing: dp(10)
                    MDLabel:
                        text: 'Goal Creation Section'
            Screen:
                name: 'Expense Tracking'
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(10)
                    spacing: dp(10)
                    MDLabel:
                        text: 'Expense Tracking Section'
            Screen:
                name: 'Savings Monitoring'
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(10)
                    spacing: dp(10)
                    MDLabel:
                        text: 'Savings Monitoring Section'
            Screen:
                name: 'Reviewing History'
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(10)
                    spacing: dp(10)
                    MDLabel:
                        text: 'Reviewing History Section'
"""

class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def show_section(self, section_name):
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = section_name

    def sign_out(self):
        # Add sign-out logic here
        pass

DemoApp().run()
