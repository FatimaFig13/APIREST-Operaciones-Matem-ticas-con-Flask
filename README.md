# API REST — Operaciones Matemáticas con Flask

API desarrollada con **Flask (Python)** que realiza operaciones aritméticas básicas: suma, resta, multiplicación y división mediante peticiones HTTP GET y POST.

---

## Requisitos Previos

- Python 3.x instalado → [python.org/downloads](https://www.python.org/downloads/)
- Git instalado → [git-scm.com](https://git-scm.com/)

---

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/api-matematicas.git
cd api-matematicas
```

### 2. Crear el entorno virtual

**Windows (CMD o PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

>  Sabrás que el entorno está activo cuando veas `(venv)` al inicio de tu terminal.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor

```bash
python app.py
```

El servidor estará corriendo en: `http://127.0.0.1:5000`

---

## Endpoints disponibles

### Métodos GET — Parámetros en la URL

| Ruta              | Operación      | Ejemplo de uso                        |
|-------------------|----------------|---------------------------------------|
| `/suma`           | a + b          | `/suma?a=10&b=5`                      |
| `/resta`          | a - b          | `/resta?a=10&b=5`                     |
| `/multiplicacion` | a × b          | `/multiplicacion?a=10&b=5`            |
| `/division`       | a ÷ b          | `/division?a=10&b=5`                  |

**Prueba directamente en tu navegador:**
```
http://127.0.0.1:5000/suma?a=10&b=5
http://127.0.0.1:5000/division?a=15&b=3
```

**Respuesta de ejemplo:**
```json
{
  "operacion": "suma",
  "a": 10.0,
  "b": 5.0,
  "resultado": 15.0
}
```

---

### Método POST — `/calcular`

Recibe los datos en formato JSON en el cuerpo de la petición.

**Body requerido:**
```json
{
  "a": 15,
  "b": 3,
  "operacion": "division"
}
```

> Los valores de `"operacion"` válidos son: `"suma"`, `"resta"`, `"multiplicacion"`, `"division"`

**Respuesta:**
```json
{
  "operacion": "division",
  "a": 15.0,
  "b": 3.0,
  "resultado": 5.0
}
```

---

## Cómo probar el endpoint POST

### Opción 1 — Windows CMD

```cmd
curl -X POST http://127.0.0.1:5000/calcular -H "Content-Type: application/json" -d "{\"a\": 15, \"b\": 3, \"operacion\": \"division\"}"
```

### Opción 2 — Windows PowerShell

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/calcular" -Method POST -ContentType "application/json" -Body '{"a": 15, "b": 3, "operacion": "division"}'
```

### Opción 3 — Linux / Mac (Terminal)

```bash
curl -X POST http://127.0.0.1:5000/calcular \
  -H "Content-Type: application/json" \
  -d '{"a": 15, "b": 3, "operacion": "division"}'
```
---

## Manejo de errores

| Situación                  | Código HTTP | Mensaje de respuesta                                 |
|----------------------------|-------------|------------------------------------------------------|
| División entre cero        | 400         | `"No se puede dividir entre cero"`                   |
| Parámetros no numéricos    | 400         | `"Parámetros inválidos. Usa números en 'a' y 'b'"`   |
| Operación no válida (POST) | 400         | `"Operación 'xyz' no válida"`                        |
| JSON mal formado (POST)    | 400         | `"JSON inválido. Envía: {'a': num, 'b': num, ...}"`  |
---

## Detener el servidor

Presiona `Ctrl + C` en la terminal donde está corriendo Flask.

## Desactivar el entorno virtual (cuando termines)

```bash
deactivate
```