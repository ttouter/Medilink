import customtkinter as ctk
import sys
import os

# Asegurar que Python encuentre la carpeta de configuración y otras carpetas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from ui import config
except ImportError:
    import config

class MediLinkApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- 1. Configuración de la Ventana Principal ---
        self.title(config.app_name)
        self.geometry("1024x720") # Un tamaño estándar para pantallas de escritorio
        self.minsize(800, 600)
        self.configure(fg_color=config.color_background)

        # Configurar el grid principal (1 fila, 2 columnas)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- 2. Inicializar la Interfaz ---
        self.crear_sidebar()
        self.crear_area_principal()
        
        # Mostrar la vista inicial por defecto
        self.mostrar_inicio()

    def crear_sidebar(self):
        """Crea el panel de navegación izquierdo."""
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=config.color_surface)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1) # Empuja los elementos de abajo hacia el fondo

        # Logo / Título de la Clínica
        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text=config.app_name.split(" - ")[0], # Solo muestra "MediLink"
            font=config.font_heading,
            text_color=config.color_primary
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        # Botones de Navegación con sus comandos asignados
        self.btn_inicio = self.crear_boton_menu("Inicio", row=1, comando=self.mostrar_inicio)
        self.btn_pacientes = self.crear_boton_menu("Pacientes", row=2, comando=self.mostrar_pacientes)
        self.btn_citas = self.crear_boton_menu("Agenda y Citas", row=3, comando=self.mostrar_citas)
        self.btn_recetas = self.crear_boton_menu("Recetas", row=4, comando=self.mostrar_inicio) # Placeholder

        # Botón de Salir (al fondo)
        self.btn_salir = ctk.CTkButton(
            self.sidebar_frame, 
            text="Salir", 
            fg_color="transparent", 
            text_color=config.color_danger,
            hover_color=config.color_background,
            font=config.font_main,
            command=self.destroy
        )
        self.btn_salir.grid(row=7, column=0, padx=20, pady=(0, 20), sticky="s")

    def crear_boton_menu(self, texto, row, comando=None):
        """Función auxiliar para crear botones del menú con el mismo estilo."""
        btn = ctk.CTkButton(
            self.sidebar_frame,
            text=texto,
            fg_color="transparent",
            text_color=config.color_text_main,
            hover_color=config.color_background,
            font=config.font_main,
            anchor="w", # Alinear texto a la izquierda
            height=40,
            command=comando
        )
        btn.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        return btn

    def crear_area_principal(self):
        """Crea el contenedor derecho donde se mostrará el contenido."""
        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color=config.color_surface)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    def limpiar_area_principal(self):
        """Destruye todos los widgets dentro del área principal para cargar una nueva vista."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # --- VISTAS DE LOS MÓDULOS ---

    def mostrar_inicio(self):
        """Vista de Inicio."""
        self.limpiar_area_principal()
        lbl_bienvenida = ctk.CTkLabel(
            self.main_frame,
            text="Bienvenido al Sistema de Gestión",
            font=config.font_heading,
            text_color=config.color_text_main
        )
        lbl_bienvenida.pack(expand=True)

    def mostrar_pacientes(self):
        """Vista del Historial de Pacientes."""
        self.limpiar_area_principal()
        
        # Título
        lbl_titulo = ctk.CTkLabel(self.main_frame, text="Historial de Pacientes", font=config.font_heading, text_color=config.color_text_main)
        lbl_titulo.pack(pady=(20, 10), padx=20, anchor="w")

        # Barra de búsqueda
        search_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=10)
        
        entry_search = ctk.CTkEntry(search_frame, placeholder_text="Buscar por nombre, apellido o ID...", font=config.font_main)
        entry_search.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        btn_search = ctk.CTkButton(search_frame, text="Buscar", font=config.font_main, fg_color=config.color_primary)
        btn_search.pack(side="right")

        # Contenedor desplazable (Scrollable Frame) para el historial
        history_frame = ctk.CTkScrollableFrame(self.main_frame, label_text="Últimas Consultas", label_font=config.font_subheading)
        history_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Datos de prueba (Aquí luego conectarías tu base de datos SQlite)
        datos_prueba = [
            {"fecha": "03/03/2026", "paciente": "Juan Pérez", "motivo": "Revisión General", "estado": "Completado"},
            {"fecha": "28/02/2026", "paciente": "María García", "motivo": "Dolor de cabeza crónico", "estado": "Pendiente de Análisis"},
            {"fecha": "15/02/2026", "paciente": "Carlos López", "motivo": "Consulta de seguimiento", "estado": "Completado"},
            {"fecha": "10/01/2026", "paciente": "Ana Martínez", "motivo": "Certificado médico", "estado": "Completado"},
        ]

        for dato in datos_prueba:
            card = ctk.CTkFrame(history_frame, corner_radius=5)
            card.pack(fill="x", pady=5, padx=5)
            
            texto_historial = f"{dato['fecha']} | {dato['paciente']} | Motivo: {dato['motivo']} | Estado: {dato['estado']}"
            lbl_card = ctk.CTkLabel(card, text=texto_historial, font=config.font_main, text_color=config.color_text_main)
            lbl_card.pack(side="left", padx=10, pady=10)
            
            btn_ver = ctk.CTkButton(card, text="Ver Detalles", width=100, fg_color=config.color_secondary)
            btn_ver.pack(side="right", padx=10, pady=10)

    def mostrar_citas(self):
        """Vista para Agendar Citas."""
        self.limpiar_area_principal()

        # Título
        lbl_titulo = ctk.CTkLabel(self.main_frame, text="Agendar Nueva Cita", font=config.font_heading, text_color=config.color_text_main)
        lbl_titulo.pack(pady=(20, 20), padx=20, anchor="w")

        # Contenedor del Formulario
        form_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        form_frame.pack(fill="both", expand=True, padx=40)

        # Configurar grid del formulario para centrar
        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=3)

        # Campos del formulario
        ctk.CTkLabel(form_frame, text="Nombre del Paciente:", font=config.font_main, text_color=config.color_text_main).grid(row=0, column=0, pady=15, sticky="e")
        ctk.CTkEntry(form_frame, width=300, font=config.font_main).grid(row=0, column=1, pady=15, padx=20, sticky="w")

        ctk.CTkLabel(form_frame, text="Fecha (DD/MM/AAAA):", font=config.font_main, text_color=config.color_text_main).grid(row=1, column=0, pady=15, sticky="e")
        ctk.CTkEntry(form_frame, width=300, font=config.font_main, placeholder_text="Ej: 15/04/2026").grid(row=1, column=1, pady=15, padx=20, sticky="w")

        ctk.CTkLabel(form_frame, text="Hora:", font=config.font_main, text_color=config.color_text_main).grid(row=2, column=0, pady=15, sticky="e")
        ctk.CTkEntry(form_frame, width=300, font=config.font_main, placeholder_text="Ej: 14:30").grid(row=2, column=1, pady=15, padx=20, sticky="w")

        ctk.CTkLabel(form_frame, text="Motivo de la Cita:", font=config.font_main, text_color=config.color_text_main).grid(row=3, column=0, pady=15, sticky="ne")
        textbox_motivo = ctk.CTkTextbox(form_frame, width=300, height=100, font=config.font_main)
        textbox_motivo.grid(row=3, column=1, pady=15, padx=20, sticky="w")

        # Botón para guardar
        btn_agendar = ctk.CTkButton(
            form_frame, 
            text="Agendar Cita", 
            font=config.font_subheading, 
            fg_color=config.color_success,
            height=40
        )
        btn_agendar.grid(row=4, column=0, columnspan=2, pady=40)


if __name__ == "__main__":
    # Configuración global inicial forzada a modo oscuro
    ctk.set_appearance_mode("Dark") 
    
    app = MediLinkApp()
    app.mainloop()