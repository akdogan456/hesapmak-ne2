import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        # Ayarları yapılandırma
        root.title("Hesap Makinesi.FARUK")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.current_input = ""  # Hesaplama için geçici değişken
        self.previous_input = ""  # Önceki doğru girdi (geri alma için)

        # Giriş ekranı (input display)
        self.entry = tk.Entry(root, font=('Times', 24), width=15, borderwidth=2, relief="solid", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Butonlar ve fonksiyonlar
        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('0', 4, 0), ('+', 1, 3), ('-', 2, 3),
            ('x', 3, 3), ('/', 4, 3), ('=', 4, 2),
            ('C', 5, 0), ('G', 4, 1)  # Undo butonunu "G" olarak değiştirdik ve 0 butonunun sağına koyduk
        ]

        # Butonları ekleyelim
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=('Times', 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'C':
            self.current_input = ""  # Temizle
            self.entry.delete(0, tk.END)
        elif char == 'G':
            # Önceki doğru değeri geri yükle (G İŞLEMİ)
            self.current_input = self.previous_input
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.current_input)
        elif char == '=':
            try:
                # Hesaplama
                result = eval(self.current_input.replace('x', '*').replace('/', '/'))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.previous_input = self.current_input  # En son doğru girdi
                self.current_input = str(result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Hata")
                self.previous_input = self.current_input  # Hata durumunda önceki değeri kaydet
                self.current_input = ""
        else:
            # Sayı veya işlem sembolü ekle
            self.previous_input = self.current_input  # Mevcut değeri önceki değere kaydet
            self.current_input += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()