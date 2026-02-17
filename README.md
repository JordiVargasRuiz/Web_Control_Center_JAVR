# Web Control Center

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](README.md)

## 📋 Descripción

**Web Control Center** es una aplicación de monitoreo en tiempo real de sitios web que te permite supervisar la disponibilidad, latencia y estado de múltiples servidores desde una interfaz gráfica intuitiva. Ideal para administradores de sistemas, DevOps y equipos de operaciones que necesitan mantener la visibilidad sobre la salud de sus infraestructuras web.
<img width="1000" height="751" alt="image" src="https://github.com/user-attachments/assets/82adeabe-834e-44c8-b004-b91bf22b7555" />

## ✨ Características

- 🔴 **Monitoreo en Tiempo Real**: Verifica continuamente el estado de sitios web
- ⚡ **Medición de Latencia**: Registra y visualiza tiempos de respuesta de servidores
- 📊 **Gráficas Interactivas**: Visualización dinámica de métricas de latencia con Matplotlib
- 📄 **Exportación a PDF**: Genera reportes detallados de monitoreo
- 🎨 **Interfaz Moderna**: UI oscura y profesional con CustomTkinter
- ⚙️ **Asincrónica**: Procesamiento paralelo de múltiples sitios sin bloqueos
- 📈 **Historial de Datos**: Mantiene registro de estadísticas para análisis

## 🛠️ Requisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)

## 📦 Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/usuario/Web_Control_Center.git
   cd Web_Control_Center
   ```

2. **Crear entorno virtual** (recomendado):
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/macOS:
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencias Principales

- **customtkinter**: Interfaz gráfica moderna
- **aiohttp**: Cliente HTTP asincrónico
- **matplotlib**: Visualización de gráficas
- **reportlab**: Generación de reportes PDF

## 🚀 Uso

### Iniciar la aplicación

```bash
python main.py
```

### Pasos básicos

1. **Agregar sitios**: Ingresa la URL del sitio web en el campo de texto y presiona "Agregar"
2. **Iniciar monitoreo**: Haz clic en el botón "Iniciar" para comenzar la supervisión
3. **Ver resultados**: 
   - Estado en tiempo real en el panel izquierdo
   - Gráficas de latencia actualizadas en tiempo real
   - Historial de eventos en el panel de logs
4. **Exportar reporte**: Genera un PDF con los datos recopilados
<img width="999" height="743" alt="image" src="https://github.com/user-attachments/assets/2f151503-53b8-4e5f-9aff-b3c32adb981c" />

## 📁 Estructura del Proyecto

```
Web_Control_Center/
├── main.py              # Aplicación principal y UI
├── monitor.py           # Lógica de monitoreo HTTP
├── charts.py            # Generación de gráficas
├── pdf_export.py        # Exportación de reportes PDF
├── requirements.txt     # Dependencias del proyecto
└── README.md           # Este archivo
```

### Descripción de Módulos

| Módulo | Descripción |
|--------|-------------|
| **main.py** | Aplicación principal con interfaz CustomTkinter, manejo de eventos y coordinación de módulos |
| **monitor.py** | Verificación asincrónica de disponibilidad y latencia de sitios web usando aiohttp |
| **charts.py** | Generación y actualización de gráficas de latencia integradas en la UI |
| **pdf_export.py** | Creación de reportes en formato PDF con ReportLab |

## 💻 Ejemplo de Uso

```python
# La aplicación se ejecuta de forma intuitiva a través de GUI
# Simplemente agrega URLs y presiona iniciar

# URLs de ejemplo:
# - https://google.com
# - https://github.com
# - https://ejemplo.local:8080
```
<img width="1000" height="750" alt="image" src="https://github.com/user-attachments/assets/9fb4176e-0d73-41f4-b55c-0f11f0db408d" />

## 🔧 Configuración

Puedes personalizar varios aspectos de la aplicación editando directamente `main.py`:

- **Tema**: Cambia `ctk.set_appearance_mode("dark")` por `"light"`
- **Color**: Modifica `ctk.set_default_color_theme("dark-blue")`
- **Tamaño de ventana**: Ajusta `app.geometry("1000x720")`
- **Timeout**: Modifica el valor en `timeout=5` en `monitor.py`

## 📊 Características Técnicas

- **Procesamiento Asincrónico**: Utiliza `asyncio` y `aiohttp` para monitorear múltiples sitios sin bloqueos
- **Threading**: Ejecuta el bucle de monitoreo en hilos separados para mantener la UI responsiva
- **Manejo de Errores**: Captura y reporta fallos de conexión de manera elegante
- **Estadísticas**: Calcula promedios y tendencias de latencia en tiempo real

## 📝 Logs y Reportes

- Los eventos se registran en la aplicación en tiempo real
- Los reportes PDF se generan automáticamente con timestamp
- El historial se mantiene en memoria durante la sesión
<img width="1002" height="748" alt="image" src="https://github.com/user-attachments/assets/a66050b8-9421-47ce-83c8-d62209920a0f" />


## 🐛 Troubleshooting

### La aplicación no inicia
```bash
# Verifica que todas las dependencias estén instaladas
pip install -r requirements.txt

# Verifica la versión de Python
python --version  # Debe ser 3.9 o superior
```

### No se conecta a sitios web
- Verifica tu conexión a internet
- Comprueba que las URLs sean válidas
- Algunos sitios pueden tener restricciones de CORS o bloqueo de bots

### Las gráficas no se actualizan
- Asegúrate de que hay datos disponibles (monitorea al menos 2-3 iteraciones)
- El historial se vacía cuando se reinicia la aplicación

## 🚧 Mejoras Futuras

- [ ] Base de datos para persistencia de datos
- [ ] Alertas por email/notificaciones
- [ ] Dashboard web
- [ ] API REST para integraciones
- [ ] Análisis histórico avanzado
- [ ] Soporte para webhooks personalizados

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Desarrollado como parte del curso de **Computación Tolerante**.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Contacto

Para preguntas o sugerencias, abre un issue en el repositorio.

---

**Última actualización**: Febrero 2026 | **Versión**: 1.0.0
