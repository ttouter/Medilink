import customtkinter as ctk
import sys
import os

# Asegurar que Python encuentre la carpeta de configuración y otras carpetas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui import config # Suponiendo que guardaste las variables en config/config.py

class MediLinkApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- 1. Configuración de la Ventana Principal ---
        self.title(config.app_name)
        self.geometry("1024x720") # Un tamaño estándar para pantallas de escritorio
        self.minsize(800, 600)
        self.configure(fg_color=config.color_background)

        # Configurar el grid principal (1 fila, 2 columnas)
        # Columna 0: Menú lateral (no se expande) | Columna 1: Área de trabajo (se expande)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- 2. Inicializar la Interfaz ---
        self.crear_sidebar()
        self.crear_area_principal()

    def crear_sidebar(self):
        """Crea el panel de navegación izquierdo."""
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=config.color_surface)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1) # Empuja los elementos hacia arriba

        # Logo / Título de la Clínica
        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text=config.app_name, 
            font=config.font_heading,
            text_color=config.color_primary
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        # Botones de Navegación
        self.btn_inicio = self.crear_boton_menu("Inicio", row=1)
        self.btn_pacientes = self.crear_boton_menu("Pacientes", row=2)
        self.btn_citas = self.crear_boton_menu("Agenda y Citas", row=3)
        self.btn_recetas = self.crear_boton_menu("Recetas", row=4)

        # Botón de Salir (al fondo)
        self.btn_salir = ctk.CTkButton(
            self.sidebar_frame, 
            text="Salir", 
            fg_color="transparent", 
            text_color=config.color_danger,
            hover_color="#ffebee",
            font=config.font_main,
            command=self.destroy
        )
        self.btn_salir.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def crear_boton_menu(self, texto, row):
        """Función auxiliar para crear botones del menú con el mismo estilo."""
        btn = ctk.CTkButton(
            self.sidebar_frame,
            text=texto,
            fg_color="transparent",
            text_color=config.color_text_main,
            hover_color=config.color_background,
            font=config.font_main,
            anchor="w", # Alinear texto a la izquierda
            height=40
        )
        btn.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        return btn

    def crear_area_principal(self):
        """Crea el contenedor derecho donde se mostrará el contenido de cada módulo."""
        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color=config.color_surface)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Etiqueta de bienvenida temporal (esto luego será reemplazado por las vistas reales)
        self.lbl_bienvenida = ctk.CTkLabel(
            self.main_frame,
            text="Bienvenido al Sistema de Gestión",
            font=config.font_subheading,
            text_color=config.color_text_muted
        )
        self.lbl_bienvenida.pack(expand=True)

if __name__ == "__main__":
    # Configuración global del tema visual
    ctk.set_appearance_mode("Light") # Los sistemas médicos suelen usar temas claros
    
    app = MediLinkApp()
    app.mainloop()