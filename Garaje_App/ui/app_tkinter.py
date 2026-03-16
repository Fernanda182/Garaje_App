import tkinter as tk
from tkinter import ttk, messagebox

from modelos.vehiculo import Vehiculo
from servicios.garaje_servicio import GarajeServicio


class AppGaraje:
    """
    Interfaz gráfica del sistema básico de gestión de garaje.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Básico de Gestión de Garaje")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.garaje_servicio = GarajeServicio()

        self.crear_widgets()

    def crear_widgets(self):
        """
        Crea todos los componentes de la interfaz gráfica.
        """
        titulo = tk.Label(
            self.root,
            text="Sistema Básico de Gestión de Garaje",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=15)

        frame_formulario = tk.Frame(self.root)
        frame_formulario.pack(pady=10)

        tk.Label(frame_formulario, text="Placa:", font=("Arial", 12)).grid(
            row=0, column=0, padx=10, pady=8, sticky="e"
        )
        self.entry_placa = tk.Entry(frame_formulario, width=30, font=("Arial", 11))
        self.entry_placa.grid(row=0, column=1, padx=10, pady=8)

        tk.Label(frame_formulario, text="Marca:", font=("Arial", 12)).grid(
            row=1, column=0, padx=10, pady=8, sticky="e"
        )
        self.entry_marca = tk.Entry(frame_formulario, width=30, font=("Arial", 11))
        self.entry_marca.grid(row=1, column=1, padx=10, pady=8)

        tk.Label(frame_formulario, text="Propietario:", font=("Arial", 12)).grid(
            row=2, column=0, padx=10, pady=8, sticky="e"
        )
        self.entry_propietario = tk.Entry(frame_formulario, width=30, font=("Arial", 11))
        self.entry_propietario.grid(row=2, column=1, padx=10, pady=8)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(
            frame_botones,
            text="Agregar vehículo",
            width=18,
            font=("Arial", 11),
            command=self.agregar_vehiculo
        )
        btn_agregar.grid(row=0, column=0, padx=10)

        btn_limpiar = tk.Button(
            frame_botones,
            text="Limpiar",
            width=18,
            font=("Arial", 11),
            command=self.limpiar_campos
        )
        btn_limpiar.grid(row=0, column=1, padx=10)

        frame_tabla = tk.Frame(self.root)
        frame_tabla.pack(pady=20)

        columnas = ("placa", "marca", "propietario")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)

        self.tree.heading("placa", text="Placa")
        self.tree.heading("marca", text="Marca")
        self.tree.heading("propietario", text="Propietario")

        self.tree.column("placa", width=150, anchor="center")
        self.tree.column("marca", width=150, anchor="center")
        self.tree.column("propietario", width=250, anchor="center")

        self.tree.pack()

    def agregar_vehiculo(self):
        """
        Agrega un vehículo al sistema y lo muestra en la tabla.
        """
        placa = self.entry_placa.get().strip()
        marca = self.entry_marca.get().strip()
        propietario = self.entry_propietario.get().strip()

        if not placa or not marca or not propietario:
            messagebox.showwarning(
                "Campos incompletos",
                "Por favor, complete todos los campos."
            )
            return

        vehiculo = Vehiculo(placa, marca, propietario)
        self.garaje_servicio.agregar_vehiculo(vehiculo)

        self.tree.insert("", tk.END, values=vehiculo.to_list())

        messagebox.showinfo("Registro exitoso", "Vehículo agregado correctamente.")

        self.limpiar_campos()

    def limpiar_campos(self):
        """
        Limpia los campos del formulario.
        """
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)
        self.entry_placa.focus()