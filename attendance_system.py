import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import csv
import os
from datetime import datetime
import hashlib
import re
from ttkthemes import ThemedTk
import time
import shutil
import math
from tkcalendar import DateEntry

# Constantes
CONFIG_FILE = "config.json"
USERS_FILE = "users.json"
ATTENDANCE_FILE = "attendance.json"
LANGUAGES_DIR = "languages"

os.makedirs(LANGUAGES_DIR, exist_ok=True)

# Diccionarios de idiomas
LANGUAGES = {
    "es": {
        "app_title": "Sistema de Gestión de Asistencia",
        "login": "Iniciar Sesión",
        "username": "Usuario",
        "password": "Contraseña",
        "login_button": "Iniciar Sesión",
        "admin_panel": "Panel de Administrador",
        "teacher_panel": "Panel de Profesor",
        "student_panel": "Panel de Estudiante",
        "logout": "Cerrar Sesión",
        "user_management": "Gestión de Usuarios",
        "attendance_management": "Gestión de Asistencia",
        "reports": "Reportes",
        "create_user": "Crear Usuario",
        "role": "Rol",
        "create_user_button": "Crear Usuario",
        "user_list": "Lista de Usuarios",
        "date": "Fecha",
        "view_attendance": "Ver Asistencia",
        "edit_attendance": "Editar Asistencia",
        "export_data": "Exportar Datos",
        "export_csv": "Exportar a CSV",
        "statistics": "Estadísticas",
        "generate_statistics": "Generar Estadísticas",
        "student": "Estudiante",
        "status": "Estado",
        "present": "Presente",
        "absent": "Ausente",
        "late": "Tardanza",
        "record_attendance": "Registrar Asistencia",
        "my_attendance": "Mi Asistencia",
        "view_history": "Ver Mi Historial de Asistencia",
        "my_statistics": "Mis Estadísticas",
        "initial_setup": "Configuración Inicial",
        "setup_system": "Configurar Sistema",
        "create_admin": "Crear Administrador",
        "preferences": "Preferencias",
        "language": "Idioma",
        "theme": "Tema",
        "finish_setup": "Finalizar Configuración",
        "error": "Error",
        "success": "Éxito",
        "info": "Información",
        "complete_fields": "Por favor complete todos los campos",
        "invalid_username": "El nombre de usuario solo puede contener letras, números y guiones bajos",
        "password_length": "La contraseña debe tener al menos 6 caracteres",
        "user_created": "Usuario creado exitosamente",
        "user_exists": "El nombre de usuario ya existe",
        "invalid_credentials": "Usuario o contraseña incorrectos",
        "invalid_date": "Formato de fecha inválido. Use YYYY-MM-DD",
        "no_records": "No hay registros para esta fecha",
        "select_record": "Por favor seleccione un registro para editar",
        "record_updated": "Registro actualizado correctamente",
        "update_failed": "No se pudo actualizar el registro",
        "export_success": "Exportación exitosa",
        "export_failed": "Error al exportar",
        "no_attendance_data": "No hay datos de asistencia para generar estadísticas",
        "total_days": "Total de días registrados",
        "total_students": "Total de estudiantes",
        "student_statistics": "Estadísticas por estudiante",
        "present_days": "Días presente",
        "absent_days": "Días ausente",
        "late_days": "Días con tardanza",
        "attendance_rate": "Tasa de asistencia",
        "cancel": "Cancelar",
        "save": "Guardar",
        "light": "Claro",
        "dark": "Oscuro",
        "setup_completed": "Configuración completada correctamente",
        "complete_admin_fields": "Por favor complete todos los campos del administrador",
        "save_as_csv": "Guardar como CSV",
        "csv_files": "Archivos CSV",
        "all_files": "Todos los archivos",
        "welcome": "Bienvenido al Sistema de Gestión de Asistencia",
        "welcome_message": "Este sistema le permite gestionar la asistencia de estudiantes de manera eficiente.",
        "dashboard": "Tablero",
        "settings": "Configuración",
        "profile": "Perfil",
        "help": "Ayuda",
        "about": "Acerca de",
        "search": "Buscar...",
        "filter": "Filtrar",
        "sort": "Ordenar",
        "refresh": "Actualizar",
        "add": "Añadir",
        "edit": "Editar",
        "delete": "Eliminar",
        "confirm": "Confirmar",
        "cancel": "Cancelar",
        "loading": "Cargando...",
        "no_data": "No hay datos disponibles",
        "select_date": "Seleccione una fecha",
        "select_student": "Seleccione un estudiante",
        "select_status": "Seleccione un estado",
        "select_role": "Seleccione un rol",
        "select_theme": "Seleccione un tema",
        "select_language": "Seleccione un idioma",
        "admin": "Administrador",
        "teacher": "Profesor",
        "student": "Estudiante",
        "change_password": "Cambiar contraseña",
        "current_password": "Contraseña actual",
        "new_password": "Nueva contraseña",
        "confirm_password": "Confirmar contraseña",
        "passwords_not_match": "Las contraseñas no coinciden",
        "password_changed": "Contraseña cambiada exitosamente",
        "change_password_failed": "No se pudo cambiar la contraseña",
        "confirm_delete": "¿Está seguro de que desea eliminar este usuario?",
        "delete_success": "Usuario eliminado exitosamente",
        "delete_failed": "No se pudo eliminar el usuario",
        "confirm_logout": "¿Está seguro de que desea cerrar sesión?",
        "yes": "Sí",
        "no": "No",
        "welcome_back": "Bienvenido de nuevo",
        "today": "Hoy",
        "yesterday": "Ayer",
        "this_week": "Esta semana",
        "this_month": "Este mes",
        "custom_range": "Rango personalizado",
        "from_date": "Desde",
        "to_date": "Hasta",
        "apply": "Aplicar",
        "reset": "Restablecer",
        "summary": "Resumen",
        "details": "Detalles",
        "chart": "Gráfico",
        "table": "Tabla",
        "print": "Imprimir",
        "download": "Descargar",
        "share": "Compartir",
        "fullscreen": "Pantalla completa",
        "exit_fullscreen": "Salir de pantalla completa",
        "zoom_in": "Acercar",
        "zoom_out": "Alejar",
        "fit": "Ajustar",
        "original": "Original",
        "next": "Siguiente",
        "previous": "Anterior",
        "first": "Primero",
        "last": "Último",
        "page": "Página",
        "of": "de",
        "items_per_page": "Elementos por página",
        "showing": "Mostrando",
        "to": "a",
        "of_total": "de un total de",
        "items": "elementos",
        "no_results": "No se encontraron resultados",
        "search_results": "Resultados de búsqueda",
        "search_no_results": "La búsqueda no arrojó resultados",
        "clear_search": "Limpiar búsqueda",
        "advanced_search": "Búsqueda avanzada",
        "search_by": "Buscar por",
        "search_in": "Buscar en",
        "match_case": "Coincidir mayúsculas y minúsculas",
        "match_whole_word": "Coincidir palabra completa",
        "match_regex": "Usar expresión regular",
        "search_options": "Opciones de búsqueda",
        "search_history": "Historial de búsqueda",
        "clear_history": "Limpiar historial",
        "save_search": "Guardar búsqueda",
        "saved_searches": "Búsquedas guardadas",
        "delete_search": "Eliminar búsqueda",
        "search_name": "Nombre de la búsqueda",
        "save": "Guardar",
        "cancel": "Cancelar",
        "ok": "Aceptar",
        "apply": "Aplicar",
        "reset": "Restablecer",
        "close": "Cerrar",
        "back": "Atrás",
        "next": "Siguiente",
        "finish": "Finalizar",
        "skip": "Omitir",
        "continue": "Continuar",
        "retry": "Reintentar",
        "ignore": "Ignorar",
        "abort": "Abortar",
        "help": "Ayuda",
        "about": "Acerca de",
        "version": "Versión",
        "build": "Compilación",
        "copyright": "Derechos de autor",
        "license": "Licencia",
        "website": "Sitio web",
        "contact": "Contacto",
        "email": "Correo electrónico",
        "phone": "Teléfono",
        "address": "Dirección",
        "social": "Redes sociales",
        "follow_us": "Síguenos",
        "like_us": "Danos me gusta",
        "share_us": "Compártenos",
        "subscribe": "Suscríbete",
        "unsubscribe": "Cancelar suscripción",
        "notifications": "Notificaciones",
        "enable_notifications": "Habilitar notificaciones",
        "disable_notifications": "Deshabilitar notificaciones",
        "notification_settings": "Configuración de notificaciones",
        "sound": "Sonido",
        "vibration": "Vibración",
        "popup": "Ventana emergente",
        "badge": "Insignia",
        "led": "LED",
        "priority": "Prioridad",
        "high": "Alta",
        "medium": "Media",
        "low": "Baja",
        "normal": "Normal",
        "urgent": "Urgente",
        "not_urgent": "No urgente",
        "important": "Importante",
        "not_important": "No importante",
        "critical": "Crítico",
        "not_critical": "No crítico",
        "emergency": "Emergencia",
        "not_emergency": "No emergencia",
        "alert": "Alerta",
        "warning": "Advertencia",
        "info": "Información",
        "debug": "Depuración",
        "trace": "Rastreo",
        "verbose": "Detallado",
        "silent": "Silencioso",
        "quiet": "Tranquilo",
        "loud": "Fuerte",
        "very_loud": "Muy fuerte",
        "mute": "Silenciar",
        "unmute": "Activar sonido",
        "volume": "Volumen",
        "brightness": "Brillo",
        "contrast": "Contraste",
        "saturation": "Saturación",
        "hue": "Tono",
        "gamma": "Gamma",
        "exposure": "Exposición",
        "sharpness": "Nitidez",
        "blur": "Desenfoque",
        "noise": "Ruido",
        "denoise": "Reducir ruido",
        "enhance": "Mejorar",
        "restore": "Restaurar",
        "reset": "Restablecer",
        "default": "Predeterminado",
        "custom": "Personalizado",
        "auto": "Automático",
        "manual": "Manual",
        "advanced": "Avanzado",
        "basic": "Básico",
        "simple": "Simple",
        "complex": "Complejo",
        "easy": "Fácil",
        "hard": "Difícil",
        "beginner": "Principiante",
        "intermediate": "Intermedio",
        "expert": "Experto",
        "master": "Maestro",
        "novice": "Novato",
        "professional": "Profesional",
        "amateur": "Aficionado",
        "home": "Inicio",
        "work": "Trabajo",
        "school": "Escuela",
        "university": "Universidad",
        "college": "Colegio",
        "academy": "Academia",
        "institute": "Instituto",
        "center": "Centro",
        "lab": "Laboratorio",
        "office": "Oficina",
        "classroom": "Aula",
        "library": "Biblioteca",
        "cafeteria": "Cafetería",
        "gym": "Gimnasio",
        "field": "Campo",
        "court": "Cancha",
        "pool": "Piscina",
        "track": "Pista",
        "stadium": "Estadio",
        "arena": "Arena",
        "hall": "Sala",
        "room": "Habitación",
        "building": "Edificio",
        "floor": "Piso",
        "level": "Nivel",
        "area": "Área",
        "zone": "Zona",
        "sector": "Sector",
        "region": "Región",
        "country": "País",
        "city": "Ciudad",
        "state": "Estado",
        "province": "Provincia",
        "county": "Condado",
        "district": "Distrito",
        "neighborhood": "Vecindario",
        "street": "Calle",
        "avenue": "Avenida",
        "boulevard": "Bulevar",
        "road": "Carretera",
        "highway": "Autopista",
        "path": "Camino",
        "trail": "Sendero",
        "route": "Ruta",
        "direction": "Dirección",
        "north": "Norte",
        "south": "Sur",
        "east": "Este",
        "west": "Oeste",
        "northeast": "Noreste",
        "northwest": "Noroeste",
        "southeast": "Sureste",
        "southwest": "Suroeste",
        "up": "Arriba",
        "down": "Abajo",
        "left": "Izquierda",
        "right": "Derecha",
        "center": "Centro",
        "middle": "Medio",
        "top": "Superior",
        "bottom": "Inferior",
        "front": "Frente",
        "back": "Atrás",
        "side": "Lado",
        "inside": "Dentro",
        "outside": "Fuera",
        "interior": "Interior",
        "exterior": "Exterior",
        "central": "Central",
        "peripheral": "Periférico",
        "main": "Principal",
        "secondary": "Secundario",
        "auxiliary": "Auxiliar",
        "primary": "Primario",
        "tertiary": "Terciario",
        "quaternary": "Cuaternario",
        "quinary": "Quinario",
        "senary": "Senario",
        "septenary": "Septenario",
        "octonary": "Octonario",
        "nonary": "Nonario",
        "denary": "Denario",
        "first": "Primero",
        "second": "Segundo",
        "third": "Tercero",
        "fourth": "Cuarto",
        "fifth": "Quinto",
        "sixth": "Sexto",
        "seventh": "Séptimo",
        "eighth": "Octavo",
        "ninth": "Noveno",
        "tenth": "Décimo",
    },
    "en": {
        "app_title": "Attendance Management System",
        "login": "Login",
        "username": "Username",
        "password": "Password",
        "login_button": "Login",
        "admin_panel": "Admin Panel",
        "teacher_panel": "Teacher Panel",
        "student_panel": "Student Panel",
        "logout": "Logout",
        "user_management": "User Management",
        "attendance_management": "Attendance Management",
        "reports": "Reports",
        "create_user": "Create User",
        "role": "Role",
        "create_user_button": "Create User",
        "user_list": "User List",
        "date": "Date",
        "view_attendance": "View Attendance",
        "edit_attendance": "Edit Attendance",
        "export_data": "Export Data",
        "export_csv": "Export to CSV",
        "statistics": "Statistics",
        "generate_statistics": "Generate Statistics",
        "student": "Student",
        "status": "Status",
        "present": "Present",
        "absent": "Absent",
        "late": "Late",
        "record_attendance": "Record Attendance",
        "my_attendance": "My Attendance",
        "view_history": "View My Attendance History",
        "my_statistics": "My Statistics",
        "initial_setup": "Initial Setup",
        "setup_system": "Setup System",
        "create_admin": "Create Admin",
        "preferences": "Preferences",
        "language": "Language",
        "theme": "Theme",
        "finish_setup": "Finish Setup",
        "error": "Error",
        "success": "Success",
        "info": "Information",
        "complete_fields": "Please complete all fields",
        "invalid_username": "Username can only contain letters, numbers, and underscores",
        "password_length": "Password must be at least 6 characters long",
        "user_created": "User created successfully",
        "user_exists": "Username already exists",
        "invalid_credentials": "Invalid username or password",
        "invalid_date": "Invalid date format. Use YYYY-MM-DD",
        "no_records": "No records for this date",
        "select_record": "Please select a record to edit",
        "record_updated": "Record updated successfully",
        "update_failed": "Failed to update record",
        "export_success": "Export successful",
        "export_failed": "Export failed",
        "no_attendance_data": "No attendance data to generate statistics",
        "total_days": "Total days recorded",
        "total_students": "Total students",
        "student_statistics": "Student statistics",
        "present_days": "Present days",
        "absent_days": "Absent days",
        "late_days": "Late days",
        "attendance_rate": "Attendance rate",
        "cancel": "Cancel",
        "save": "Save",
        "light": "Light",
        "dark": "Dark",
        "setup_completed": "Setup completed successfully",
        "complete_admin_fields": "Please complete all admin fields",
        "save_as_csv": "Save as CSV",
        "csv_files": "CSV files",
        "all_files": "All files",
        "welcome": "Welcome to the Attendance Management System",
        "welcome_message": "This system allows you to efficiently manage student attendance.",
        "dashboard": "Dashboard",
        "settings": "Settings",
        "profile": "Profile",
        "help": "Help",
        "about": "About",
        "search": "Search...",
        "filter": "Filter",
        "sort": "Sort",
        "refresh": "Refresh",
        "add": "Add",
        "edit": "Edit",
        "delete": "Delete",
        "confirm": "Confirm",
        "cancel": "Cancel",
        "loading": "Loading...",
        "no_data": "No data available",
        "select_date": "Select a date",
        "select_student": "Select a student",
        "select_status": "Select a status",
        "select_role": "Select a role",
        "select_theme": "Select a theme",
        "select_language": "Select a language",
        "admin": "Administrator",
        "teacher": "Teacher",
        "student": "Student",
        "change_password": "Change Password",
        "current_password": "Current Password",
        "new_password": "New Password",
        "confirm_password": "Confirm Password",
        "passwords_not_match": "Passwords do not match",
        "password_changed": "Password changed successfully",
        "change_password_failed": "Failed to change password",
        "confirm_delete": "Are you sure you want to delete this user?",
        "delete_success": "User deleted successfully",
        "delete_failed": "Failed to delete user",
        "confirm_logout": "Are you sure you want to log out?",
        "yes": "Yes",
        "no": "No",
        "welcome_back": "Welcome back",
        "today": "Today",
        "yesterday": "Yesterday",
        "this_week": "This week",
        "this_month": "This month",
        "custom_range": "Custom range",
        "from_date": "From",
        "to_date": "To",
        "apply": "Apply",
        "reset": "Reset",
        "summary": "Summary",
        "details": "Details",
        "chart": "Chart",
        "table": "Table",
        "print": "Print",
        "download": "Download",
        "share": "Share",
        "fullscreen": "Fullscreen",
        "exit_fullscreen": "Exit fullscreen",
        "zoom_in": "Zoom in",
        "zoom_out": "Zoom out",
        "fit": "Fit",
        "original": "Original",
        "next": "Next",
        "previous": "Previous",
        "first": "First",
        "last": "Last",
        "page": "Page",
        "of": "of",
        "items_per_page": "Items per page",
        "showing": "Showing",
        "to": "to",
        "of_total": "of",
        "items": "items",
        "no_results": "No results found",
        "search_results": "Search results",
        "search_no_results": "Your search returned no results",
        "clear_search": "Clear search",
        "advanced_search": "Advanced search",
        "search_by": "Search by",
        "search_in": "Search in",
        "match_case": "Match case",
        "match_whole_word": "Match whole word",
        "match_regex": "Use regular expression",
        "search_options": "Search options",
        "search_history": "Search history",
        "clear_history": "Clear history",
        "save_search": "Save search",
        "saved_searches": "Saved searches",
        "delete_search": "Delete search",
        "search_name": "Search name",
        "save": "Save",
        "cancel": "Cancel",
        "ok": "OK",
        "apply": "Apply",
        "reset": "Reset",
        "close": "Close",
        "back": "Back",
        "next": "Next",
        "finish": "Finish",
        "skip": "Skip",
        "continue": "Continue",
        "retry": "Retry",
        "ignore": "Ignore",
        "abort": "Abort",
        "help": "Help",
        "about": "About",
        "version": "Version",
        "build": "Build",
        "copyright": "Copyright",
        "license": "License",
        "website": "Website",
        "contact": "Contact",
        "email": "Email",
        "phone": "Phone",
        "address": "Address",
        "social": "Social",
        "follow_us": "Follow us",
        "like_us": "Like us",
        "share_us": "Share us",
        "subscribe": "Subscribe",
        "unsubscribe": "Unsubscribe",
        "notifications": "Notifications",
        "enable_notifications": "Enable notifications",
        "disable_notifications": "Disable notifications",
        "notification_settings": "Notification settings",
        "sound": "Sound",
        "vibration": "Vibration",
        "popup": "Popup",
        "badge": "Badge",
        "led": "LED",
        "priority": "Priority",
        "high": "High",
        "medium": "Medium",
        "low": "Low",
        "normal": "Normal",
        "urgent": "Urgent",
        "not_urgent": "Not urgent",
        "important": "Important",
        "not_important": "Not important",
        "critical": "Critical",
        "not_critical": "Not critical",
        "emergency": "Emergency",
        "not_emergency": "Not emergency",
        "alert": "Alert",
        "warning": "Warning",
        "info": "Information",
        "debug": "Debug",
        "trace": "Trace",
        "verbose": "Verbose",
        "silent": "Silent",
        "quiet": "Quiet",
        "loud": "Loud",
        "very_loud": "Very loud",
        "mute": "Mute",
        "unmute": "Unmute",
        "volume": "Volume",
        "brightness": "Brightness",
        "contrast": "Contrast",
        "saturation": "Saturation",
        "hue": "Hue",
        "gamma": "Gamma",
        "exposure": "Exposure",
        "sharpness": "Sharpness",
        "blur": "Blur",
        "noise": "Noise",
        "denoise": "Denoise",
        "enhance": "Enhance",
        "restore": "Restore",
        "reset": "Reset",
        "default": "Default",
        "custom": "Custom",
        "auto": "Auto",
        "manual": "Manual",
        "advanced": "Advanced",
        "basic": "Basic",
        "simple": "Simple",
        "complex": "Complex",
        "easy": "Easy",
        "hard": "Hard",
        "beginner": "Beginner",
        "intermediate": "Intermediate",
        "expert": "Expert",
        "master": "Master",
        "novice": "Novice",
        "professional": "Professional",
        "amateur": "Amateur",
        "home": "Home",
        "work": "Work",
        "school": "School",
        "university": "University",
        "college": "College",
        "academy": "Academy",
        "institute": "Institute",
        "center": "Center",
        "lab": "Lab",
        "office": "Office",
        "classroom": "Classroom",
        "library": "Library",
        "cafeteria": "Cafeteria",
        "gym": "Gym",
        "field": "Field",
        "court": "Court",
        "pool": "Pool",
        "track": "Track",
        "stadium": "Stadium",
        "arena": "Arena",
        "hall": "Hall",
        "room": "Room",
        "building": "Building",
        "floor": "Floor",
        "level": "Level",
        "area": "Area",
        "zone": "Zone",
        "sector": "Sector",
        "region": "Region",
        "country": "Country",
        "city": "City",
        "state": "State",
        "province": "Province",
        "county": "County",
        "district": "District",
        "neighborhood": "Neighborhood",
        "street": "Street",
        "avenue": "Avenue",
        "boulevard": "Boulevard",
        "road": "Road",
        "highway": "Highway",
        "path": "Path",
        "trail": "Trail",
        "route": "Route",
        "direction": "Direction",
        "north": "North",
        "south": "South",
        "east": "East",
        "west": "West",
        "northeast": "Northeast",
        "northwest": "Northwest",
        "southeast": "Southeast",
        "southwest": "Southwest",
        "up": "Up",
        "down": "Down",
        "left": "Left",
        "right": "Right",
        "center": "Center",
        "middle": "Middle",
        "top": "Top",
        "bottom": "Bottom",
        "front": "Front",
        "back": "Back",
        "side": "Side",
        "inside": "Inside",
        "outside": "Outside",
        "interior": "Interior",
        "exterior": "Exterior",
        "central": "Central",
        "peripheral": "Peripheral",
        "main": "Main",
        "secondary": "Secondary",
        "auxiliary": "Auxiliary",
        "primary": "Primary",
        "tertiary": "Tertiary",
        "quaternary": "Quaternary",
        "quinary": "Quinary",
        "senary": "Senary",
        "septenary": "Septenary",
        "octonary": "Octonary",
        "nonary": "Nonary",
        "denary": "Denary",
        "first": "First",
        "second": "Second",
        "third": "Third",
        "fourth": "Fourth",
        "fifth": "Fifth",
        "sixth": "Sixth",
        "seventh": "Seventh",
        "eighth": "Eighth",
        "ninth": "Ninth",
        "tenth": "Tenth",
    }
}

