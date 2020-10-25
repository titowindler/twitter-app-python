from kivymd.app import MDApp
from kivy.core.window import Window
# from kivymd.uix.screen import Screen
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (300, 500)

screen_helper = """
ScreenManager:
    LoginScreen:
    HomeScreen:
   
<LoginScreen>:
    name: 'login'
    MDFloatLayout:
    MDLabel:
        text: "Login"
        pos_hint: {"center_y": .85}
        font_style: "H4"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: "Welcome To Twitter"
        pos_hint: {"center_y": .75}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDTextField:
        hint_text: "Enter Your Email"
        pos_hint: {"center_x": .5, "center_y": .6}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: .8
    MDTextField:
        hint_text: "Enter Your Password"
        pos_hint: {"center_x": .5, "center_y": .45}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: .8
        password: True
    MDRaisedButton: 
        text: "Log In"
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint_x: .5
        on_press: root.manager.current = 'home'
    MDRaisedButton: 
        text: "Sign In With Google"
        pos_hint: {"center_x": .5, "center_y": .20}
        size_hint_x: .5  

<HomeScreen>:
    name: 'home'
    BoxLayout:
    MDToolbar:
        title: 'Bottom navigation'
        md_bg_color: 1, 1, 1, 1
        specific_text_color: 1, 1, 1, 1
    MDBottomNavigation:
        panel_color: 1, 1, 1, 1
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Post'
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Search'
            Screen:
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "280dp", "180dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        MDLabel:
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]
            Image:
                source: "img//home-user-1.png"
                y: self.parent.y + self.parent.height - 100
                x: self.parent.x
                size_hint: .5, .2
        MDSeparator:
            height: "1dp"
        MDLabel:
            text: "Jennifer Lopez"
            pos_hint: {"center_x": .9, "center_y": .15}
        MDLabel:
            text: "Today is the last day of school and the first day of twitter"
            pos_hint: {"center_x": .5, "center_y": .10}
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Twitter"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            MDRaisedButton: 
                text: "Log Out"
                pos_hint: {"center_y": .7}
                size_hint_x: .5
                on_press: root.manager.current = 'login'


"""


class LoginScreen(Screen):
    pass


class HomeScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(HomeScreen(name='home'))


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        screen = Builder.load_string(screen_helper)
        return screen

DemoApp().run()