import tkinter as tk

class Base:

    def __init__(self) -> None:
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
        self.text_label.config(text="Botão clicado!")
    

b = Base()