# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
import tkinter as tk
from tkinter import ttk
# Requires tkcalendar:  pip install tkcalendar
from tkcalendar import DateEntry
from bibliotecas.json_gravacao import Json_utils

THEME_BG = "#2b2b2b"
THEME_FG = "#e8e8e8"
THEME_ACCENT = "#4a9eff"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#3c3c3c"
THEME_FONT = ("Segoe UI", 10)

json_prototipo = {
            "gastos" : {
                "hora" : [],
                "aluguel" : [],
                "transporte" : [],
                "internet" : [],
                "alimentacao" : [],
            },
            "investimentos" : {
                "renda_fixa" : [],
                "tesouro_direto" : [],
                "acoes" : [],
                "fiis" : []
            }
        }
Json_utils("controle").gravar_json(json_prototipo)

def apply_theme(root):
    """Apply the project theme as defaults; per-widget options override these."""
    root.configure(bg=THEME_BG)
    root.option_add("*background", THEME_BG)
    root.option_add("*foreground", THEME_FG)
    root.option_add("*font", THEME_FONT)
    root.option_add("*Entry.background", THEME_FIELD_BG)
    root.option_add("*Text.background", THEME_FIELD_BG)
    root.option_add("*Listbox.background", THEME_FIELD_BG)
    root.option_add("*Button.background", THEME_ACCENT)
    root.option_add("*Button.foreground", THEME_ACCENT_FG)
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
    style.configure(".", background=THEME_BG, foreground=THEME_FG, fieldbackground=THEME_FIELD_BG, font=THEME_FONT)


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Controle orçamento")
        root.geometry("520x380")
        apply_theme(root)

        self.label1 = tk.Label(root, text="Gastos")
        self.label1.place(x=215, y=0, width=90, height=26)

        self.label2 = tk.Label(root, text="Tipo de Gasto")
        self.label2.place(x=50, y=40, width=90, height=26)

        self.combobox1 = ttk.Combobox(root, values=["Aluguel", "Transporte", "Internet", "Alimentação"])
        self.combobox1.place(x=15, y=72, width=160, height=28)

        self.Label3 = tk.Label(root, text="Valor Gasto")
        self.Label3.place(x=215, y=40, width=90, height=26)

        self.entry2 = tk.Entry(root)
        self.entry2.place(x=200, y=70, width=120, height=30)

        self.label4 = tk.Label(root, text="Dia")
        self.label4.place(x=360, y=40, width=90, height=26)

        self.dateentry1 = DateEntry(root, date_pattern="yyyy-mm-dd")
        self.dateentry1.place(x=350, y=71, width=130, height=28)

        # self.separator1 = ttk.Separator(root, orient="horizontal")
        # self.separator1.place(x=0, y=160, width=520, height=20)

        self.label5 = tk.Label(root, text="Investimentos")
        self.label5.place(x=215, y=177, width=90, height=26)

        self.combobox2 = ttk.Combobox(root, values=["Renda fixa", "Tesouro direto", "Ações","FIIS"])
        self.combobox2.place(x=15, y=260, width=160, height=28)

        self.entry3 = tk.Entry(root)
        self.entry3.place(x=200, y=260, width=120, height=30)

        self.dateentry2 = DateEntry(root, date_pattern="yyyy-mm-dd")
        self.dateentry2.place(x=360, y=259, width=130, height=28)

        self.label6 = tk.Label(root, text="Tipo de Investimento")
        self.label6.place(x=30, y=229, width=130, height=30)

        self.label7 = tk.Label(root, text="Valor Investido")
        self.label7.place(x=215, y=229, width=90, height=26)

        self.label8 = tk.Label(root, text="Dia")
        self.label8.place(x=380, y=229, width=90, height=26)

        self.button1 = tk.Button(root, text="Salvar", command=self.on_button1)
        self.button1.place(x=312, y=330, width=96, height=32)

        self.button2 = tk.Button(root, text="Limpar", command=self.on_button2)
        self.button2.place(x=415, y=330, width=96, height=32)

        self.label9_alertas1 = tk.Label(root, text="")
        self.label9_alertas1.place(x=15, y=140, width=210, height=30)

        self.label10_alertas2 = tk.Label(root, text="")
        self.label10_alertas2.place(x=20, y=332, width=210, height=30)

    def salvamento(self):
        pass
    def on_button1(self):
        self.salvamento()
        
    def on_button2(self):
        self.entry2.delete(0,tk.END)
        self.entry3.delete(0,tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
