#configuração para não dar erro do OpenGL 2.0
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#----

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
import math 

Window.clearcolor = (14/255, 61/255, 76/255, 0)
Window.size = (400, 600)

class CalculadoraTela(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.operadores = ['+', '-', '*', '/', '√']
        self.ultimo_operador = None
        self.ultimo_botao = None

    def on_button_press(self, instance):
        resultado_atual = self.ids.resultado.text
        button_text = instance.text

        if button_text in self.operadores:
            if button_text == '√':
                if resultado_atual: 
                    try:
                        result = str(math.sqrt(float(resultado_atual)))
                        self.ids.resultado.text = result
                    except ValueError:
                        self.ids.resultado.text = "Erro"
                return    
            if resultado_atual and (self.ultimo_operador is False):
                self.ids.resultado.text += button_text
                self.ultimo_operador = True
            elif resultado_atual == '' and button_text == '-':
                self.ids.resultado.text += button_text
                self.ultimo_operador = True
        else:
            if resultado_atual == '' and button_text == '0':
                return
            else:
                self.ids.resultado.text += button_text
                self.ultimo_operador = False

        self.ultimo_botao = button_text

    def on_solution(self, instance):
        text = self.ids.resultado.text
        if text:
            try:
                solution = str(eval(text))
                self.ids.resultado.text = solution
            except Exception as e:
                self.ids.resultado.text = "Erro"

    def on_clear(self, instance):
        self.ids.resultado.text = ''

class CalculatodoraApp(App):
    def build(self):
        return CalculadoraTela()

if __name__ == '__main__':
    Builder.load_file('calculadora_tela.kv')
    CalculatodoraApp().run()