# ==========================================
# CONFIGURACIÓN INICIAL Y GESTIÓN DE USUARIOS
# ==========================================

# Guardar diccionarios de idiomas en archivos
for lang_code, translations in LANGUAGES.items():
    lang_file = os.path.join(LANGUAGES_DIR, f"{lang_code}.json")
    if not os.path.exists(lang_file):
        with open(lang_file, 'w', encoding='utf-8') as f:
            json.dump(translations, f, indent=4, ensure_ascii=False)

# Configuración inicial
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Configuración por defecto
        default_config = {
            "language": "es",
            "theme": "light",
            "admin_created": False
        }
        save_config(default_config)
        return default_config

def save_config(config):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

# Gestión de usuarios
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {"users": []}

def save_users(users_data):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users_data, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password, role):
    users_data = load_users()
    
    # Verificar si el usuario ya existe
    for user in users_data["users"]:
        if user["username"] == username:
            return False, "user_exists"
    
    # Crear nuevo usuario
    new_user = {
        "username": username,
        "password": hash_password(password),
        "role": role
    }
    
    users_data["users"].append(new_user)
    save_users(users_data)
    return True, "user_created"

def authenticate_user(username, password):
    users_data = load_users()
    
    for user in users_data["users"]:
        if user["username"] == username and user["password"] == hash_password(password):
            return True, user["role"]
    
    return False, None

# Gestión de asistencia
def load_attendance():
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {"attendance": {}}

def save_attendance(attendance_data):
    with open(ATTENDANCE_FILE, 'w', encoding='utf-8') as f:
        json.dump(attendance_data, f, indent=4)

def record_attendance(date, student_id, status):
    attendance_data = load_attendance()
    
    if date not in attendance_data["attendance"]:
        attendance_data["attendance"][date] = {}
    
    attendance_data["attendance"][date][student_id] = status
    save_attendance(attendance_data)
    return True

def edit_attendance(date, student_id, new_status):
    attendance_data = load_attendance()
    
    if date in attendance_data["attendance"] and student_id in attendance_data["attendance"][date]:
        attendance_data["attendance"][date][student_id] = new_status
        save_attendance(attendance_data)
        return True
    
    return False

def get_student_attendance(student_id):
    attendance_data = load_attendance()
    student_records = {}
    
    for date, records in attendance_data["attendance"].items():
        if student_id in records:
            student_records[date] = records[student_id]
    
    return student_records

def get_date_attendance(date):
    attendance_data = load_attendance()
    
    if date in attendance_data["attendance"]:
        return attendance_data["attendance"][date]
    
    return {}

def export_to_csv(filename):
    attendance_data = load_attendance()
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Obtener todos los estudiantes únicos
            all_students = set()
            for date_records in attendance_data["attendance"].values():
                all_students.update(date_records.keys())
            
            # Crear encabezados
            fieldnames = ['Fecha'] + list(all_students)
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            # Escribir datos
            for date, records in sorted(attendance_data["attendance"].items()):
                row = {'Fecha': date}
                for student in all_students:
                    row[student] = records.get(student, 'N/A')
                writer.writerow(row)
                
        return True, "export_success"
    except Exception as e:
        return False, f"export_failed: {str(e)}"

