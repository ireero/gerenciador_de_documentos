import tkinter as tk
import leitor_de_pastas as l

class Tela:

    def __init__(self) -> None:
        self.trocado = False
        self.leitor_pastas = l.LeitosDePastas()

        print(self.leitor_pastas.pastas)

        # Cria a janela
        window = tk.Tk()
        window.title("Tela com Tkinter")
        # Cria label centralizada
        self.text_label = tk.Label(window, text="Texto Centralizado", font=("Helvetica", 16))
        self.text_label.pack(pady=50)
        # Cria janela
        window.geometry("400x300")
        # Cria botão
        self.button = tk.Button(window, text="Clique Aqui", command=self.button_click)
        self.button.pack()

        # Iniciar o loop de eventos
        window.mainloop()

    def button_click(self):
        if self.trocado:
            self.trocado = False
            self.text_label.config(text=f"Texto Centralizado")
        else:
            self.trocado = True
            self.text_label.config(text=f"{self.leitor_pastas.pastas}")

b = Tela()