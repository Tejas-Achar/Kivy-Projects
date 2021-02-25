from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader


class Test(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def play_sa(self):
        sound = SoundLoader.load('Sa.mp3')
        if sound:
            sound.play()
    def play_ri(self):
        sound = SoundLoader.load('Ri.mp3')
        if sound:
            sound.play()
    def play_ga(self):
        sound = SoundLoader.load('Ga.mp3')
        if sound:
            sound.play()
    def play_ma(self):
        sound = SoundLoader.load('Ma.mp3')
        if sound:
            sound.play()
    def play_pa(self):
        sound = SoundLoader.load('Pa.mp3')
        if sound:
            sound.play()
    def play_da(self):
        sound = SoundLoader.load('Da.mp3')
        if sound:
            sound.play()
    def play_ni(self):
        sound = SoundLoader.load('Ni.mp3')
        if sound:
            sound.play()
    def play_saa(self):
        sound = SoundLoader.load('Saaaa.mp3')
        if sound:
            sound.play()

class MusicApp(App):
    def build(self):
        return Test()

music = MusicApp()
music.run()