def load_justifications():
    if not os.path.exists("justifications.json"):
        return {"justifications": {}}
    with open("justifications.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_justifications(data):
    with open("justifications.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def submit_justification(date, student_id, reason, file_path=None):
    justifications = load_justifications()
    if date not in justifications["justifications"]:
        justifications["justifications"][date] = {}
    justifications["justifications"][date][student_id] = {
        "reason": reason,
        "status": "pending",
        "response": "",
        "attachment": file_path  
    }
    save_justifications(justifications)
    return True

def respond_justification(date, student_id, decision, response_message=""):
    justifications = load_justifications()
    if date in justifications["justifications"] and student_id in justifications["justifications"][date]:
        justifications["justifications"][date][student_id]["status"] = decision
        justifications["justifications"][date][student_id]["response"] = response_message
        save_justifications(justifications)
        return True
    return False

def get_pending_justifications():
    justifications = load_justifications()
    pending = []
    for date, records in justifications["justifications"].items():
        for student, info in records.items():
            if info["status"] == "pending":
                pending.append((date, student, info["reason"]))
    return pending

def get_justification_status(date, student_id):
    justifications = load_justifications()
    if date in justifications["justifications"] and student_id in justifications["justifications"][date]:
        return justifications["justifications"][date][student_id]
    return None
    
# ==========================================
# CONFIGURACIÓN DE IDIOMAS Y TEMAS
# ==========================================
class I18n:
    def __init__(self):
        self.config = load_config()
        self.current_language = self.config["language"]
        self.translations = self._load_translations()
        
    def _load_translations(self):
        lang_file = os.path.join(LANGUAGES_DIR, f"{self.current_language}.json")
        if os.path.exists(lang_file):
            with open(lang_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Si no existe el archivo, usar el diccionario predefinido
            return LANGUAGES.get(self.current_language, LANGUAGES["en"])
    
    def set_language(self, language_code):
        if language_code in LANGUAGES:
            self.current_language = language_code
            self.config["language"] = language_code
            save_config(self.config)
            self.translations = self._load_translations()
            return True
        return False
    
    def get(self, key, default=None):
        return self.translations.get(key, default if default is not None else key)

# Clase para manejar temas
class ThemeManager:
    def __init__(self, app):
        self.app = app
        self.config = load_config()
        self.current_theme = self.config["theme"]
        
        # Definir colores para temas
        self.themes = {
            "light": {
                "bg": "#f5f5f5",
                "fg": "#333333",
                "accent": "#3498db",
                "accent_hover": "#2980b9",
                "success": "#2ecc71",
                "warning": "#f39c12",
                "error": "#e74c3c",
                "card_bg": "#ffffff",
                "border": "#e0e0e0",
                "input_bg": "#ffffff",
                "input_fg": "#333333",
                "button_bg": "#3498db",
                "button_fg": "#ffffff",
                "button_hover_bg": "#2980b9",
                "button_hover_fg": "#ffffff",
                "header_bg": "#3498db",
                "header_fg": "#ffffff",
                "sidebar_bg": "#ffffff",
                "sidebar_fg": "#333333",
                "sidebar_hover": "#f0f0f0",
                "sidebar_active": "#e0e0e0",
                "table_header_bg": "#f0f0f0",
                "table_header_fg": "#333333",
                "table_row_odd": "#ffffff",
                "table_row_even": "#f9f9f9",
                "table_border": "#e0e0e0",
                "tooltip_bg": "#333333",
                "tooltip_fg": "#ffffff",
                "scrollbar_bg": "#f0f0f0",
                "scrollbar_thumb": "#c0c0c0",
                "scrollbar_hover": "#a0a0a0",
                "dialog_bg": "#ffffff",
                "dialog_fg": "#333333",
                "dialog_border": "#e0e0e0",
                "dialog_shadow": "rgba(0, 0, 0, 0.1)",
                "menu_bg": "#ffffff",
                "menu_fg": "#333333",
                "menu_hover": "#f0f0f0",
                "menu_border": "#e0e0e0",
                "menu_shadow": "rgba(0, 0, 0, 0.1)",
                "tab_bg": "#f0f0f0",
                "tab_fg": "#333333",
                "tab_active_bg": "#ffffff",
                "tab_active_fg": "#3498db",
                "tab_hover_bg": "#e0e0e0",
                "tab_hover_fg": "#333333",
                "tab_border": "#e0e0e0",
                "progress_bg": "#f0f0f0",
                "progress_fg": "#3498db",
                "slider_bg": "#f0f0f0",
                "slider_fg": "#3498db",
                "slider_handle": "#ffffff",
                "slider_handle_border": "#c0c0c0",
                "switch_bg": "#f0f0f0",
                "switch_fg": "#3498db",
                "switch_handle": "#ffffff",
                "switch_handle_border": "#c0c0c0",
                "checkbox_bg": "#ffffff",
                "checkbox_fg": "#3498db",
                "checkbox_border": "#c0c0c0",
                "radio_bg": "#ffffff",
                "radio_fg": "#3498db",
                "radio_border": "#c0c0c0",
                "calendar_bg": "#ffffff",
                "calendar_fg": "#333333",
                "calendar_header_bg": "#f0f0f0",
                "calendar_header_fg": "#333333",
                "calendar_weekend_bg": "#f9f9f9",
                "calendar_weekend_fg": "#333333",
                "calendar_today_bg": "#3498db",
                "calendar_today_fg": "#ffffff",
                "calendar_selected_bg": "#2980b9",
                "calendar_selected_fg": "#ffffff",
                "calendar_border": "#e0e0e0",
                "tooltip_bg": "#333333",
                "tooltip_fg": "#ffffff",
                "tooltip_border": "#000000",
                "tooltip_shadow": "rgba(0, 0, 0, 0.2)",
            },
            "dark": {
                "bg": "#121212",
                "fg": "#f5f5f5",
                "accent": "#3498db",
                "accent_hover": "#2980b9",
                "success": "#2ecc71",
                "warning": "#f39c12",
                "error": "#e74c3c",
                "card_bg": "#1e1e1e",
                "border": "#333333",
                "input_bg": "#2a2a2a",
                "input_fg": "#f5f5f5",
                "button_bg": "#3498db",
                "button_fg": "#ffffff",
                "button_hover_bg": "#2980b9",
                "button_hover_fg": "#ffffff",
                "header_bg": "#1a1a1a",
                "header_fg": "#f5f5f5",
                "sidebar_bg": "#1a1a1a",
                "sidebar_fg": "#f5f5f5",
                "sidebar_hover": "#2a2a2a",
                "sidebar_active": "#3a3a3a",
                "table_header_bg": "#2a2a2a",
                "table_header_fg": "#f5f5f5",
                "table_row_odd": "#1e1e1e",
                "table_row_even": "#262626",
                "table_border": "#333333",
                "tooltip_bg": "#f5f5f5",
                "tooltip_fg": "#121212",
                "scrollbar_bg": "#2a2a2a",
                "scrollbar_thumb": "#4a4a4a",
                "scrollbar_hover": "#5a5a5a",
                "dialog_bg": "#1e1e1e",
                "dialog_fg": "#f5f5f5",
                "dialog_border": "#333333",
                "dialog_shadow": "rgba(0, 0, 0, 0.3)",
                "menu_bg": "#1e1e1e",
                "menu_fg": "#f5f5f5",
                "menu_hover": "#2a2a2a",
                "menu_border": "#333333",
                "menu_shadow": "rgba(0, 0, 0, 0.3)",
                "tab_bg": "#2a2a2a",
                "tab_fg": "#f5f5f5",
                "tab_active_bg": "#3a3a3a",
                "tab_active_fg": "#3498db",
                "tab_hover_bg": "#333333",
                "tab_hover_fg": "#f5f5f5",
                "tab_border": "#333333",
                "progress_bg": "#2a2a2a",
                "progress_fg": "#3498db",
                "slider_bg": "#2a2a2a",
                "slider_fg": "#3498db",
                "slider_handle": "#4a4a4a",
                "slider_handle_border": "#5a5a5a",
                "switch_bg": "#2a2a2a",
                "switch_fg": "#3498db",
                "switch_handle": "#4a4a4a",
                "switch_handle_border": "#5a5a5a",
                "checkbox_bg": "#2a2a2a",
                "checkbox_fg": "#3498db",
                "checkbox_border": "#4a4a4a",
                "radio_bg": "#2a2a2a",
                "radio_fg": "#3498db",
                "radio_border": "#4a4a4a",
                "calendar_bg": "#1e1e1e",
                "calendar_fg": "#f5f5f5",
                "calendar_header_bg": "#2a2a2a",
                "calendar_header_fg": "#f5f5f5",
                "calendar_weekend_bg": "#262626",
                "calendar_weekend_fg": "#f5f5f5",
                "calendar_today_bg": "#3498db",
                "calendar_today_fg": "#ffffff",
                "calendar_selected_bg": "#2980b9",
                "calendar_selected_fg": "#ffffff",
                "calendar_border": "#333333",
                "tooltip_bg": "#f5f5f5",
                "tooltip_fg": "#121212",
                "tooltip_border": "#f5f5f5",
                "tooltip_shadow": "rgba(0, 0, 0, 0.4)",
            }
        }
        
    def set_theme(self, theme_name):
        if theme_name in self.themes:
            self.current_theme = theme_name
            self.config["theme"] = theme_name
            save_config(self.config)
            self.apply_theme()
            return True
        return False
    
    def apply_theme(self):
        theme = self.themes[self.current_theme]
        
        # Aplicar tema a la aplicación
        if self.current_theme == "dark":
            self.app.set_theme("equilux")
        else:
            self.app.set_theme("arc")
        
        # Configurar estilos personalizados
        style = ttk.Style()
        
        # Configurar colores de fondo y texto
        style.configure("TFrame", background=theme["bg"])
        style.configure("TLabel", background=theme["bg"], foreground=theme["fg"])
        style.configure("TButton", background=theme["button_bg"], foreground=theme["button_fg"])
        style.map("TButton",
                 background=[("active", theme["button_hover_bg"])],
                 foreground=[("active", theme["button_hover_fg"])])
        style.configure("TEntry", fieldbackground=theme["input_bg"], foreground=theme["input_fg"])
        style.configure("TCombobox", fieldbackground=theme["input_bg"], foreground=theme["input_fg"])
        style.configure("TCheckbutton", background=theme["bg"], foreground=theme["fg"])
        style.configure("TRadiobutton", background=theme["bg"], foreground=theme["fg"])
        
        # Configurar estilos para encabezados
        style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), background=theme["header_bg"], foreground=theme["header_fg"])
        style.configure("Header.TFrame", background=theme["header_bg"])
        
        # Configurar estilos para tarjetas
        style.configure("Card.TFrame", background=theme["card_bg"], relief="raised")
        style.configure("Card.TLabel", background=theme["card_bg"], foreground=theme["fg"])
        
        # Configurar estilos para tablas
        style.configure("Treeview", background=theme["table_row_odd"], foreground=theme["fg"], fieldbackground=theme["table_row_odd"])
        style.configure("Treeview.Heading", background=theme["table_header_bg"], foreground=theme["table_header_fg"])
        style.map("Treeview",
                 background=[("selected", theme["accent"])],
                 foreground=[("selected", theme["button_fg"])])
        
        # Configurar estilos para pestañas
        style.configure("TNotebook", background=theme["bg"])
        style.configure("TNotebook.Tab", background=theme["tab_bg"], foreground=theme["tab_fg"], padding=[10, 5])
        style.map("TNotebook.Tab",
                 background=[("selected", theme["tab_active_bg"])],
                 foreground=[("selected", theme["tab_active_fg"])])
        
        # Configurar estilos para botones de acción
        style.configure("Action.TButton", font=("Helvetica", 10, "bold"), padding=5)
        style.configure("Success.TButton", background=theme["success"], foreground=theme["button_fg"])
        style.map("Success.TButton", background=[("active", theme["success"])])
        style.configure("Warning.TButton", background=theme["warning"], foreground=theme["button_fg"])
        style.map("Warning.TButton", background=[("active", theme["warning"])])
        style.configure("Error.TButton", background=theme["error"], foreground=theme["button_fg"])
        style.map("Error.TButton", background=[("active", theme["error"])])
        
        # Configurar estilos para marcos con bordes
        style.configure("Bordered.TFrame", background=theme["bg"], borderwidth=1, relief="solid")
        style.configure("Bordered.TLabelframe", background=theme["bg"], borderwidth=1, relief="solid")
        
        # Aplicar colores a widgets específicos
        self.app.configure(background=theme["bg"])
        
        # Actualizar todos los widgets
        for widget in self.app.winfo_children():
            self._update_widget_colors(widget, theme)
    
    def _update_widget_colors(self, widget, theme):
        try:
            widget_class = widget.winfo_class()
            
            if widget_class in ("Frame", "Labelframe", "TFrame", "TLabelframe"):
                widget.configure(background=theme["bg"])
            elif widget_class in ("Label", "TLabel"):
                widget.configure(background=theme["bg"], foreground=theme["fg"])
            elif widget_class in ("Button", "TButton"):
                pass  # Los botones ttk se manejan con el estilo
            elif widget_class in ("Entry", "TEntry"):
                pass  # Las entradas ttk se manejan con el estilo
            elif widget_class == "Text":
                widget.configure(background=theme["input_bg"], foreground=theme["input_fg"])
            elif widget_class == "Listbox":
                widget.configure(background=theme["input_bg"], foreground=theme["input_fg"])
            elif widget_class == "Canvas":
                widget.configure(background=theme["bg"])
            
            # Actualizar widgets hijos
            for child in widget.winfo_children():
                self._update_widget_colors(child, theme)
        except:
            pass  # Ignorar errores para widgets que no soportan estas propiedades

# ==========================================
# CONFIGURACIÓN DE ANIMACIONES
# ==========================================
class AnimationManager:
    @staticmethod
    def fade_in(widget, duration=500, steps=20):
        """Anima la aparición gradual de un widget"""
        widget.update_idletasks()
        alpha_step = 1.0 / steps
        delay_step = duration / steps
        
        # Ocultar inicialmente
        widget.attributes('-alpha', 0.0)
        widget.deiconify()
        
        # Animar
        for i in range(steps + 1):
            alpha = min(i * alpha_step, 1.0)
            widget.attributes('-alpha', alpha)
            widget.update_idletasks()
            time.sleep(delay_step / 1000)
    
    @staticmethod
    def fade_out(widget, duration=500, steps=20, callback=None):
        """Anima la desaparición gradual de un widget"""
        widget.update_idletasks()
        alpha_step = 1.0 / steps
        delay_step = duration / steps
        
        # Animar
        for i in range(steps, -1, -1):
            alpha = max(i * alpha_step, 0.0)
            widget.attributes('-alpha', alpha)
            widget.update_idletasks()
            time.sleep(delay_step / 1000)
        
        widget.withdraw()
        if callback:
            callback()
    
    @staticmethod
    def slide_in(widget, direction="right", duration=500, steps=20):
        """Anima la entrada deslizante de un widget"""
        widget.update_idletasks()
        width = widget.winfo_width()
        height = widget.winfo_height()
        
        if direction == "right":
            x_start = -width
            y_start = 0
            x_end = 0
            y_end = 0
        elif direction == "left":
            x_start = width
            y_start = 0
            x_end = 0
            y_end = 0
        elif direction == "down":
            x_start = 0
            y_start = -height
            x_end = 0
            y_end = 0
        elif direction == "up":
            x_start = 0
            y_start = height
            x_end = 0
            y_end = 0
        
        x_step = (x_end - x_start) / steps
        y_step = (y_end - y_start) / steps
        delay_step = duration / steps
        
        # Posicionar inicialmente
        widget.place(x=x_start, y=y_start)
        widget.deiconify()
        
        # Animar
        for i in range(steps + 1):
            x = x_start + i * x_step
            y = y_start + i * y_step
            widget.place(x=x, y=y)
            widget.update_idletasks()
            time.sleep(delay_step / 1000)
    
    @staticmethod
    def slide_out(widget, direction="right", duration=500, steps=20, callback=None):
        """Anima la salida deslizante de un widget"""
        widget.update_idletasks()
        width = widget.winfo_width()
        height = widget.winfo_height()
        
        x_start = widget.winfo_x()
        y_start = widget.winfo_y()
        
        if direction == "right":
            x_end = width
            y_end = y_start
        elif direction == "left":
            x_end = -width
            y_end = y_start
        elif direction == "down":
            x_end = x_start
            y_end = height
        elif direction == "up":
            x_end = x_start
            y_end = -height
        
        x_step = (x_end - x_start) / steps
        y_step = (y_end - y_start) / steps
        delay_step = duration / steps
        
        # Animar
        for i in range(steps + 1):
            x = x_start + i * x_step
            y = y_start + i * y_step
            widget.place(x=x, y=y)
            widget.update_idletasks()
            time.sleep(delay_step / 1000)
        
        widget.withdraw()
        if callback:
            callback()
    
    @staticmethod
    def pulse(widget, duration=1000, steps=20, scale=1.1):
        """Crea un efecto de pulso (agrandar y reducir)"""
        widget.update_idletasks()
        original_width = widget.winfo_width()
        original_height = widget.winfo_height()
        
        max_width = original_width * scale
        max_height = original_height * scale
        
        half_steps = steps // 2
        width_step_up = (max_width - original_width) / half_steps
        height_step_up = (max_height - original_height) / half_steps
        width_step_down = (original_width - max_width) / half_steps
        height_step_down = (original_height - max_height) / half_steps
        delay_step = duration / steps
        
        # Animar crecimiento
        for i in range(half_steps):
            new_width = original_width + i * width_step_up
            new_height = original_height + i * height_step_up
            widget.configure(width=int(new_width), height=int(new_height))
            widget.update_idletasks()
            time.sleep(delay_step / 1000)
        
        # Animar reducción
        for i in range(half_steps):
            new_width = max_width + i * width_step_down
            new_height = max_height + i * height_step_down
            widget.configure(width=int(new_width), height=int(new_height))
            widget.update_idletasks()
            time.sleep(delay_step / 1000)
        
        # Restaurar tamaño original
        widget.configure(width=original_width, height=original_height)
        widget.update_idletasks()
    
    @staticmethod
    def highlight(widget, duration=500, color="#ffcc00"):
        """Destaca un widget cambiando temporalmente su color de fondo"""
        original_bg = widget.cget("background")
        
        widget.configure(background=color)
        widget.update_idletasks()
        
        def restore_bg():
            widget.configure(background=original_bg)
        
        widget.after(duration, restore_bg)
    
    @staticmethod
    def shake(widget, duration=500, distance=10, steps=10):
        """Crea un efecto de sacudida horizontal"""
        widget.update_idletasks()
        original_x = widget.winfo_x()
        delay_step = duration / (steps * 2)
        
        for i in range(steps):
            # Mover a la derecha
            widget.place(x=original_x + distance)
            widget.update_idletasks()
            time.sleep(delay_step / 1000)
            
            # Mover a la izquierda
            widget.place(x=original_x - distance)
            widget.update_idletasks()
            time.sleep(delay_step / 1000)
        
        # Restaurar posición original
        widget.place(x=original_x)
        widget.update_idletasks()
    
    @staticmethod
    def typewriter(label, text, delay=50):
        """Efecto de máquina de escribir para mostrar texto gradualmente"""
        label.configure(text="")
        
        def type_char(index=0):
            if index < len(text):
                label.configure(text=label.cget("text") + text[index])
                label.after(delay, type_char, index + 1)
        
        type_char()
    
@staticmethod
def loading_animation(canvas, x, y, radius=10, duration=2000, color="#3498db"):
    """Crea una animación de carga circular"""
    
    steps = 8
    angle_step = 360 / steps
    delay_step = duration / steps
    
    dots = []
    for i in range(steps):
        angle = i * angle_step
        rad_angle = angle * (math.pi / 180)
        dot_x = x + radius * 2 * math.cos(rad_angle)
        dot_y = y + radius * 2 * math.sin(rad_angle)
        dot = canvas.create_oval(dot_x - radius/2, dot_y - radius/2, 
                                dot_x + radius/2, dot_y + radius/2, 
                                fill=color, outline="")
        dots.append(dot)
    
    def animate(step=0):
        for i, dot in enumerate(dots):
            opacity = 0.3 + 0.7 * ((i + step) % steps) / steps
            # Convertir la opacidad a formato hexadecimal para el color
            hex_opacity = format(int(opacity * 255), '02x')
            canvas.itemconfig(dot, fill=f"{color}{hex_opacity}")
        canvas.after(int(delay_step), animate, (step + 1) % steps)
    
    animate()
    return dots

    # Clases para la interfaz gráfica
class LoginFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.i18n = controller.i18n
        
        # Variables
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        
        # Widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Contenedor principal con padding
        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(fill="both", expand=True)
        
        # Logo o imagen de bienvenida (usando un canvas para efectos visuales)
        logo_frame = ttk.Frame(main_frame)
        logo_frame.pack(pady=(0, 20))
        
        logo_canvas = tk.Canvas(logo_frame, width=200, height=100, highlightthickness=0)
        logo_canvas.pack()
        
        # Dibujar un logo simple
        logo_canvas.create_oval(50, 20, 150, 80, fill="#3498db", outline="")
        logo_canvas.create_text(100, 50, text="AMS", fill="white", font=("Helvetica", 24, "bold"))
        
        # Título con animación de escritura
        self.title_label = ttk.Label(main_frame, text="", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=(0, 30))
        
        # Marco de login con efecto de elevación
        login_frame = ttk.Frame(main_frame, style="Card.TFrame")
        login_frame.pack(padx=20, pady=20, fill="x")
        
        # Padding interno
        inner_frame = ttk.Frame(login_frame, padding=20)
        inner_frame.pack(fill="x")
        
        # Subtítulo
        login_label = ttk.Label(inner_frame, text=self.i18n.get("login"), font=("Helvetica", 14))
        login_label.pack(pady=(0, 20), anchor="w")
        
        # Usuario
        username_frame = ttk.Frame(inner_frame)
        username_frame.pack(fill="x", pady=5)
        
        ttk.Label(username_frame, text=self.i18n.get("username")).pack(side="left", padx=(0, 10))
        username_entry = ttk.Entry(username_frame, textvariable=self.username_var, width=30)
        username_entry.pack(side="right", fill="x", expand=True)
        
        # Contraseña
        password_frame = ttk.Frame(inner_frame)
        password_frame.pack(fill="x", pady=5)
        
        ttk.Label(password_frame, text=self.i18n.get("password")).pack(side="left", padx=(0, 10))
        password_entry = ttk.Entry(password_frame, textvariable=self.password_var, show="•", width=30)
        password_entry.pack(side="right", fill="x", expand=True)
        
        # Botón de login con estilo
        button_frame = ttk.Frame(inner_frame)
        button_frame.pack(fill="x", pady=(20, 0))
        
        login_button = ttk.Button(
            button_frame, 
            text=self.i18n.get("login_button"), 
            command=self.login,
            style="Action.TButton"
        )
        login_button.pack(side="right")
        
        # Enlazar Enter a login
        self.bind("<Return>", lambda event: self.login())
        
        # Iniciar animación de escritura después de un breve retraso
        self.after(500, lambda: AnimationManager.typewriter(
            self.title_label, 
            self.i18n.get("welcome"), 
            delay=50
        ))
        
    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        
        if not username or not password:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("complete_fields"))
            return
        
        success, role = authenticate_user(username, password)
        
        if success:
            self.controller.current_user = username
            self.controller.current_role = role
            
            # Mostrar mensaje de bienvenida
            welcome_text = f"{self.i18n.get('welcome_back')}, {username}!"
            messagebox.showinfo(self.i18n.get("success"), welcome_text)
            
            # Redirigir según el rol
            if role == "admin":
                self.controller.show_frame("AdminDashboard")
            elif role == "teacher":
                self.controller.show_frame("TeacherDashboard")
            elif role == "student":
                self.controller.show_frame("StudentDashboard")
        else:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("invalid_credentials"))

