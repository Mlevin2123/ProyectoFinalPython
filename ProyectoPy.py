import tkinter as tk
from tkinter import ttk, messagebox, Menu
import csv

class LibretaContactosApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Libreta de Contactos V2.0')
        self.root.configure(bg="#53CDB8")
        self.root.geometry("+350+80")
        self.root.resizable(0, 0)
        
        # Menú principal
        menu = Menu(self.root)
        self.root.config(menu=menu)
        archivo_menu = Menu(menu, tearoff=0, bg="#FFBB20")
        archivo_menu.add_command(label="Mostrar todos los contactos", command=self.mostrar_contactos)
        archivo_menu.add_command(label="Cerrar", command=self.root.quit)
        menu.add_cascade(label="Menú", menu=archivo_menu)
        
        # Marco de entrada de datos
        entrada_frame = tk.LabelFrame(self.root, bg="#53CDB8")
        entrada_frame.grid(row=0, column=0)
        
        tk.Label(entrada_frame, text='Nombre', bg="#53CDB8").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(entrada_frame, width=25)
        self.nombre_entry.grid(row=1, column=0)
        
        tk.Label(entrada_frame, text='Teléfono', bg="#53CDB8").grid(row=0, column=1)
        self.telefono_entry = tk.Entry(entrada_frame, width=20)
        self.telefono_entry.grid(row=1, column=1)
        
        tk.Label(entrada_frame, text='Correo', bg="#53CDB8").grid(row=0, column=2)
        self.correo_entry = tk.Entry(entrada_frame, width=25)
        self.correo_entry.grid(row=1, column=2)
        
        # Botones de acciones
        acciones_frame = tk.LabelFrame(self.root, bg="#53CDB8")
        acciones_frame.grid(row=2, column=0, pady=5)
        
        tk.Button(acciones_frame, text="Agregar Contacto", command=self.agregar_contacto, bg="#FFBB20").grid(row=0, column=0, padx=2)
        tk.Button(acciones_frame, text="Buscar Contacto", command=self.buscar_contacto, bg="#FFBB20").grid(row=0, column=1, padx=2)
        tk.Button(acciones_frame, text="Eliminar Contacto", command=self.eliminar_contacto, bg="#F26262").grid(row=0, column=2, padx=2)
        
        # Tabla de contactos
        self.tabla = ttk.Treeview(self.root, columns=("Teléfono", "Correo"), height=15)
        self.tabla.grid(row=4, column=0, padx=10, pady=10)
        self.tabla.heading("#0", text="Nombre")
        self.tabla.heading("Teléfono", text="Teléfono")
        self.tabla.heading("Correo", text="Correo")
        
        # Scroll para la tabla
        scrollbar_y = tk.Scrollbar(self.root, orient="vertical", command=self.tabla.yview)
        scrollbar_y.grid(row=4, column=1, sticky="ns")
        self.tabla.configure(yscroll=scrollbar_y.set)

    def agregar_contacto(self):
        nombre, telefono, correo = self.nombre_entry.get(), self.telefono_entry.get(), self.correo_entry.get()
        if not nombre or not telefono or not correo:
            messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos")
            return
        with open("libreta_contactos.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow((nombre, telefono, correo))
        self.tabla.insert("", "end", text=nombre, values=(telefono, correo))
        self.limpiar_entradas()

    def buscar_contacto(self):
        nombre = self.nombre_entry.get()
        encontrado = False
        for item in self.tabla.get_children():
            if self.tabla.item(item, "text") == nombre:
                self.tabla.selection_set(item)
                encontrado = True
                break
        if not encontrado:
            messagebox.showinfo("Contacto no encontrado", f"No se encontró el contacto '{nombre}'")

    def eliminar_contacto(self):
        nombre = self.nombre_entry.get()
        if not nombre:
            messagebox.showwarning("Campo vacío", "Por favor, ingrese el nombre del contacto a eliminar.")
            return
            
        confirmar = messagebox.askyesno("Eliminar Contacto", f"¿Eliminar el contacto '{nombre}'?")
        if confirmar:
            try:
                contactos_actuales = []
                with open("libreta_contactos.csv", "r", newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row and row[0].lower() != nombre.lower():  # Verifica que la fila no esté vacía y no sea el contacto a eliminar
                            contactos_actuales.append(row)

                with open("libreta_contactos.csv", "w", newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerows(contactos_actuales)

                self.mostrar_contactos()
                messagebox.showinfo("Contacto eliminado", f"El contacto '{nombre}' ha sido eliminado.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar el contacto: {e}")

    def mostrar_contactos(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        try:
            with open("libreta_contactos.csv", "r", newline='', encoding='utf-8') as f:
                for nombre, telefono, correo in csv.reader(f):
                    self.tabla.insert("", "end", text=nombre, values=(telefono, correo))
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo 'libreta_contactos.csv' no fue encontrado.")

    def limpiar_entradas(self):
        self.nombre_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.correo_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibretaContactosApp(root)
    root.mainloop()
