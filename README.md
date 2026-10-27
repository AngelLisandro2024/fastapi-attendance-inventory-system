<div align="center">

# 📋 Vico Code — Sistema de Control de Asistencia e Inventario
### **Plataforma Full-Stack de Gestión de Personal, Marcajes y Activos con FastAPI**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38BDF8?style=for-the-badge&logo=tailwind-css&logoColor=white)
![ReportLab](https://img.shields.io/badge/ReportLab-F43F5E?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)

</div>

---

## 📖 Descripción del Proyecto

**Vico Code Attendance & Inventory System** es una aplicación web robusta orientada al control interno de organizaciones. Permite administrar el personal, registrar marcajes diarios de asistencia (entradas y salidas), gestionar la asignación de equipos o insumos de inventario, y generar reportes oficiales en formato PDF de manera dinámica.

---

## ✨ Características Principales

* 👥 **Gestión de Personal:** Registro y administración de empleados con control de cédula, nombres, apellidos y cargos institucionales.
* ⏰ **Control de Asistencia:** Registro de marcajes de entrada y salida vinculados en tiempo real al personal con historial cronológico ordenado.
* 📦 **Inventario y Asignaciones:** Control de insumos y equipos con seguimiento de cantidades, fechas de entrega/devolución y estados operativos.
* 📄 **Generación de Reportes PDF:** Exportación automatizada de todo el balance general del sistema (personal, asistencias e inventario) utilizando **ReportLab**.
* 🎨 **UI Moderna y Responsiva:** Interfaz optimizada utilizando plantillas modulares Jinja2 y componentes estilizados con **Tailwind CSS**.

---

## 🛠️ Stack Tecnológico

| Categoría | Tecnología |
| :--- | :--- |
| **Backend Framework** | Python 3, FastAPI, Uvicorn |
| **ORM & Database** | SQLAlchemy, SQLite3 |
| **Frontend & UI** | HTML5, Jinja2 (Template Inheritance), Tailwind CSS, FontAwesome |
| **Generación de Documentos** | ReportLab (PDF Streaming) |
| **Form Management** | `python-multipart` |

---

## 📂 Estructura del Proyecto

```text
fastapi-attendance-inventory-system/
├── templates/
│   ├── base.html         # Plantilla maestra con navegación y diseño global
│   ├── index.html        # Dashboard principal con estadísticas en vivo
│   ├── empleados.html    # Módulo de registro y listado de personal
│   ├── asistencia.html   # Módulo de control de entradas/salidas y bitácora
│   └── inventario.html   # Módulo de asignación y control de inventario
├── database.py           # Configuración del motor SQLite y sesión SQLAlchemy
├── models.py             # Definición de modelos relacionales (Empleados, Marcajes, Inventario)
├── pdf_generator.py      # Lógica de construcción y formato de reportes PDF con ReportLab
├── main.py               # Servidor FastAPI, rutas web y endpoints de redirección
└── requirements.txt      # Dependencias del proyecto

```
⚡ Instalación y Ejecución Local
Sigue estos pasos para poner en marcha el proyecto en tu máquina:

Clonar el repositorio:

Bash

git clone [https://github.com/AngelLisandro2024/fastapi-attendance-inventory-system.git](https://github.com/AngelLisandro2024/fastapi-attendance-inventory-system.git)

cd fastapi-attendance-inventory-system

Crear y activar el entorno virtual:

Bash

python3 -m venv venv

# En Windows:

venv\Scripts\activate

# En Linux/macOS:

source venv/bin/activate

Instalar dependencias:

Bash

pip install -r requirements.txt

Ejecutar el servidor con Uvicorn:

Bash

uvicorn main:app --reload

Abrir en el navegador:

Dashboard Principal: http://127.0.0.1:8000

Documentación Interactiva (Swagger UI): http://127.0.0.1:8000/docs

👨‍💻 Autor
Diseñado y desarrollado por Angel Fernández (@AngelLisandro2024).
