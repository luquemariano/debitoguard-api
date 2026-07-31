<img width="874" height="914" alt="Screenshot" src="https://github.com/user-attachments/assets/73a3b456-46f9-4614-a2aa-f3600484db35" />
<img width="717" height="590" alt="WhatsApp Image 2026-07-31 at 01 28 28" src="https://github.com/user-attachments/assets/8efa1cc8-4d43-4c0d-aee8-946a6dee96ca" />
<img width="710" height="591" alt="WhatsApp Image 2026-07-31 at 01 28 28 (1)" src="https://github.com/user-attachments/assets/a6084180-d219-4166-ab0e-148eb7b47a76" />
# 🛡️ DebitoGuard API
> **Sistema Inteligente de Pre-Auditoría de Facturas Médicas & Extracción de Órdenes con IA**

DebitoGuard es una API REST y solución analítica diseñada para el sector **HealthTech** (obras sociales, prepagas y sanatorios en Argentina). Evalúa de forma automática facturas y solicitudes de prestaciones médicas combinando **reglas de negocio administrativas** con **modelos de lenguaje (LLM)** para el análisis de coherencia clínica.

---

## 🚀 Características Principales

* **📄 OCR & Extracción Inteligente (PDF):** Procesa archivos PDF de órdenes médicas e extrae automáticamente el ID de factura, afiliado, código de práctica, CIE-10 y resumen clínico.
* **🧠 Auditoría Clínica con IA (Groq / Llama 3.3):** Evalúa si la práctica solicitada tiene una justificación médica sólida respecto al diagnóstico CIE-10 e historial del paciente.
* **⚡ Lógica Híbrida de Reglas (FastAPI + Pydantic):** Valida topes administrativos y montos máximos antes de consultar a la IA, optimizando costos de procesamiento.
* **💻 Dashboard Interactivo (Frontend Integrado):** Interfaz web responsive para carga manual o vía PDF con respuesta visual en tiempo real (APROBADA, OBSERVADA, RECHAZADA).

---

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.12+ | FastAPI | Pydantic
* **IA / LLM:** Groq API (`llama-3.3-70b-versatile`)
* **Procesamiento de Documentos:** `pypdf` | `python-multipart`
* **Frontend:** HTML5 | CSS3 (Variables & Modern Layout) | JavaScript (Fetch API)
* **Control de Versiones:** Git | GitHub

---

## ⚙️ Instalación y Configuración Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/luquemariano/debitoguard-api.git](https://github.com/luquemariano/debitoguard-api.git)
   cd debitoguard-api