# ==========================================
# CONFIGURACIÓN DEL PANEL DE ADMINISTRACIÓN
# ==========================================

class AdminDashboard(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.i18n = controller.i18n
        
        # Variables
        self.new_username_var = tk.StringVar()
        self.new_password_var = tk.StringVar()
        self.new_role_var = tk.StringVar(value="student")
        self.selected_date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_users)
        
        # Widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Crear layout principal con sidebar y contenido
        self.main_paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.main_paned.pack(fill="both", expand=True)
        
        # Sidebar
        self.sidebar = ttk.Frame(self.main_paned, style="Card.TFrame", padding=10)
        self.main_paned.add(self.sidebar, weight=1)
        
        # Contenido principal
        self.content = ttk.Frame(self.main_paned)
        self.main_paned.add(self.content, weight=4)
        
        # Configurar sidebar
        self.setup_sidebar()
        
        # Configurar contenido inicial
        self.show_dashboard()
        
    def setup_sidebar(self):
        # Logo o avatar
        logo_frame = ttk.Frame(self.sidebar)
        logo_frame.pack(fill="x", pady=(0, 20))
        
        # Título del sistema
        system_name = ttk.Label(logo_frame, text="AMS", font=("Helvetica", 18, "bold"))
        system_name.pack(side="left")
        
        # Información del usuario
        user_frame = ttk.Frame(self.sidebar)
        user_frame.pack(fill="x", pady=(0, 20))
        
        user_label = ttk.Label(user_frame, text=f"{self.i18n.get('admin')}: {self.controller.current_user}", font=("Helvetica", 10))
        user_label.pack(anchor="w")
        
        # Separador
        ttk.Separator(self.sidebar, orient="horizontal").pack(fill="x", pady=10)
        
        # Menú de navegación
        nav_frame = ttk.Frame(self.sidebar)
        nav_frame.pack(fill="x")
        
        # Estilo para botones de navegación
        style = ttk.Style()
        style.configure("Sidebar.TButton", font=("Helvetica", 11), anchor="w", padding=(10, 5))

        
        # Botones de navegación
        dashboard_btn = ttk.Button(
            nav_frame,
            text=self.i18n.get("dashboard"),
            command=self.show_dashboard,
            style="Sidebar.TButton"
            
        )
        dashboard_btn.pack(fill="x", pady=2)
        
        users_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("user_management"), 
            command=self.show_users,
            style="Sidebar.TButton"
        )
        users_btn.pack(fill="x", pady=2)
        
        attendance_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("attendance_management"), 
            command=self.show_attendance,
            style="Sidebar.TButton"
        )
        attendance_btn.pack(fill="x", pady=2)
        
        reports_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("reports"), 
            command=self.show_reports,
            style="Sidebar.TButton"
        )
        reports_btn.pack(fill="x", pady=2)
        
        settings_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("settings"), 
            command=self.show_settings,
            style="Sidebar.TButton"
        )
        settings_btn.pack(fill="x", pady=2)
        
        # Separador
        ttk.Separator(self.sidebar, orient="horizontal").pack(fill="x", pady=10)
        
        # Botón de cerrar sesión en la parte inferior
        logout_btn = ttk.Button(
            self.sidebar, 
            text=self.i18n.get("logout"), 
            command=self.confirm_logout,
            style="Error.TButton"
        )
        logout_btn.pack(side="bottom", fill="x", pady=(10, 0))
    
    def clear_content(self):
        # Limpiar el frame de contenido
        for widget in self.content.winfo_children():
            widget.destroy()
    
    def show_dashboard(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("dashboard"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido del dashboard
        dashboard_frame = ttk.Frame(self.content, padding=20)
        dashboard_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Tarjetas de resumen
        cards_frame = ttk.Frame(dashboard_frame)
        cards_frame.pack(fill="x", pady=(0, 20))
        
        # Configurar grid para tarjetas
        cards_frame.columnconfigure(0, weight=1)
        cards_frame.columnconfigure(1, weight=1)
        cards_frame.columnconfigure(2, weight=1)
        
        # Tarjeta de usuarios
        users_card = ttk.Frame(cards_frame, style="Card.TFrame", padding=15)
        users_card.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        users_count = len(load_users()["users"])
        ttk.Label(users_card, text=self.i18n.get("user_management"), font=("Helvetica", 12, "bold")).pack(anchor="w")
        ttk.Label(users_card, text=str(users_count), font=("Helvetica", 24)).pack(anchor="w", pady=5)
        
        # Tarjeta de asistencia
        attendance_card = ttk.Frame(cards_frame, style="Card.TFrame", padding=15)
        attendance_card.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        attendance_data = load_attendance()
        attendance_count = len(attendance_data["attendance"])
        ttk.Label(attendance_card, text=self.i18n.get("attendance_management"), font=("Helvetica", 12, "bold")).pack(anchor="w")
        ttk.Label(attendance_card, text=str(attendance_count), font=("Helvetica", 24)).pack(anchor="w", pady=5)
        
        # Tarjeta de reportes
        reports_card = ttk.Frame(cards_frame, style="Card.TFrame", padding=15)
        reports_card.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        
        # Calcular tasa de asistencia general
        total_present = 0
        total_records = 0
        
        for date, records in attendance_data["attendance"].items():
            for student, status in records.items():
                total_records += 1
                if status == self.i18n.get("present"):
                    total_present += 1
        
        attendance_rate = round((total_present / total_records) * 100, 2) if total_records > 0 else 0
        
        ttk.Label(reports_card, text=self.i18n.get("attendance_rate"), font=("Helvetica", 12, "bold")).pack(anchor="w")
        ttk.Label(reports_card, text=f"{attendance_rate}%", font=("Helvetica", 24)).pack(anchor="w", pady=5)
        
        # Actividad reciente
        recent_frame = ttk.LabelFrame(dashboard_frame, text=self.i18n.get("recent_activity"))
        recent_frame.pack(fill="both", expand=True, pady=10)
        
        # Tabla de actividad reciente
        columns = ("date", "student", "status")
        self.recent_tree = ttk.Treeview(recent_frame, columns=columns, show="headings", height=10)
        
        # Definir encabezados
        self.recent_tree.heading("date", text=self.i18n.get("date"))
        self.recent_tree.heading("student", text=self.i18n.get("student"))
        self.recent_tree.heading("status", text=self.i18n.get("status"))
        
        # Configurar columnas
        self.recent_tree.column("date", width=150)
        self.recent_tree.column("student", width=150)
        self.recent_tree.column("status", width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(recent_frame, orient="vertical", command=self.recent_tree.yview)
        self.recent_tree.configure(yscrollcommand=scrollbar.set)
        
        # Empaquetar
        self.recent_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Cargar datos recientes
        self.load_recent_activity()
    
    def load_recent_activity(self):
        # Limpiar tabla
        for item in self.recent_tree.get_children():
            self.recent_tree.delete(item)
        
        # Cargar datos de asistencia
        attendance_data = load_attendance()
        
        # Convertir a lista para ordenar
        all_records = []
        for date, records in attendance_data["attendance"].items():
            for student, status in records.items():
                all_records.append((date, student, status))
        
        # Ordenar por fecha (más reciente primero)
        all_records.sort(reverse=True)
        
        # Mostrar solo los 10 más recientes
        for i, (date, student, status) in enumerate(all_records[:10]):
            self.recent_tree.insert("", "end", values=(date, student, status))
    
    def show_users(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("user_management"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido de usuarios
        users_frame = ttk.Frame(self.content, padding=20)
        users_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Marco para crear usuarios
        create_frame = ttk.LabelFrame(users_frame, text=self.i18n.get("create_user"))
        create_frame.pack(fill="x", pady=(0, 20))
        
        # Formulario en grid
        form_frame = ttk.Frame(create_frame, padding=10)
        form_frame.pack(fill="x")
        
        # Configurar grid
        form_frame.columnconfigure(0, weight=0)
        form_frame.columnconfigure(1, weight=1)
        
        # Usuario
        ttk.Label(form_frame, text=self.i18n.get("username")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        username_entry = ttk.Entry(form_frame, textvariable=self.new_username_var)
        username_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Contraseña
        ttk.Label(form_frame, text=self.i18n.get("password")).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        password_entry = ttk.Entry(form_frame, textvariable=self.new_password_var, show="•")
        password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Rol
        ttk.Label(form_frame, text=self.i18n.get("role")).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        role_combo = ttk.Combobox(
            form_frame, 
            textvariable=self.new_role_var, 
            values=[self.i18n.get("admin"), self.i18n.get("teacher"), self.i18n.get("student")], 
            state="readonly"
        )
        role_combo.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        # Botón de crear
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        create_button = ttk.Button(
            button_frame, 
            text=self.i18n.get("create_user_button"), 
            command=self.create_new_user,
            style="Success.TButton"
        )
        create_button.pack()
        
        # Marco para buscar usuarios
        search_frame = ttk.Frame(users_frame)
        search_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(search_frame, text=self.i18n.get("search")).pack(side="left", padx=(0, 5))
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side="left", fill="x", expand=True)
        
        # Lista de usuarios
        list_frame = ttk.LabelFrame(users_frame, text=self.i18n.get("user_list"))
        list_frame.pack(fill="both", expand=True)
        
        # Tabla de usuarios
        columns = ("username", "role")
        self.users_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        # Definir encabezados
        self.users_tree.heading("username", text=self.i18n.get("username"))
        self.users_tree.heading("role", text=self.i18n.get("role"))
        
        # Configurar columnas
        self.users_tree.column("username", width=150)
        self.users_tree.column("role", width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.users_tree.yview)
        self.users_tree.configure(yscrollcommand=scrollbar.set)
        
        # Empaquetar
        self.users_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Cargar usuarios
        self.load_users_list()
    
    def filter_users(self, *args):
        search_term = self.search_var.get().lower()
        
        # Limpiar tabla
        for item in self.users_tree.get_children():
            self.users_tree.delete(item)
        
        # Cargar usuarios filtrados
        users_data = load_users()
        
        for user in users_data["users"]:
            username = user["username"].lower()
            role = user["role"].lower()
            
            if search_term in username or search_term in role:
                # Traducir el rol
                translated_role = self.i18n.get(user["role"])
                self.users_tree.insert("", "end", values=(user["username"], translated_role))
    
    def show_attendance(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("attendance_management"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido de asistencia
        attendance_frame = ttk.Frame(self.content, padding=20)
        attendance_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Marco para seleccionar fecha
        date_frame = ttk.Frame(attendance_frame)
        date_frame.pack(fill="x", pady=(0, 20))
        
        ttk.Label(date_frame, text=self.i18n.get("date")).pack(side="left", padx=(0, 5))
        date_entry = ttk.Entry(date_frame, textvariable=self.selected_date_var, width=15)
        date_entry.pack(side="left", padx=5)
        
        view_button = ttk.Button(
            date_frame, 
            text=self.i18n.get("view_attendance"), 
            command=self.load_date_attendance
        )
        view_button.pack(side="left", padx=5)
        
        # Fecha actual como botón
        today_button = ttk.Button(
            date_frame, 
            text=self.i18n.get("today"), 
            command=lambda: (
                self.selected_date_var.set(datetime.now().strftime("%Y-%m-%d")),
                self.load_date_attendance()
            )
        )
        today_button.pack(side="left", padx=5)
        
        # Lista de asistencia
        list_frame = ttk.LabelFrame(attendance_frame, text=self.i18n.get("attendance_management"))
        list_frame.pack(fill="both", expand=True)
        
        # Tabla de asistencia
        columns = ("student", "status")
        self.attendance_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        # Definir encabezados
        self.attendance_tree.heading("student", text=self.i18n.get("student"))
        self.attendance_tree.heading("status", text=self.i18n.get("status"))
        
        # Configurar columnas
        self.attendance_tree.column("student", width=150)
        self.attendance_tree.column("status", width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.attendance_tree.yview)
        self.attendance_tree.configure(yscrollcommand=scrollbar.set)
        
        # Empaquetar
        self.attendance_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botones de acción
        action_frame = ttk.Frame(attendance_frame)
        action_frame.pack(fill="x", pady=10)
        
        edit_button = ttk.Button(
            action_frame, 
            text=self.i18n.get("edit_attendance"), 
            command=self.edit_attendance_dialog
        )
        edit_button.pack(side="left", padx=5)
        
        # Cargar asistencia del día actual
        self.load_date_attendance()
    
    def show_reports(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("reports"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido de reportes
        reports_frame = ttk.Frame(self.content, padding=20)
        reports_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Marco para exportar
        export_frame = ttk.LabelFrame(reports_frame, text=self.i18n.get("export_data"))
        export_frame.pack(fill="x", pady=(0, 20))
        
        export_button = ttk.Button(
            export_frame, 
            text=self.i18n.get("export_csv"), 
            command=self.export_csv,
            padding=10
        )
        export_button.pack(padx=10, pady=10)
        
        # Marco para estadísticas
        stats_frame = ttk.LabelFrame(reports_frame, text=self.i18n.get("statistics"))
        stats_frame.pack(fill="both", expand=True)
        
        # Botón para generar estadísticas
        generate_button = ttk.Button(
            stats_frame, 
            text=self.i18n.get("generate_statistics"), 
            command=self.generate_statistics,
            padding=10
        )
        generate_button.pack(padx=10, pady=10)
        
        # Área de texto para mostrar estadísticas con estilo
        self.stats_text = tk.Text(stats_frame, height=15, width=50, wrap="word", padx=10, pady=10)
        self.stats_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Configurar etiquetas para dar formato al texto
        self.stats_text.tag_configure("title", font=("Helvetica", 12, "bold"))
        self.stats_text.tag_configure("subtitle", font=("Helvetica", 10, "bold"))
        self.stats_text.tag_configure("normal", font=("Helvetica", 10))
        self.stats_text.tag_configure("highlight", font=("Helvetica", 10, "bold"), foreground="#3498db")
    
    def show_settings(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("settings"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido de configuración
        settings_frame = ttk.Frame(self.content, padding=20)
        settings_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Marco para preferencias
        pref_frame = ttk.LabelFrame(settings_frame, text=self.i18n.get("preferences"))
        pref_frame.pack(fill="x", pady=(0, 20))
        
        # Idioma
        lang_frame = ttk.Frame(pref_frame, padding=10)
        lang_frame.pack(fill="x")
        
        ttk.Label(lang_frame, text=self.i18n.get("language")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Obtener idioma actual
        config = load_config()
        current_lang = config["language"]
        
        # Combobox para idioma
        lang_var = tk.StringVar(value=current_lang)
        lang_combo = ttk.Combobox(
            lang_frame, 
            textvariable=lang_var, 
            values=["es", "en"], 
            state="readonly",
            width=10
        )
        lang_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Tema
        theme_frame = ttk.Frame(pref_frame, padding=10)
        theme_frame.pack(fill="x")
        
        ttk.Label(theme_frame, text=self.i18n.get("theme")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Obtener tema actual
        current_theme = config["theme"]
        
        # Combobox para tema
        theme_var = tk.StringVar(value=current_theme)
        theme_combo = ttk.Combobox(
            theme_frame, 
            textvariable=theme_var, 
            values=[self.i18n.get("light"), self.i18n.get("dark")], 
            state="readonly",
            width=10
        )
        theme_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Botón para guardar preferencias
        save_button = ttk.Button(
            pref_frame, 
            text=self.i18n.get("save"), 
            command=lambda: self.save_preferences(lang_var.get(), theme_var.get()),
            padding=10
        )
        save_button.pack(padx=10, pady=10, anchor="e")
        
        # Marco para cambiar contraseña
        password_frame = ttk.LabelFrame(settings_frame, text=self.i18n.get("change_password"))
        password_frame.pack(fill="x")
        
        # Formulario para cambiar contraseña
        pwd_form = ttk.Frame(password_frame, padding=10)
        pwd_form.pack(fill="x")
        
        # Configurar grid
        pwd_form.columnconfigure(0, weight=0)
        pwd_form.columnconfigure(1, weight=1)
        
        # Contraseña actual
        ttk.Label(pwd_form, text=self.i18n.get("current_password")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        current_pwd_var = tk.StringVar()
        current_pwd_entry = ttk.Entry(pwd_form, textvariable=current_pwd_var, show="•")
        current_pwd_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Nueva contraseña
        ttk.Label(pwd_form, text=self.i18n.get("new_password")).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        new_pwd_var = tk.StringVar()
        new_pwd_entry = ttk.Entry(pwd_form, textvariable=new_pwd_var, show="•")
        new_pwd_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Confirmar contraseña
        ttk.Label(pwd_form, text=self.i18n.get("confirm_password")).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        confirm_pwd_var = tk.StringVar()
        confirm_pwd_entry = ttk.Entry(pwd_form, textvariable=confirm_pwd_var, show="•")
        confirm_pwd_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        # Botón para cambiar contraseña
        change_pwd_button = ttk.Button(
            pwd_form, 
            text=self.i18n.get("change_password"), 
            command=lambda: self.change_password(
                current_pwd_var.get(),
                new_pwd_var.get(),
                confirm_pwd_var.get()
            ),
            padding=10
        )
        change_pwd_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="e")
    
    def save_preferences(self, language, theme):
        # Convertir tema de nombre mostrado a valor interno
        if theme == self.i18n.get("light"):
            theme_value = "light"
        elif theme == self.i18n.get("dark"):
            theme_value = "dark"
        else:
            theme_value = theme
        
        # Guardar configuración
        config = load_config()
        config["language"] = language
        config["theme"] = theme_value
        save_config(config)
        
        # Aplicar cambios
        self.controller.i18n.set_language(language)
        self.controller.theme_manager.set_theme(theme_value)
        
        # Mostrar mensaje de éxito
        messagebox.showinfo(
            self.i18n.get("success"), 
            self.i18n.get("preferences_saved")
        )
        
        # Recargar la aplicación para aplicar los cambios
        self.controller.reload_app()
    
    def change_password(self, current_pwd, new_pwd, confirm_pwd):
        # Validar que las contraseñas no estén vacías
        if not current_pwd or not new_pwd or not confirm_pwd:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("complete_fields")
            )
            return
        
        # Validar que la nueva contraseña y la confirmación coincidan
        if new_pwd != confirm_pwd:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("passwords_not_match")
            )
            return
        
        # Validar longitud de la contraseña
        if len(new_pwd) < 6:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("password_length")
            )
            return
        
        # Verificar contraseña actual
        users_data = load_users()
        current_user = self.controller.current_user
        
        user_found = False
        for user in users_data["users"]:
            if user["username"] == current_user:
                user_found = True
                if user["password"] == hash_password(current_pwd):
                    # Cambiar contraseña
                    user["password"] = hash_password(new_pwd)
                    save_users(users_data)
                    messagebox.showinfo(
                        self.i18n.get("success"), 
                        self.i18n.get("password_changed")
                    )
                    return
                else:
                    messagebox.showerror(
                        self.i18n.get("error"), 
                        self.i18n.get("invalid_credentials")
                    )
                    return
        
        if not user_found:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("user_not_found")
            )
    
    def create_new_user(self):
        username = self.new_username_var.get()
        password = self.new_password_var.get()
        
        # Convertir rol de nombre mostrado a valor interno
        role_display = self.new_role_var.get()
        if role_display == self.i18n.get("admin"):
            role = "admin"
        elif role_display == self.i18n.get("teacher"):
            role = "teacher"
        elif role_display == self.i18n.get("student"):
            role = "student"
        else:
            role = role_display
        
        if not username or not password:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("complete_fields"))
            return
        
        # Validar nombre de usuario (solo letras, números y guiones bajos)
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("invalid_username"))
            return
        
        # Validar contraseña (mínimo 6 caracteres)
        if len(password) < 6:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("password_length"))
            return
        
        success, message_key = create_user(username, password, role)
        
        if success:
            messagebox.showinfo(self.i18n.get("success"), self.i18n.get(message_key))
            # Limpiar campos
            self.new_username_var.set("")
            self.new_password_var.set("")
            # Actualizar lista
            self.load_users_list()
        else:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get(message_key))
    
    def load_users_list(self):
        # Limpiar tabla
        for item in self.users_tree.get_children():
            self.users_tree.delete(item)
        
        # Cargar usuarios
        users_data = load_users()
        
        for user in users_data["users"]:
            # Traducir el rol
            translated_role = self.i18n.get(user["role"])
            self.users_tree.insert("", "end", values=(user["username"], translated_role))
    
    def load_date_attendance(self):
        date = self.selected_date_var.get()
        
        # Validar formato de fecha
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("invalid_date"))
            return
        
        # Limpiar tabla
        for item in self.attendance_tree.get_children():
            self.attendance_tree.delete(item)
        
        # Cargar asistencia
        attendance_records = get_date_attendance(date)
        
        if not attendance_records:
            messagebox.showinfo(self.i18n.get("info"), self.i18n.get("no_records"))
            return
        
        for student, status in attendance_records.items():
            self.attendance_tree.insert("", "end", values=(student, status))
    
    def edit_attendance_dialog(self):
        # Verificar si hay un elemento seleccionado
        selected_item = self.attendance_tree.selection()
        
        if not selected_item:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("select_record"))
            return
        
        # Obtener datos del elemento seleccionado
        student = self.attendance_tree.item(selected_item[0], "values")[0]
        current_status = self.attendance_tree.item(selected_item[0], "values")[1]
        
        # Crear diálogo
        dialog = tk.Toplevel(self)
        dialog.title(self.i18n.get("edit_attendance"))
        dialog.geometry("400x200")
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()
        
        # Aplicar tema al diálogo
        dialog.configure(background=self.controller.theme_manager.themes[self.controller.theme_manager.current_theme]["bg"])
        
        # Variables
        status_var = tk.StringVar(value=current_status)
        
        # Contenido del diálogo
        content_frame = ttk.Frame(dialog, padding=20)
        content_frame.pack(fill="both", expand=True)
        
        # Información del estudiante
        ttk.Label(
            content_frame, 
            text=f"{self.i18n.get('student')}: {student}",
            font=("Helvetica", 12, "bold")
        ).pack(padx=10, pady=10)
        
        # Selector de estado
        status_frame = ttk.Frame(content_frame)
        status_frame.pack(fill="x", pady=10)
        
        ttk.Label(status_frame, text=f"{self.i18n.get('status')}:").pack(side="left", padx=(0, 10))
        status_combo = ttk.Combobox(
            status_frame, 
            textvariable=status_var, 
            values=[self.i18n.get("present"), self.i18n.get("absent"), self.i18n.get("late")], 
            state="readonly",
            width=15
        )
        status_combo.pack(side="left")
        
        # Botones
        button_frame = ttk.Frame(content_frame)
        button_frame.pack(fill="x", pady=20)
        
        ttk.Button(
            button_frame, 
            text=self.i18n.get("cancel"), 
            command=dialog.destroy,
            style="Error.TButton"
        ).pack(side="left", padx=5)
        
        ttk.Button(
            button_frame, 
            text=self.i18n.get("save"), 
            command=lambda: self.save_edited_attendance(dialog, student, status_var.get()),
            style="Success.TButton"
        ).pack(side="right", padx=5)
    
    def save_edited_attendance(self, dialog, student, new_status):
        date = self.selected_date_var.get()
        
        success = edit_attendance(date, student, new_status)
        
        if success:
            messagebox.showinfo(self.i18n.get("success"), self.i18n.get("record_updated"))
            dialog.destroy()
            # Actualizar tabla
            self.load_date_attendance()
        else:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("update_failed"))
    
    def export_csv(self):
        # Solicitar ubicación para guardar
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[(self.i18n.get("csv_files"), ".csv"), (self.i18n.get("all_files"), ".*")],
            title=self.i18n.get("save_as_csv")
        )
        
        if not filename:
            return
        
        success, message_key = export_to_csv(filename)
        
        if success:
            messagebox.showinfo(self.i18n.get("success"), self.i18n.get(message_key))
        else:
            messagebox.showerror(self.i18n.get("error"), message_key)
    
    def generate_statistics(self):
        attendance_data = load_attendance()
        
        if not attendance_data["attendance"]:
            messagebox.showinfo(self.i18n.get("info"), self.i18n.get("no_attendance_data"))
            return
        
        # Limpiar área de texto
        self.stats_text.delete(1.0, tk.END)
        
        # Calcular estadísticas
        total_days = len(attendance_data["attendance"])
        
        # Obtener todos los estudiantes
        all_students = set()
        for date_records in attendance_data["attendance"].values():
            all_students.update(date_records.keys())
        
        total_students = len(all_students)
        
        # Calcular asistencia por estudiante
        student_stats = {}
        
        for student in all_students:
            present = 0
            absent = 0
            late = 0
            
            for date, records in attendance_data["attendance"].items():
                if student in records:
                    status = records[student]
                    if status == self.i18n.get("present"):
                        present += 1
                    elif status == self.i18n.get("absent"):
                        absent += 1
                    elif status == self.i18n.get("late"):
                        late += 1
            
            student_stats[student] = {
                "present": present,
                "absent": absent,
                "late": late,
                "attendance_rate": round((present / total_days) * 100, 2) if total_days > 0 else 0
            }
        
        # Mostrar estadísticas generales
        self.stats_text.insert(tk.END, f"{self.i18n.get('total_days')}: {total_days}\n", "title")
        self.stats_text.insert(tk.END, f"{self.i18n.get('total_students')}: {total_students}\n\n", "title")
        
        # Mostrar estadísticas por estudiante
        self.stats_text.insert(tk.END, f"{self.i18n.get('student_statistics')}:\n", "subtitle")
        self.stats_text.insert(tk.END, "-" * 50 + "\n", "normal")
        
        for student, stats in student_stats.items():
            self.stats_text.insert(tk.END, f"{self.i18n.get('student')}: {student}\n", "subtitle")
            self.stats_text.insert(tk.END, f"  {self.i18n.get('present_days')}: {stats['present']}\n", "normal")
            self.stats_text.insert(tk.END, f"  {self.i18n.get('absent_days')}: {stats['absent']}\n", "normal")
            self.stats_text.insert(tk.END, f"  {self.i18n.get('late_days')}: {stats['late']}\n", "normal")
            self.stats_text.insert(tk.END, f"  {self.i18n.get('attendance_rate')}: {stats['attendance_rate']}%\n", "highlight")
            self.stats_text.insert(tk.END, "-" * 50 + "\n", "normal")
    
    def confirm_logout(self):
        result = messagebox.askyesno(
            self.i18n.get("confirm"), 
            self.i18n.get("confirm_logout")
        )
        
        if result:
            self.controller.logout()

# ==========================================
# CONFIGURACIÓN DE INTERFAZ DE USUARIO PARA EL PROFESOR
# ==========================================

class TeacherDashboard(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.i18n = controller.i18n
        
        # Variables
        self.selected_date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        self.student_var = tk.StringVar()
        self.status_var = tk.StringVar(value=self.i18n.get("present"))
        
        # Widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Crear layout principal con sidebar y contenido
        self.main_paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.main_paned.pack(fill="both", expand=True)
        
        # Sidebar
        self.sidebar = ttk.Frame(self.main_paned, style="Card.TFrame", padding=10)
        self.main_paned.add(self.sidebar, weight=1)
        
        # Contenido principal
        self.content = ttk.Frame(self.main_paned)
        self.main_paned.add(self.content, weight=4)
        
        # Configurar sidebar
        self.setup_sidebar()
        
        # Configurar contenido inicial
        self.show_dashboard()
    
    def setup_sidebar(self):
        # Logo o avatar
        logo_frame = ttk.Frame(self.sidebar)
        logo_frame.pack(fill="x", pady=(0, 20))
        
        # Título del sistema
        system_name = ttk.Label(logo_frame, text="AMS", font=("Helvetica", 18, "bold"))
        system_name.pack(side="left")
        
        # Información del usuario
        user_frame = ttk.Frame(self.sidebar)
        user_frame.pack(fill="x", pady=(0, 20))
        
        user_label = ttk.Label(user_frame, text=f"{self.i18n.get('teacher')}: {self.controller.current_user}", font=("Helvetica", 10))
        user_label.pack(anchor="w")
        
        # Separador
        ttk.Separator(self.sidebar, orient="horizontal").pack(fill="x", pady=10)
        
        # Menú de navegación
        nav_frame = ttk.Frame(self.sidebar)
        nav_frame.pack(fill="x")
        
        # Estilo para botones de navegación
        style = ttk.Style()
        style.configure("Sidebar.TButton", font=("Helvetica", 11), anchor="w", padding=(10, 5))

        button_style = {"style": "Sidebar.TButton"}
        
        # Botones de navegación
        dashboard_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("dashboard"), 
            command=self.show_dashboard,
            style="Sidebar.TButton"
        )
        dashboard_btn.pack(fill="x", pady=2)
        
        attendance_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("attendance_management"), 
            command=self.show_attendance,
            style="Sidebar.TButton"
        )
        attendance_btn.pack(fill="x", pady=2)

        just_btn = ttk.Button(
            nav_frame,
            text="Revisar Justificaciones",
            command=self.show_pending_justifications,
            style="Sidebar.TButton"
        )
        just_btn.pack(fill="x", pady=2)

        reports_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("reports"), 
            command=self.show_reports,
            style="Sidebar.TButton"
        )
        reports_btn.pack(fill="x", pady=2)
        
        settings_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("settings"), 
            command=self.show_settings,
            style="Sidebar.TButton"
        )
        settings_btn.pack(fill="x", pady=2)
        
        # Separador
        ttk.Separator(self.sidebar, orient="horizontal").pack(fill="x", pady=10)
        
        # Botón de cerrar sesión en la parte inferior
        logout_btn = ttk.Button(
            self.sidebar, 
            text=self.i18n.get("logout"), 
            command=self.confirm_logout,
            style="Error.TButton"
        )
        logout_btn.pack(side="bottom", fill="x", pady=(10, 0))
    
    def clear_content(self):
        # Limpiar el frame de contenido
        for widget in self.content.winfo_children():
            widget.destroy()
    
    def show_dashboard(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("dashboard"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido del dashboard
        dashboard_frame = ttk.Frame(self.content, padding=20)
        dashboard_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Mensaje de bienvenida
        welcome_frame = ttk.Frame(dashboard_frame, style="Card.TFrame", padding=20)
        welcome_frame.pack(fill="x", pady=(0, 20))
        
        welcome_title = ttk.Label(
            welcome_frame, 
            text=f"{self.i18n.get('welcome_back')}, {self.controller.current_user}!",
            font=("Helvetica", 16, "bold")
        )
        welcome_title.pack(anchor="w")
        
        welcome_message = ttk.Label(
            welcome_frame, 
            text=self.i18n.get("welcome_message"),
            font=("Helvetica", 10)
        )
        welcome_message.pack(anchor="w", pady=(5, 0))
        
        # Accesos rápidos
        shortcuts_frame = ttk.LabelFrame(dashboard_frame, text=self.i18n.get("quick_access"))
        shortcuts_frame.pack(fill="x", pady=(0, 20))
        
        shortcuts_content = ttk.Frame(shortcuts_frame, padding=10)
        shortcuts_content.pack(fill="x")
        
        # Configurar grid para accesos rápidos
        shortcuts_content.columnconfigure(0, weight=1)
        shortcuts_content.columnconfigure(1, weight=1)
        
        # Botón para registrar asistencia
        record_btn = ttk.Button(
            shortcuts_content, 
            text=self.i18n.get("record_attendance"), 
            command=self.show_attendance,
            padding=10
        )
        record_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        # Botón para ver reportes
        reports_btn = ttk.Button(
            shortcuts_content, 
            text=self.i18n.get("reports"), 
            command=self.show_reports,
            padding=10
        )
        reports_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Actividad reciente
        recent_frame = ttk.LabelFrame(dashboard_frame, text=self.i18n.get("recent_activity"))
        recent_frame.pack(fill="both", expand=True, pady=10)
        
        # Tabla de actividad reciente
        columns = ("date", "student", "status")
        self.recent_tree = ttk.Treeview(recent_frame, columns=columns, show="headings", height=10)
        
        # Definir encabezados
        self.recent_tree.heading("date", text=self.i18n.get("date"))
        self.recent_tree.heading("student", text=self.i18n.get("student"))
        self.recent_tree.heading("status", text=self.i18n.get("status"))
        
        # Configurar columnas
        self.recent_tree.column("date", width=150)
        self.recent_tree.column("student", width=150)
        self.recent_tree.column("status", width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(recent_frame, orient="vertical", command=self.recent_tree.yview)
        self.recent_tree.configure(yscrollcommand=scrollbar.set)
        
        # Empaquetar
        self.recent_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Cargar datos recientes
        self.load_recent_activity()
    
    def load_recent_activity(self):
        # Limpiar tabla
        for item in self.recent_tree.get_children():
            self.recent_tree.delete(item)
        
        # Cargar datos de asistencia
        attendance_data = load_attendance()
        
        # Convertir a lista para ordenar
        all_records = []
        for date, records in attendance_data["attendance"].items():
            for student, status in records.items():
                all_records.append((date, student, status))
        
        # Ordenar por fecha (más reciente primero)
        all_records.sort(reverse=True)
        
        # Mostrar solo los 10 más recientes
        for i, (date, student, status) in enumerate(all_records[:10]):
            self.recent_tree.insert("", "end", values=(date, student, status))
    
    def show_attendance(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("attendance_management"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido de asistencia
        attendance_frame = ttk.Frame(self.content, padding=20)
        attendance_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Marco para registrar asistencia
        record_frame = ttk.LabelFrame(attendance_frame, text=self.i18n.get("record_attendance"))
        record_frame.pack(fill="x", pady=(0, 20))
        
        # Formulario para registrar asistencia
        form_frame = ttk.Frame(record_frame, padding=10)
        form_frame.pack(fill="x")
        
        # Fecha
        date_frame = ttk.Frame(form_frame)
        date_frame.pack(fill="x", pady=5)
        
        ttk.Label(date_frame, text=self.i18n.get("date")).pack(side="left", padx=(0, 10))
        date_entry = ttk.Entry(date_frame, textvariable=self.selected_date_var, width=15)
        date_entry.pack(side="left")
        
        # Botón para fecha actual
        today_button = ttk.Button(
            date_frame, 
            text=self.i18n.get("today"), 
            command=lambda: self.selected_date_var.set(datetime.now().strftime("%Y-%m-%d"))
        )
        today_button.pack(side="left", padx=5)
        
        # Estudiante
        student_frame = ttk.Frame(form_frame)
        student_frame.pack(fill="x", pady=5)
        
        ttk.Label(student_frame, text=self.i18n.get("student")).pack(side="left", padx=(0, 10))
        
        # Obtener lista de estudiantes
        students = self.get_students_list()
        student_combo = ttk.Combobox(student_frame, textvariable=self.student_var, values=students, state="readonly", width=20)
        student_combo.pack(side="left")
        
        # Estado
        status_frame = ttk.Frame(form_frame)
        status_frame.pack(fill="x", pady=5)
        
        ttk.Label(status_frame, text=self.i18n.get("status")).pack(side="left", padx=(0, 10))
        status_combo = ttk.Combobox(
            status_frame, 
            textvariable=self.status_var, 
            values=[self.i18n.get("present"), self.i18n.get("absent"), self.i18n.get("late")], 
            state="readonly",
            width=15
        )
        status_combo.pack(side="left")
        
        # Botón de registro
        button_frame = ttk.Frame(form_frame)
        button_frame.pack(fill="x", pady=10)
        
        record_button = ttk.Button(
            button_frame, 
            text=self.i18n.get("record_attendance"), 
            command=self.record_attendance,
            style="Success.TButton",
            padding=10
        )
        record_button.pack(side="right")
        
        # Marco para ver asistencia
        view_frame = ttk.LabelFrame(attendance_frame, text=self.i18n.get("view_attendance"))
        view_frame.pack(fill="both", expand=True)
        
        # Controles para ver asistencia
        controls_frame = ttk.Frame(view_frame, padding=10)
        controls_frame.pack(fill="x")
        
        view_button = ttk.Button(
            controls_frame, 
            text=self.i18n.get("view_attendance"), 
            command=self.view_attendance,
            padding=10
        )
        view_button.pack(side="left")
        
        # Tabla de asistencia
        table_frame = ttk.Frame(view_frame)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        columns = ("student", "status")
        self.attendance_tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        
        # Definir encabezados
        self.attendance_tree.heading("student", text=self.i18n.get("student"))
        self.attendance_tree.heading("status", text=self.i18n.get("status"))
        
        # Configurar columnas
        self.attendance_tree.column("student", width=150)
        self.attendance_tree.column("status", width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.attendance_tree.yview)
        self.attendance_tree.configure(yscrollcommand=scrollbar.set)
        
        # Empaquetar
        self.attendance_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Cargar asistencia del día actual
        self.view_attendance()
    
    def show_reports(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("reports"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido de reportes
        reports_frame = ttk.Frame(self.content, padding=20)
        reports_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Marco para estadísticas
        stats_frame = ttk.LabelFrame(reports_frame, text=self.i18n.get("statistics"))
        stats_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        # Botón para generar estadísticas
        generate_button = ttk.Button(
            stats_frame, 
            text=self.i18n.get("generate_statistics"), 
            command=self.generate_statistics,
            padding=10
        )
        generate_button.pack(padx=10, pady=10)
        
        # Área de texto para mostrar estadísticas con estilo
        self.stats_text = tk.Text(stats_frame, height=15, width=50, wrap="word", padx=10, pady=10)
        self.stats_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Configurar etiquetas para dar formato al texto
        self.stats_text.tag_configure("title", font=("Helvetica", 12, "bold"))
        self.stats_text.tag_configure("subtitle", font=("Helvetica", 10, "bold"))
        self.stats_text.tag_configure("normal", font=("Helvetica", 10))
        self.stats_text.tag_configure("highlight", font=("Helvetica", 10, "bold"), foreground="#3498db")
        
        # Marco para exportar
        export_frame = ttk.LabelFrame(reports_frame, text=self.i18n.get("export_data"))
        export_frame.pack(fill="x")
        
        export_button = ttk.Button(
            export_frame, 
            text=self.i18n.get("export_csv"), 
            command=self.export_csv,
            padding=10
        )
        export_button.pack(padx=10, pady=10)

    def show_pending_justifications(self):
        self.clear_content()

        pending = get_pending_justifications()
        frame = ttk.Frame(self.content, padding=20)
        frame.pack(fill="both", expand=True)

        columns = ("date", "student", "reason", "attachment")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.pack(fill="both", expand=True)

        for col in columns:
            tree.heading(col, text=col.capitalize())
            tree.column(col, width=150)

        for date, student, reason in pending:
            record = get_justification_status(date, student)
            attachment = record.get("attachment", "Sin archivo")
            tree.insert("", "end", values=(date, student, reason, attachment))

        def review_selected():
            item = tree.selection()
            if not item:
                messagebox.showwarning("Atención", "Seleccione una justificación")
                return
            values = tree.item(item)["values"]
            date, student_id = values[0], values[1]
            self.review_justification(date, student_id)


        ttk.Button(frame, text="Revisar Justificación", command=review_selected).pack()

    def review_justification(self, date, student_id):
        record = get_justification_status(date, student_id)
        if not record:
            messagebox.showerror("Error", "No se encontró la justificación")
            return

        top = tk.Toplevel(self)
        top.title("Revisar Justificación")
        top.geometry("400x400")

        ttk.Label(top, text=f"Estudiante: {student_id}").pack()
        ttk.Label(top, text=f"Fecha: {date}").pack()
        ttk.Label(top, text=f"Motivo: {record['reason']}").pack(pady=10)

        if record.get("attachment"):
            def open_attachment():
                os.startfile(record["attachment"])
            ttk.Button(top, text="Ver adjunto", command=open_attachment).pack()

        ttk.Label(top, text="Respuesta:").pack(pady=5)
        response_var = tk.StringVar()
        ttk.Entry(top, textvariable=response_var).pack(fill="x")

        def accept():
            respond_justification(date, student_id, "accepted", response_var.get())
            messagebox.showinfo("Éxito", "Justificación aceptada")
            top.destroy()

        def reject():
            respond_justification(date, student_id, "rejected", response_var.get())
            messagebox.showinfo("Éxito", "Justificación rechazada")
            top.destroy()

        ttk.Button(top, text="Aceptar", command=accept).pack(side="left", padx=10, pady=20)
        ttk.Button(top, text="Rechazar", command=reject).pack(side="right", padx=10, pady=20)

    def show_settings(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("settings"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido de configuración
        settings_frame = ttk.Frame(self.content, padding=20)
        settings_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Marco para preferencias
        pref_frame = ttk.LabelFrame(settings_frame, text=self.i18n.get("preferences"))
        pref_frame.pack(fill="x", pady=(0, 20))
        
        # Idioma
        lang_frame = ttk.Frame(pref_frame, padding=10)
        lang_frame.pack(fill="x")
        
        ttk.Label(lang_frame, text=self.i18n.get("language")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Obtener idioma actual
        config = load_config()
        current_lang = config["language"]
        
        # Combobox para idioma
        lang_var = tk.StringVar(value=current_lang)
        lang_combo = ttk.Combobox(
            lang_frame, 
            textvariable=lang_var, 
            values=["es", "en"], 
            state="readonly",
            width=10
        )
        lang_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Tema
        theme_frame = ttk.Frame(pref_frame, padding=10)
        theme_frame.pack(fill="x")
        
        ttk.Label(theme_frame, text=self.i18n.get("theme")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Obtener tema actual
        current_theme = config["theme"]
        
        # Combobox para tema
        theme_var = tk.StringVar(value=current_theme)
        theme_combo = ttk.Combobox(
            theme_frame, 
            textvariable=theme_var, 
            values=[self.i18n.get("light"), self.i18n.get("dark")], 
            state="readonly",
            width=10
        )
        theme_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Botón para guardar preferencias
        save_button = ttk.Button(
            pref_frame, 
            text=self.i18n.get("save"), 
            command=lambda: self.save_preferences(lang_var.get(), theme_var.get()),
            padding=10
        )
        save_button.pack(padx=10, pady=10, anchor="e")
        
        # Marco para cambiar contraseña
        password_frame = ttk.LabelFrame(settings_frame, text=self.i18n.get("change_password"))
        password_frame.pack(fill="x")
        
        # Formulario para cambiar contraseña
        pwd_form = ttk.Frame(password_frame, padding=10)
        pwd_form.pack(fill="x")
        
        # Configurar grid
        pwd_form.columnconfigure(0, weight=0)
        pwd_form.columnconfigure(1, weight=1)
        
        # Contraseña actual
        ttk.Label(pwd_form, text=self.i18n.get("current_password")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        current_pwd_var = tk.StringVar()
        current_pwd_entry = ttk.Entry(pwd_form, textvariable=current_pwd_var, show="•")
        current_pwd_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Nueva contraseña
        ttk.Label(pwd_form, text=self.i18n.get("new_password")).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        new_pwd_var = tk.StringVar()
        new_pwd_entry = ttk.Entry(pwd_form, textvariable=new_pwd_var, show="•")
        new_pwd_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Confirmar contraseña
        ttk.Label(pwd_form, text=self.i18n.get("confirm_password")).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        confirm_pwd_var = tk.StringVar()
        confirm_pwd_entry = ttk.Entry(pwd_form, textvariable=confirm_pwd_var, show="•")
        confirm_pwd_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        # Botón para cambiar contraseña
        change_pwd_button = ttk.Button(
            pwd_form, 
            text=self.i18n.get("change_password"), 
            command=lambda: self.change_password(
                current_pwd_var.get(),
                new_pwd_var.get(),
                confirm_pwd_var.get()
            ),
            padding=10
        )
        change_pwd_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="e")
    
    def save_preferences(self, language, theme):
        # Convertir tema de nombre mostrado a valor interno
        if theme == self.i18n.get("light"):
            theme_value = "light"
        elif theme == self.i18n.get("dark"):
            theme_value = "dark"
        else:
            theme_value = theme
        
        # Guardar configuración
        config = load_config()
        config["language"] = language
        config["theme"] = theme_value
        save_config(config)
        
        # Aplicar cambios
        self.controller.i18n.set_language(language)
        self.controller.theme_manager.set_theme(theme_value)
        
        # Mostrar mensaje de éxito
        messagebox.showinfo(
            self.i18n.get("success"), 
            self.i18n.get("preferences_saved")
        )
        
        # Recargar la aplicación para aplicar los cambios
        self.controller.reload_app()

        
    
    def get_students_list(self):
        users_data = load_users()
        students = []
        
        for user in users_data["users"]:
            if user["role"] == "student":
                students.append(user["username"])
        
        return students
    
    def record_attendance(self):
        date = self.selected_date_var.get()
        student = self.student_var.get()
        status = self.status_var.get()
        
        # Validar datos
        if not date or not student or not status:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("complete_fields"))
            return
        
        # Validar formato de fecha
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("invalid_date"))
            return
        
        # Registrar asistencia
        success = record_attendance(date, student, status)
        
        if success:
            messagebox.showinfo(self.i18n.get("success"), self.i18n.get("record_updated"))
            # Actualizar tabla si se está viendo la misma fecha
            self.view_attendance()
        else:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("update_failed"))
    
    def view_attendance(self):
        date = self.selected_date_var.get()
        
        # Validar formato de fecha
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("invalid_date"))
            return
        
        # Limpiar tabla
        for item in self.attendance_tree.get_children():
            self.attendance_tree.delete(item)
        
        # Cargar asistencia
        attendance_records = get_date_attendance(date)
        
        if not attendance_records:
            messagebox.showinfo(self.i18n.get("info"), self.i18n.get("no_records"))
            return
        
        for student, status in attendance_records.items():
            self.attendance_tree.insert("", "end", values=(student, status))
    
    def generate_statistics(self):
        attendance_data = load_attendance()
        
        if not attendance_data["attendance"]:
            messagebox.showinfo(self.i18n.get("info"), self.i18n.get("no_attendance_data"))
            return
        
        # Limpiar área de texto
        self.stats_text.delete(1.0, tk.END)
        
        # Calcular estadísticas
        total_days = len(attendance_data["attendance"])
        
        # Obtener todos los estudiantes
        all_students = set()
        for date_records in attendance_data["attendance"].values():
            all_students.update(date_records.keys())
        
        total_students = len(all_students)
        
        # Calcular asistencia por estudiante
        student_stats = {}
        
        for student in all_students:
            present = 0
            absent = 0
            late = 0
            
            for date, records in attendance_data["attendance"].items():
                if student in records:
                    status = records[student]
                    if status == self.i18n.get("present"):
                        present += 1
                    elif status == self.i18n.get("absent"):
                        absent += 1
                    elif status == self.i18n.get("late"):
                        late += 1
            
            student_stats[student] = {
                "present": present,
                "absent": absent,
                "late": late,
                "attendance_rate": round((present / total_days) * 100, 2) if total_days > 0 else 0
            }
        
        # Mostrar estadísticas generales
        self.stats_text.insert(tk.END, f"{self.i18n.get('total_days')}: {total_days}\n", "title")
        self.stats_text.insert(tk.END, f"{self.i18n.get('total_students')}: {total_students}\n\n", "title")
        
        # Mostrar estadísticas por estudiante
        self.stats_text.insert(tk.END, f"{self.i18n.get('student_statistics')}:\n", "subtitle")
        self.stats_text.insert(tk.END, "-" * 50 + "\n", "normal")
        
        for student, stats in student_stats.items():
            self.stats_text.insert(tk.END, f"{self.i18n.get('student')}: {student}\n", "subtitle")
            self.stats_text.insert(tk.END, f"  {self.i18n.get('present_days')}: {stats['present']}\n", "normal")
            self.stats_text.insert(tk.END, f"  {self.i18n.get('absent_days')}: {stats['absent']}\n", "normal")
            self.stats_text.insert(tk.END, f"  {self.i18n.get('late_days')}: {stats['late']}\n", "normal")
            self.stats_text.insert(tk.END, f"  {self.i18n.get('attendance_rate')}: {stats['attendance_rate']}%\n", "highlight")
            self.stats_text.insert(tk.END, "-" * 50 + "\n", "normal")
    
    def export_csv(self):
        # Solicitar ubicación para guardar
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[(self.i18n.get("csv_files"), "*.csv"), (self.i18n.get("all_files"), "*.*")],
            title=self.i18n.get("save_as_csv")
        )
        
        if not filename:
            return
        
        success, message_key = export_to_csv(filename)
        
        if success:
            messagebox.showinfo(self.i18n.get("success"), self.i18n.get(message_key))
        else:
            messagebox.showerror(self.i18n.get("error"), message_key)
    
    def change_password(self, current_pwd, new_pwd, confirm_pwd):
        # Validar que las contraseñas no estén vacías
        if not current_pwd or not new_pwd or not confirm_pwd:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("complete_fields")
            )
            return
        
        # Validar que la nueva contraseña y la confirmación coincidan
        if new_pwd != confirm_pwd:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("passwords_not_match")
            )
            return
        
        # Validar longitud de la contraseña
        if len(new_pwd) < 6:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("password_length")
            )
            return
        
        # Verificar contraseña actual
        users_data = load_users()
        current_user = self.controller.current_user
        
        user_found = False
        for user in users_data["users"]:
            if user["username"] == current_user:
                user_found = True
                if user["password"] == hash_password(current_pwd):
                    # Cambiar contraseña
                    user["password"] = hash_password(new_pwd)
                    save_users(users_data)
                    messagebox.showinfo(
                        self.i18n.get("success"), 
                        self.i18n.get("password_changed")
                    )
                    return
                else:
                    messagebox.showerror(
                        self.i18n.get("error"), 
                        self.i18n.get("invalid_credentials")
                    )
                    return
        
        if not user_found:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("user_not_found")
            )
    
    def confirm_logout(self):
        result = messagebox.askyesno(
            self.i18n.get("confirm"), 
            self.i18n.get("confirm_logout")
        )
        
        if result:
            self.controller.logout()

# ==========================================
# CONFIGURACIÓN DE INTERFAZ DE USUARIO PARA ESTUDIANTES
# ==========================================

class StudentDashboard(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.i18n = controller.i18n
        
        # Widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Crear layout principal con sidebar y contenido
        self.main_paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.main_paned.pack(fill="both", expand=True)
        
        # Sidebar
        self.sidebar = ttk.Frame(self.main_paned, style="Card.TFrame", padding=10)
        self.main_paned.add(self.sidebar, weight=1)
        
        # Contenido principal
        self.content = ttk.Frame(self.main_paned)
        self.main_paned.add(self.content, weight=4)
        
        # Configurar sidebar
        self.setup_sidebar()
        
        # Configurar contenido inicial
        self.show_dashboard()
    
    def setup_sidebar(self):
        # Logo o avatar
        logo_frame = ttk.Frame(self.sidebar)
        logo_frame.pack(fill="x", pady=(0, 20))
        
        # Título del sistema
        system_name = ttk.Label(logo_frame, text="AMS", font=("Helvetica", 18, "bold"))
        system_name.pack(side="left")
        
        # Información del usuario
        user_frame = ttk.Frame(self.sidebar)
        user_frame.pack(fill="x", pady=(0, 20))
        
        user_label = ttk.Label(user_frame, text=f"{self.i18n.get('student')}: {self.controller.current_user}", font=("Helvetica", 10))
        user_label.pack(anchor="w")
        
        # Separador
        ttk.Separator(self.sidebar, orient="horizontal").pack(fill="x", pady=10)
        
        # Menú de navegación
        nav_frame = ttk.Frame(self.sidebar)
        nav_frame.pack(fill="x")
        
        # Estilo para botones de navegación
        button_style = {"font": ("Helvetica", 11), "anchor": "w", "padding": (10, 5)}
        
        # Botones de navegación
        dashboard_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("dashboard"), 
            command=self.show_dashboard,
            style="Sidebar.TButton"
        )
        dashboard_btn.pack(fill="x", pady=2)
        
        attendance_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("my_attendance"), 
            command=self.show_attendance,
            style="Sidebar.TButton"
        )
        attendance_btn.pack(fill="x", pady=2)

        justify_btn = ttk.Button(
            nav_frame,
            text=self.i18n.get("record_attendance") + " / Justificar Falta",
            command=self.create_justification_form,
            style="Sidebar.TButton"
        )
        justify_btn.pack(fill="x", pady=2)

        just_btn = ttk.Button(
            nav_frame,
            text="Ver Justificaciones",
            command=self.show_my_justifications,
            style="Sidebar.TButton"
        )
        just_btn.pack(fill="x", pady=2)

        settings_btn = ttk.Button(
            nav_frame, 
            text=self.i18n.get("settings"), 
            command=self.show_settings,
            style="Sidebar.TButton"
        )
        settings_btn.pack(fill="x", pady=2)

        
        # Separador
        ttk.Separator(self.sidebar, orient="horizontal").pack(fill="x", pady=10)
        
        # Botón de cerrar sesión en la parte inferior
        logout_btn = ttk.Button(
            self.sidebar, 
            text=self.i18n.get("logout"), 
            command=self.confirm_logout,
            style="Error.TButton"
        )
        logout_btn.pack(side="bottom", fill="x", pady=(10, 0))
    
    def clear_content(self):
        # Limpiar el frame de contenido
        for widget in self.content.winfo_children():
            widget.destroy()
    
    def show_dashboard(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("dashboard"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido del dashboard
        dashboard_frame = ttk.Frame(self.content, padding=20)
        dashboard_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Mensaje de bienvenida
        welcome_frame = ttk.Frame(dashboard_frame, style="Card.TFrame", padding=20)
        welcome_frame.pack(fill="x", pady=(0, 20))
        
        welcome_title = ttk.Label(
            welcome_frame, 
            text=f"{self.i18n.get('welcome_back')}, {self.controller.current_user}!",
            font=("Helvetica", 16, "bold")
        )
        welcome_title.pack(anchor="w")
        
        welcome_message = ttk.Label(
            welcome_frame, 
            text=self.i18n.get("welcome_message"),
            font=("Helvetica", 10)
        )
        welcome_message.pack(anchor="w", pady=(5, 0))
        
        # Resumen de asistencia
        summary_frame = ttk.LabelFrame(dashboard_frame, text=self.i18n.get("attendance_summary"))
        summary_frame.pack(fill="x", pady=(0, 20))
        
        # Obtener estadísticas de asistencia
        student_records = get_student_attendance(self.controller.current_user)
        
        total_days = len(student_records)
        present = sum(1 for status in student_records.values() if status == self.i18n.get("present"))
        absent = sum(1 for status in student_records.values() if status == self.i18n.get("absent"))
        late = sum(1 for status in student_records.values() if status == self.i18n.get("late"))
        
        attendance_rate = round((present / total_days) * 100, 2) if total_days > 0 else 0
        
        # Mostrar estadísticas en tarjetas
        stats_frame = ttk.Frame(summary_frame, padding=10)
        stats_frame.pack(fill="x")
        
        # Configurar grid para estadísticas
        stats_frame.columnconfigure(0, weight=1)
        stats_frame.columnconfigure(1, weight=1)
        stats_frame.columnconfigure(2, weight=1)
        stats_frame.columnconfigure(3, weight=1)
        
        # Tarjeta de días totales
        total_card = ttk.Frame(stats_frame, style="Card.TFrame", padding=10)
        total_card.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        ttk.Label(total_card, text=self.i18n.get("total_days"), font=("Helvetica", 10, "bold")).pack(anchor="w")
        ttk.Label(total_card, text=str(total_days), font=("Helvetica", 18)).pack(anchor="w", pady=5)
        
        # Tarjeta de días presente
        present_card = ttk.Frame(stats_frame, style="Card.TFrame", padding=10)
        present_card.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        ttk.Label(present_card, text=self.i18n.get("present_days"), font=("Helvetica", 10, "bold")).pack(anchor="w")
        ttk.Label(present_card, text=str(present), font=("Helvetica", 18)).pack(anchor="w", pady=5)
        
        # Tarjeta de días ausente
        absent_card = ttk.Frame(stats_frame, style="Card.TFrame", padding=10)
        absent_card.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        
        ttk.Label(absent_card, text=self.i18n.get("absent_days"), font=("Helvetica", 10, "bold")).pack(anchor="w")
        ttk.Label(absent_card, text=str(absent), font=("Helvetica", 18)).pack(anchor="w", pady=5)
        
        # Tarjeta de tasa de asistencia
        rate_card = ttk.Frame(stats_frame, style="Card.TFrame", padding=10)
        rate_card.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        
        ttk.Label(rate_card, text=self.i18n.get("attendance_rate"), font=("Helvetica", 10, "bold")).pack(anchor="w")
        ttk.Label(rate_card, text=f"{attendance_rate}%", font=("Helvetica", 18)).pack(anchor="w", pady=5)
        
        # Accesos rápidos
        shortcuts_frame = ttk.LabelFrame(dashboard_frame, text=self.i18n.get("quick_access"))
        shortcuts_frame.pack(fill="x")
        
        shortcuts_content = ttk.Frame(shortcuts_frame, padding=10)
        shortcuts_content.pack(fill="x")
        
        # Botón para ver asistencia
        view_btn = ttk.Button(
            shortcuts_content, 
            text=self.i18n.get("view_history"), 
            command=self.show_attendance,
            padding=10
        )
        view_btn.pack(fill="x", pady=5)
    
    def show_attendance(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("my_attendance"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido de asistencia
        attendance_frame = ttk.Frame(self.content, padding=20)
        attendance_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Marco para ver asistencia
        view_frame = ttk.LabelFrame(attendance_frame, text=self.i18n.get("attendance_history"))
        view_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        # Botón para ver asistencia
        view_button = ttk.Button(
            view_frame, 
            text=self.i18n.get("view_history"), 
            command=self.view_attendance,
            padding=10
        )
        view_button.pack(padx=10, pady=10)
        
        # Tabla de asistencia
        table_frame = ttk.Frame(view_frame)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        columns = ("date", "status")
        self.attendance_tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        
        # Definir encabezados
        self.attendance_tree.heading("date", text=self.i18n.get("date"))
        self.attendance_tree.heading("status", text=self.i18n.get("status"))
        
        # Configurar columnas
        self.attendance_tree.column("date", width=150)
        self.attendance_tree.column("status", width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.attendance_tree.yview)
        self.attendance_tree.configure(yscrollcommand=scrollbar.set)
        
        # Empaquetar
        self.attendance_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Marco para estadísticas
        stats_frame = ttk.LabelFrame(attendance_frame, text=self.i18n.get("my_statistics"))
        stats_frame.pack(fill="x")
        
        # Área de texto para mostrar estadísticas
        self.stats_text = tk.Text(stats_frame, height=8, width=50, wrap="word", padx=10, pady=10)
        self.stats_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Configurar etiquetas para dar formato al texto
        self.stats_text.tag_configure("title", font=("Helvetica", 12, "bold"))
        self.stats_text.tag_configure("normal", font=("Helvetica", 10))
        self.stats_text.tag_configure("highlight", font=("Helvetica", 10, "bold"), foreground="#3498db")
        
        # Cargar asistencia
        self.view_attendance()

    def create_justification_form(self):
        self.clear_content()

    # --- VERIFICAR JUSTIFICACIONES RESPONDIDAS ---
        data = load_justifications()["justifications"]
        user = self.controller.current_user
        notificados = 0

        for date, records in data.items():
            if user in records:
                status = records[user].get("status")
                response = records[user].get("response", "")
                if status in ["accepted", "rejected"] and response:
                    notificados += 1
                    messagebox.showinfo(
                        "Respuesta recibida",
                        f"Tu justificación del {date} fue '{status.upper()}'.\nComentario: {response}"
                    )

        if notificados == 0:
            print("[INFO] No hay nuevas respuestas.")

    # --- FORMULARIO DE ENVÍO DE JUSTIFICACIÓN ---
        self.just_date_var = tk.StringVar()
        self.just_reason_var = tk.StringVar()
        self.just_file_var = tk.StringVar()

        frame = ttk.Frame(self.content, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Fecha (YYYY-MM-DD):").pack(anchor="w")
        DateEntry(frame, textvariable=self.just_date_var, date_pattern="yyyy-mm-dd").pack(fill="x", pady=5)

        ttk.Label(frame, text="Motivo de la justificación:").pack(anchor="w")
        ttk.Entry(frame, textvariable=self.just_reason_var).pack(fill="x", pady=5)

        ttk.Label(frame, text="Archivo adjunto (opcional):").pack(anchor="w")
        file_frame = ttk.Frame(frame)
        file_frame.pack(fill="x", pady=5)
        ttk.Entry(file_frame, textvariable=self.just_file_var, state="readonly").pack(side="left", expand=True, fill="x")
        ttk.Button(file_frame, text="Examinar", command=self.select_file).pack(side="right")

        ttk.Button(frame, text="Enviar Justificación", command=self.submit_justification).pack(pady=10)


    def select_file(self):
        file_path = filedialog.askopenfilename(title="Seleccionar archivo")
        if file_path:
            self.just_file_var.set(file_path)

    def submit_justification(self):
        date = self.just_date_var.get()
        reason = self.just_reason_var.get()
        file_path = self.just_file_var.get()
        student_id = self.controller.current_user

    # Copiar archivo a carpeta 'attachments'
        dest_path = None
        if file_path:
            os.makedirs("attachments", exist_ok=True)
            file_name = os.path.basename(file_path)
            dest_path = os.path.join("attachments", f"{student_id}_{date}_{file_name}")
            shutil.copy(file_path, dest_path)

        success = submit_justification(date, student_id, reason, dest_path)
        if success:
            messagebox.showinfo("Éxito", "Justificación enviada correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo enviar la justificación.")

    def show_my_justifications(self):
        self.clear_content()
        frame = ttk.Frame(self.content, padding=20)
        frame.pack(fill="both", expand=True)

        columns = ("date", "reason", "status", "response")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.pack(fill="both", expand=True)

        for col in columns:
            tree.heading(col, text=col.capitalize())
            tree.column(col, width=120)

        data = load_justifications()["justifications"]
        user = self.controller.current_user
        for date, records in data.items():
            if user in records:
                r = records[user]
                tree.insert("", "end", values=(date, r["reason"], r["status"], r["response"]))

    def show_settings(self):
        self.clear_content()
        
        # Título
        header_frame = ttk.Frame(self.content, style="Header.TFrame")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title = ttk.Label(header_frame, text=self.i18n.get("settings"), style="Header.TLabel")
        title.pack(side="left", padx=10, pady=10)
        
        # Contenido de configuración
        settings_frame = ttk.Frame(self.content, padding=20)
        settings_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Marco para preferencias
        pref_frame = ttk.LabelFrame(settings_frame, text=self.i18n.get("preferences"))
        pref_frame.pack(fill="x", pady=(0, 20))
        
        # Idioma
        lang_frame = ttk.Frame(pref_frame, padding=10)
        lang_frame.pack(fill="x")
        
        ttk.Label(lang_frame, text=self.i18n.get("language")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Obtener idioma actual
        config = load_config()
        current_lang = config["language"]
        
        # Combobox para idioma
        lang_var = tk.StringVar(value=current_lang)
        lang_combo = ttk.Combobox(
            lang_frame, 
            textvariable=lang_var, 
            values=["es", "en"], 
            state="readonly",
            width=10
        )
        lang_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Tema
        theme_frame = ttk.Frame(pref_frame, padding=10)
        theme_frame.pack(fill="x")
        
        ttk.Label(theme_frame, text=self.i18n.get("theme")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Obtener tema actual
        current_theme = config["theme"]
        
        # Combobox para tema
        theme_var = tk.StringVar(value=current_theme)
        theme_combo = ttk.Combobox(
            theme_frame, 
            textvariable=theme_var, 
            values=[self.i18n.get("light"), self.i18n.get("dark")], 
            state="readonly",
            width=10
        )
        theme_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Botón para guardar preferencias
        save_button = ttk.Button(
            pref_frame, 
            text=self.i18n.get("save"), 
            command=lambda: self.save_preferences(lang_var.get(), theme_var.get()),
            padding=10
        )
        save_button.pack(padx=10, pady=10, anchor="e")
        
        # Marco para cambiar contraseña
        password_frame = ttk.LabelFrame(settings_frame, text=self.i18n.get("change_password"))
        password_frame.pack(fill="x")
        
        # Formulario para cambiar contraseña
        pwd_form = ttk.Frame(password_frame, padding=10)
        pwd_form.pack(fill="x")
        
        # Configurar grid
        pwd_form.columnconfigure(0, weight=0)
        pwd_form.columnconfigure(1, weight=1)
        
        # Contraseña actual
        ttk.Label(pwd_form, text=self.i18n.get("current_password")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        current_pwd_var = tk.StringVar()
        current_pwd_entry = ttk.Entry(pwd_form, textvariable=current_pwd_var, show="•")
        current_pwd_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Nueva contraseña
        ttk.Label(pwd_form, text=self.i18n.get("new_password")).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        new_pwd_var = tk.StringVar()
        new_pwd_entry = ttk.Entry(pwd_form, textvariable=new_pwd_var, show="•")
        new_pwd_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Confirmar contraseña
        ttk.Label(pwd_form, text=self.i18n.get("confirm_password")).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        confirm_pwd_var = tk.StringVar()
        confirm_pwd_entry = ttk.Entry(pwd_form, textvariable=confirm_pwd_var, show="•")
        confirm_pwd_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        # Botón para cambiar contraseña
        change_pwd_button = ttk.Button(
            pwd_form, 
            text=self.i18n.get("change_password"), 
            command=lambda: self.change_password(
                current_pwd_var.get(),
                new_pwd_var.get(),
                confirm_pwd_var.get()
            ),
            padding=10
        )
        change_pwd_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="e")
    
    def save_preferences(self, language, theme):
        # Convertir tema de nombre mostrado a valor interno
        if theme == self.i18n.get("light"):
            theme_value = "light"
        elif theme == self.i18n.get("dark"):
            theme_value = "dark"
        else:
            theme_value = theme
        
        # Guardar configuración
        config = load_config()
        config["language"] = language
        config["theme"] = theme_value
        save_config(config)
        
        # Aplicar cambios
        self.controller.i18n.set_language(language)
        self.controller.theme_manager.set_theme(theme_value)
        
        # Mostrar mensaje de éxito
        messagebox.showinfo(
            self.i18n.get("success"), 
            self.i18n.get("preferences_saved")
        )
        
        # Recargar la aplicación para aplicar los cambios
        self.controller.reload_app()
    
    def view_attendance(self):
        # Limpiar tabla
        for item in self.attendance_tree.get_children():
            self.attendance_tree.delete(item)
        
        # Cargar asistencia
        student_records = get_student_attendance(self.controller.current_user)
        
        if not student_records:
            messagebox.showinfo(self.i18n.get("info"), self.i18n.get("no_records"))
            return
        
        # Ordenar por fecha
        sorted_dates = sorted(student_records.keys(), reverse=True)
        
        for date in sorted_dates:
            status = student_records[date]
            self.attendance_tree.insert("", "end", values=(date, status))
        
        # Calcular estadísticas
        self.calculate_statistics(student_records)
    
    def calculate_statistics(self, records):
        # Limpiar área de texto
        self.stats_text.delete(1.0, tk.END)
        
        # Calcular estadísticas
        total_days = len(records)
        present = sum(1 for status in records.values() if status == self.i18n.get("present"))
        absent = sum(1 for status in records.values() if status == self.i18n.get("absent"))
        late = sum(1 for status in records.values() if status == self.i18n.get("late"))
        
        attendance_rate = round((present / total_days) * 100, 2) if total_days > 0 else 0
        
        # Mostrar estadísticas
        self.stats_text.insert(tk.END, f"{self.i18n.get('total_days')}: {total_days}\n", "title")
        self.stats_text.insert(tk.END, f"{self.i18n.get('present_days')}: {present}\n", "normal")
        self.stats_text.insert(tk.END, f"{self.i18n.get('absent_days')}: {absent}\n", "normal")
        self.stats_text.insert(tk.END, f"{self.i18n.get('late_days')}: {late}\n", "normal")
        self.stats_text.insert(tk.END, f"{self.i18n.get('attendance_rate')}: {attendance_rate}%\n", "highlight")
    
    def change_password(self, current_pwd, new_pwd, confirm_pwd):
        # Validar que las contraseñas no estén vacías
        if not current_pwd or not new_pwd or not confirm_pwd:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("complete_fields")
            )
            return
        
        # Validar que la nueva contraseña y la confirmación coincidan
        if new_pwd != confirm_pwd:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("passwords_not_match")
            )
            return
        
        # Validar longitud de la contraseña
        if len(new_pwd) < 6:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("password_length")
            )
            return
        
        # Verificar contraseña actual
        users_data = load_users()
        current_user = self.controller.current_user
        
        user_found = False
        for user in users_data["users"]:
            if user["username"] == current_user:
                user_found = True
                if user["password"] == hash_password(current_pwd):
                    # Cambiar contraseña
                    user["password"] = hash_password(new_pwd)
                    save_users(users_data)
                    messagebox.showinfo(
                        self.i18n.get("success"), 
                        self.i18n.get("password_changed")
                    )
                    return
                else:
                    messagebox.showerror(
                        self.i18n.get("error"), 
                        self.i18n.get("invalid_credentials")
                    )
                    return
        
        if not user_found:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("user_not_found")
            )
    
    def confirm_logout(self):
        result = messagebox.askyesno(
            self.i18n.get("confirm"), 
            self.i18n.get("confirm_logout")
        )
        
        if result:
            self.controller.logout()

# ==========================================
# CONFIGURACIÓN DE INTERFAZ DE USUARIO PARA ASISTENCIA
# ==========================================

class SetupWizard(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.i18n = controller.i18n
        
        # Variables
        self.admin_username_var = tk.StringVar()
        self.admin_password_var = tk.StringVar()
        self.language_var = tk.StringVar(value="es")
        self.theme_var = tk.StringVar(value=self.i18n.get("light"))
        
        # Widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Contenedor principal con padding
        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(fill="both", expand=True)
        
        # Título con animación
        self.title_label = ttk.Label(main_frame, text="", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=(0, 30))
        
        # Iniciar animación de escritura después de un breve retraso
        self.after(500, lambda: AnimationManager.typewriter(
            self.title_label, 
            self.i18n.get("initial_setup"), 
            delay=50
        ))
        
        # Marco de configuración con efecto de elevación
        setup_frame = ttk.Frame(main_frame, style="Card.TFrame")
        setup_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Padding interno
        inner_frame = ttk.Frame(setup_frame, padding=20)
        inner_frame.pack(fill="both", expand=True)
        
        # Administrador
        admin_frame = ttk.LabelFrame(inner_frame, text=self.i18n.get("create_admin"))
        admin_frame.pack(fill="x", pady=(0, 20))
        
        admin_form = ttk.Frame(admin_frame, padding=10)
        admin_form.pack(fill="x")
        
        # Configurar grid
        admin_form.columnconfigure(0, weight=0)
        admin_form.columnconfigure(1, weight=1)
        
        # Usuario
        ttk.Label(admin_form, text=self.i18n.get("username")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(admin_form, textvariable=self.admin_username_var).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Contraseña
        ttk.Label(admin_form, text=self.i18n.get("password")).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(admin_form, textvariable=self.admin_password_var, show="•").grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Preferencias
        pref_frame = ttk.LabelFrame(inner_frame, text=self.i18n.get("preferences"))
        pref_frame.pack(fill="x")
        
        pref_form = ttk.Frame(pref_frame, padding=10)
        pref_form.pack(fill="x")
        
        # Configurar grid
        pref_form.columnconfigure(0, weight=0)
        pref_form.columnconfigure(1, weight=1)
        
        # Idioma
        ttk.Label(pref_form, text=self.i18n.get("language")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Combobox(pref_form, textvariable=self.language_var, values=["es", "en"], state="readonly").grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Tema
        ttk.Label(pref_form, text=self.i18n.get("theme")).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Combobox(pref_form, textvariable=self.theme_var, values=[self.i18n.get("light"), self.i18n.get("dark")], state="readonly").grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Botón de finalizar
        button_frame = ttk.Frame(inner_frame)
        button_frame.pack(fill="x", pady=(20, 0))
        
        finish_button = ttk.Button(
            button_frame, 
            text=self.i18n.get("finish_setup"), 
            command=self.finish_setup,
            style="Success.TButton",
            padding=10
        )
        finish_button.pack(side="right")
        
    def finish_setup(self):
        admin_username = self.admin_username_var.get()
        admin_password = self.admin_password_var.get()
        language = self.language_var.get()
        
        # Convertir tema de nombre mostrado a valor interno
        theme_display = self.theme_var.get()
        if theme_display == self.i18n.get("light"):
            theme = "light"
        elif theme_display == self.i18n.get("dark"):
            theme = "dark"
        else:
            theme = theme_display
        
        # Validar datos
        if not admin_username or not admin_password:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("complete_admin_fields"))
            return
        
        # Validar nombre de usuario (solo letras, números y guiones bajos)
        if not re.match(r'^[a-zA-Z0-9_]+$', admin_username):
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("invalid_username"))
            return
        
        # Validar contraseña (mínimo 6 caracteres)
        if len(admin_password) < 6:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get("password_length"))
            return
        
        # Crear administrador
        success, message_key = create_user(admin_username, admin_password, "admin")
        
        if not success:
            messagebox.showerror(self.i18n.get("error"), self.i18n.get(message_key))
            return
        
        # Guardar configuración
        config = load_config()
        config["language"] = language
        config["theme"] = theme
        config["admin_created"] = True
        save_config(config)
        
        # Aplicar configuración
        self.controller.i18n.set_language(language)
        self.controller.theme_manager.set_theme(theme)
        
        messagebox.showinfo(self.i18n.get("success"), self.i18n.get("setup_completed"))
        
        # Mostrar login
        self.controller.show_frame("LoginFrame")

# ==========================================
# CONFIGURACIÓN DE INTERFAZ DE USUARIO PARA ASISTENCIA
# ==========================================

class AttendanceApp(ThemedTk):
    def __init__(self):
        super().__init__(theme="arc")
        
        self.title("Sistema de Gestión de Asistencia")
        self.geometry("1000x700")
        self.minsize(800, 600)
        
        # Inicializar internacionalización
        self.i18n = I18n()
        
        # Inicializar gestor de temas
        self.theme_manager = ThemeManager(self)
        
        # Variables de sesión
        self.current_user = None
        self.current_role = None
        
        # Contenedor principal
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        
        # Diccionario de frames
        self.frames = {}
        
        # Crear frames
        for F in (LoginFrame, AdminDashboard, TeacherDashboard, StudentDashboard, SetupWizard):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Configurar grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Mostrar frame inicial
        self.check_initial_setup()
        
        # Aplicar tema
        self.theme_manager.apply_theme()
        
        # Actualizar título según el idioma
        self.update_title()
    
    def check_initial_setup(self):
        config = load_config()
        
        if not config["admin_created"]:
            self.show_frame("SetupWizard")
        else:
            self.show_frame("LoginFrame")
    
    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        
        # Efecto de transición
        self.update_idletasks()
        frame.update_idletasks()
        
        # Aplicar efecto de aparición gradual
        frame.tk_setPalette(background=self.theme_manager.themes[self.theme_manager.current_theme]["bg"])
        
        # Actualizar título según el frame actual
        if frame_name == "LoginFrame":
            self.title(self.i18n.get("app_title"))
        elif frame_name == "AdminDashboard":
            self.title(f"{self.i18n.get('app_title')} - {self.i18n.get('admin_panel')}")
        elif frame_name == "TeacherDashboard":
            self.title(f"{self.i18n.get('app_title')} - {self.i18n.get('teacher_panel')}")
        elif frame_name == "StudentDashboard":
            self.title(f"{self.i18n.get('app_title')} - {self.i18n.get('student_panel')}")
        elif frame_name == "SetupWizard":
            self.title(f"{self.i18n.get('app_title')} - {self.i18n.get('initial_setup')}")
    
    def logout(self):
        self.current_user = None
        self.current_role = None
        self.show_frame("LoginFrame")
    
    def update_title(self):
        self.title(self.i18n.get("app_title"))
    
    def reload_app(self):
        # Recrear frames con la nueva configuración
        container = next(iter([w for w in self.winfo_children() if isinstance(w, ttk.Frame)]), None)
        
        if container:
            # Limpiar frames existentes
            for frame in self.frames.values():
                frame.destroy()
            
            # Recrear frames
            self.frames = {}
            for F in (LoginFrame, AdminDashboard, TeacherDashboard, StudentDashboard, SetupWizard):
                frame = F(container, self)
                self.frames[F.__name__] = frame
                frame.grid(row=0, column=0, sticky="nsew")
            
            # Mostrar frame de login
            self.show_frame("LoginFrame")
        
        # Aplicar tema
        self.theme_manager.apply_theme()
        
        # Actualizar título
        self.update_title()

# Punto de entrada
if __name__ == "__main__":
    # Asegurar que existan los directorios necesarios
    os.makedirs(LANGUAGES_DIR, exist_ok=True)
    
    # Iniciar aplicación
    app = AttendanceApp()
    app.mainloop()

