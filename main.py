from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window
import random

Window.size = (360, 640)
Window.clearcolor = (0.08, 0.09, 0.11, 1)


class JogoMemoria(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=18, spacing=12, **kwargs)

        self.nivel = 1
        self.sequencia = []
        self.indice = 0

        self.titulo = Label(
            text="Treino de Memória",
            font_size=24,
            bold=True,
            size_hint=(1, 0.12)
        )

        self.nivel_label = Label(
            text="Nível 1",
            font_size=18,
            size_hint=(1, 0.08)
        )

        self.numero_label = Label(
            text="Iniciar",
            font_size=44,
            bold=True,
            size_hint=(1, 0.32)
        )

        self.entrada = TextInput(
            hint_text="Digite a sequência",
            multiline=False,
            font_size=22,
            halign="center",
            input_filter="int",
            size_hint=(1, 0.10)
        )
        self.entrada.disabled = True

        self.botao_verificar = Button(
            text="Verificar",
            font_size=20,
            size_hint=(1, 0.10)
        )
        self.botao_verificar.disabled = True
        self.botao_verificar.bind(on_press=self.verificar)

        self.botao_iniciar = Button(
            text="Iniciar jogo",
            font_size=20,
            size_hint=(1, 0.10)
        )
        self.botao_iniciar.bind(on_press=self.iniciar_jogo)

        self.info = Label(
            text="Memorize cada número e digite a sequência.",
            font_size=13,
            size_hint=(1, 0.08)
        )

        self.add_widget(self.titulo)
        self.add_widget(self.nivel_label)
        self.add_widget(self.numero_label)
        self.add_widget(self.entrada)
        self.add_widget(self.botao_verificar)
        self.add_widget(self.botao_iniciar)
        self.add_widget(self.info)

    def iniciar_jogo(self, instance=None):
        self.nivel = 1
        self.sequencia = []
        self.nova_rodada()

    def nova_rodada(self):
        self.entrada.text = ""
        self.entrada.disabled = True
        self.botao_verificar.disabled = True

        self.nivel_label.text = f"Nível {self.nivel}"

        numero = random.randint(0, 9)
        self.sequencia.append(numero)

        self.indice = 0
        Clock.schedule_once(self.mostrar_numero, 0.5)

    def mostrar_numero(self, dt=None):
        if self.indice < len(self.sequencia):
            self.numero_label.text = str(self.sequencia[self.indice])
            Clock.schedule_once(self.esconder_numero, 0.7)
        else:
            self.numero_label.text = "Digite"
            self.entrada.disabled = False
            self.botao_verificar.disabled = False
            self.entrada.focus = True

    def esconder_numero(self, dt=None):
        self.numero_label.text = ""
        self.indice += 1
        Clock.schedule_once(self.mostrar_numero, 0.3)

    def verificar(self, instance=None):
        resposta = self.entrada.text.strip()
        correta = "".join(str(n) for n in self.sequencia)

        self.entrada.text = ""

        if resposta == correta:
            self.numero_label.text = "Certo!"
            self.nivel += 1
            Clock.schedule_once(lambda dt: self.nova_rodada(), 1)
        else:
            self.numero_label.text = f"Errou\nEra {correta}"
            Clock.schedule_once(lambda dt: self.iniciar_jogo(), 2)


class AppMemoria(App):
    def build(self):
        return JogoMemoria()


if __name__ == "__main__":
    AppMemoria().run()git --version