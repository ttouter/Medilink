import os
import sys

#rutas del sistema
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

assets_dir = os.path.join(base_dir,"assets")
images_dir = os.path.join(assets_dir, "images")
icons_dir = os.path.join(assets_dir, "icons")
sounds_dir = os.path.join(assets_dir, "sounds")

db_dir = os.path.join(base_dir, "database")
db_path = os.path.join(db_dir, "medilink_data.db")

#constantes
app_name = "MediLink - Sistema de Gestión Médica"
tax_rate = 0.16

# colores del tema (Solo Modo Oscuro)
color_primary = "#0288D1"
color_secondary = "#0097A7"
color_background = "#121212" 
color_surface = "#1E1E1E"    
color_text_main = "#E0E0E0"  
color_text_muted = "#A0A0A0" 
color_success = "#4CAF50"    
color_danger = "#EF5350"     

#tipografia
font_main = ("Segoe UI", 14)
font_heading = ("Segoe UI", 24, "bold")
font_subheading = ("Segoe UI", 18, "bold")