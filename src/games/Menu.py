import RoletaV1 as r

import tkinter as tk
from tkinter import simpledialog, messagebox

class RoletaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roleta Online")
        self.conta = 10

        self.login_frame()

    def login_frame(self):
        self.clear()
        tk.Label(self.root, text="Login:").pack()
        self.entry_login = tk.Entry(self.root)
        self.entry_login.pack()

        tk.Label(self.root, text="Senha:").pack()
        self.entry_senha = tk.Entry(self.root, show="*")
        self.entry_senha.pack()

        tk.Button(self.root, text="Entrar", command=self.menu_principal).pack(pady=10)

    def menu_principal(self):
        user = self.entry_login.get()
        senha = self.entry_senha.get()
        self.clear()

        # Aqui poderia haver uma verificação real
        if user and senha:
            tk.Label(self.root, text="ROLETA ONLINE", font=("Helvetica", 14, "bold")).pack(pady=10)
            self.label_saldo = tk.Label(self.root, text=f"Conta: R$ {self.conta}")
            self.label_saldo.pack()

            tk.Button(self.root, text="1. Jogar", width=20, command=self.jogar).pack(pady=5)
            tk.Button(self.root, text="2. Adicionar fundos", width=20, command=self.adicionar_fundos).pack(pady=5)
            tk.Button(self.root, text="3. Sair", width=20, command=self.root.quit).pack(pady=5)
        else:
            messagebox.showerror("Erro", "Login ou senha inválidos")

    def jogar(self):
        self.conta = r.Game(self.conta)
        self.atualizar_saldo()

    def adicionar_fundos(self):
        try:
            valor = simpledialog.askinteger("Adicionar Fundos", "Valor a adicionar:")
            if valor and valor > 0:
                self.conta += valor
                self.atualizar_saldo()
                messagebox.showinfo("Fundos adicionados", f"Novo saldo: R$ {self.conta}")
        except:
            messagebox.showerror("Erro", "Entrada inválida")

    def atualizar_saldo(self):
        self.label_saldo.config(text=f"Conta: R$ {self.conta}")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = RoletaApp(root)
    root.mainloop()


