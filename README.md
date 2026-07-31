# 🛡️ DébitoGuard Health API

> **API de apoyo para la preauditoría administrativa de órdenes y facturación médica**

DébitoGuard Health API es una solución experimental de HealthTech desarrollada con Python y FastAPI para asistir en el análisis preliminar de documentación médica y administrativa.

La aplicación permite cargar información manualmente o extraer datos desde órdenes médicas en formato PDF. Luego aplica reglas de negocio configurables y utiliza inteligencia artificial para identificar posibles inconsistencias, generar observaciones y priorizar los casos que requieren revisión profesional.

Está orientada a problemáticas habituales de obras sociales, prepagas, clínicas, sanatorios y prestadores de salud de Argentina.

---
<img width="710" height="591" alt="WhatsApp Image 2026-07-31 at 01 28 28 (1)" src="https://github.com/user-attachments/assets/a6084180-d219-4166-ab0e-148eb7b47a76" />
<img width="874" height="914" alt="Screenshot" src="https://github.com/user-attachments/assets/73a3b456-46f9-4614-a2aa-f3600484db35" />

## 🚀 Características Principales

- **📄 Procesamiento de documentos:** permite cargar órdenes médicas en formato PDF y extraer los campos relevantes para su revisión.

- **🔎 Validaciones administrativas:** aplica reglas configurables sobre montos, códigos, documentación y datos obligatorios.

- **🧠 Análisis asistido por IA:** genera observaciones orientativas sobre la relación entre la información registrada, el diagnóstico informado y la práctica solicitada.

- **🚦 Priorización de casos:** clasifica las solicitudes según el nivel de revisión requerido.

- **📝 Resultados explicables:** informa qué reglas fueron aplicadas y cuáles fueron las observaciones detectadas.

- **💻 Interfaz web integrada:** permite realizar cargas manuales o documentales y consultar los resultados de manera visual. 

---

## ⚠️ Alcance y uso responsable

DébitoGuard Health API es un proyecto demostrativo orientado a la asistencia administrativa y no reemplaza la intervención de auditores médicos, profesionales de la salud ni responsables autorizados.

La aplicación:

- No realiza diagnósticos médicos.
- No prescribe tratamientos.
- No autoriza ni rechaza prestaciones de manera definitiva.
- No debe utilizarse como única fuente para tomar decisiones clínicas o administrativas.
- Requiere revisión humana antes de cualquier decisión real.

Los resultados generados mediante inteligencia artificial son orientativos y pueden contener errores.

## 👤 Supervisión humana

El flujo de trabajo está diseñado bajo un enfoque **human-in-the-loop**:

1. La aplicación recibe la información.
2. Se ejecutan validaciones automáticas.
3. La inteligencia artificial genera observaciones orientativas.
4. El resultado queda disponible para revisión.
5. Una persona autorizada toma la decisión final.

La aplicación busca reducir tareas repetitivas y mejorar la organización de la revisión, no reemplazar el criterio profesional.

## 🧪 Datos utilizados en la demostración

Todos los pacientes, prestadores, diagnósticos, órdenes, facturas e importes utilizados en este proyecto son ficticios o fueron creados específicamente para pruebas.

El proyecto no contiene datos reales de pacientes, afiliados, profesionales, instituciones ni organismos de salud.

Para probar la aplicación se recomienda utilizar únicamente información sintética y documentos preparados para demostración.

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.12+ | FastAPI | Pydantic
* **IA / LLM:** Groq API (`llama-3.3-70b-versatile`)
* **Procesamiento de Documentos:** `pypdf` | `python-multipart`
* **Frontend:** HTML5 | CSS3 (Variables & Modern Layout) | JavaScript (Fetch API)
* **Control de Versiones:** Git | GitHub

---
<img width="717" height="590" alt="WhatsApp Image 2026-07-31 at 01 28 28" src="https://github.com/user-attachments/assets/8efa1cc8-4d43-4c0d-aee8-946a6dee96ca" />


## ⚙️ Instalación y configuración local

### 1. Clonar el repositorio

```bash
git clone https://github.com/luquemariano/debitoguard-api.git
cd debitoguard-api
```

### 2. Crear un entorno virtual

En Windows PowerShell:

```powershell
py -m venv .venv
```

### 3. Activar el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando el entorno esté activo, la terminal debería mostrar `(.venv)` al comienzo de la línea.

Si PowerShell bloquea la activación, ejecutá una sola vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Luego volvé a ejecutar:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```powershell
py -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configurar la API key de Groq

El repositorio incluye un archivo de ejemplo llamado `.env.example`.

Creá una copia llamada `.env`:

```powershell
Copy-Item .env.example .env
```

Luego abrí el archivo `.env` y reemplazá:

```text
GROQ_API_KEY=tu_api_key_de_groq_aqui
```

por tu clave personal de Groq:

```text
GROQ_API_KEY=gsk_tu_clave_personal
```

> No publiques tu clave real en GitHub. El archivo `.env` debe permanecer excluido mediante `.gitignore`.

### 6. Ejecutar la aplicación

Desde la carpeta principal del proyecto:

```powershell
uvicorn app.main:app --reload
```

También podés utilizar:

```powershell
py -m uvicorn app.main:app --reload
```

### 7. Abrir DébitoGuard

Con el servidor funcionando, abrí en el navegador:

```text
http://127.0.0.1:8000
```

La documentación automática de la API estará disponible en:

```text
http://127.0.0.1:8000/docs
```

La documentación alternativa estará disponible en:

```text
http://127.0.0.1:8000/redoc
```

### 8. Detener el servidor

En la terminal donde está ejecutándose Uvicorn, presioná:

```text
Ctrl + C
```

## 📁 Estructura principal

```text
debitoguard-api/
├── app/
│   ├── __init__.py
│   ├── ai_auditor.py
│   ├── main.py
│   ├── models.py
│   └── rules.py
├── static/
│   └── index.html
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔐 Variables de entorno

La aplicación utiliza la siguiente variable:

| Variable | Descripción |
|---|---|
| `GROQ_API_KEY` | Clave necesaria para utilizar el análisis y la extracción documental mediante Groq |

La aplicación puede iniciar sin la clave configurada, pero las funciones de inteligencia artificial no estarán disponibles.
