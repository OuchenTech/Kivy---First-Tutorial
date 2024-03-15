from kivy.config import Config
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '650')

from kivymd.app import MDApp

from screens.tutorialone.tutorialone import TutorialOne

class MainApp(MDApp):
    def build(self):
        self.title = 'First Tutorial'
        
    def on_start(self):
        self.root.current= 'tutorial_one'
        
if __name__ == '__main__':
    MainApp().run()