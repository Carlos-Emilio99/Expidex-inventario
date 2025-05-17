# Sistema de Gestión de Inventario – Expidex

Este proyecto es una plataforma web desarrollada con Django para Expidex. El sistema permite gestionar usuarios, productos e inventario de forma eficiente, conforme a un cronograma de entregas progresivas.

---

## 📦 Módulos incluidos en esta entrega (Lunes 19 de Mayo)

### ✅ Módulo de Usuarios
- Autenticación con login y logout.
- Roles definidos: Administrador, Operador, Consultor.
- Redirección a un Dashboard al iniciar sesión.
- Gestión de usuarios mediante panel de administración.

### ✅ Módulo de Productos
- Registro de productos con: nombre, código, categoría, unidad de medida y cantidad disponible.
- Administración completa desde el panel admin (agregado, edición, filtros y búsqueda).

### ✅ Módulo de Inventario (Versión base sin gestión de archivos)
- Registro de movimientos de inventario (entradas y salidas).
- Actualización automática del stock disponible.
- Visualización de movimientos en el panel admin.
- Asociación de usuario responsable, tipo de movimiento, fecha y observaciones.

---

## 🛠 Instalación y configuración

### 🔹 Requisitos:
- Python 3.10+
- Django 5.2.1
- Visual Studio Code
- Git

### 🔹 Pasos para desarrollo local:

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/expidex-inventario.git
   cd expidex-inventario
