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

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.12+ | FastAPI | Pydantic
* **IA / LLM:** Groq API (`llama-3.3-70b-versatile`)
* **Procesamiento de Documentos:** `pypdf` | `python-multipart`
* **Frontend:** HTML5 | CSS3 (Variables & Modern Layout) | JavaScript (Fetch API)
* **Control de Versiones:** Git | GitHub

---
<img width="717" height="590" alt="WhatsApp Image 2026-07-31 at 01 28 28" src="https://github.com/user-attachments/assets/8efa1cc8-4d43-4c0d-aee8-946a6dee96ca" />

## ⚙️ Instalación y Configuración Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/luquemariano/debitoguard-api.git](https://github.com/luquemariano/debitoguard-api.git)
   cd debitoguard-api
