import os
from dotenv import load_dotenv
from groq import Groq
from app.models import FacturaMedica

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key) if groq_api_key else None

def analizar_coherencia_clinica(factura: FacturaMedica) -> str:
    if not client:
        return "IA Check no configurado: Falta GROQ_API_KEY en el .env"

    if not factura.resumen_clinico:
        return "No se adjuntó resumen clínico para análisis semántico."

    prompt = f"""
    Actúa como un Auditor Médico experto en facturación de prestaciones sanitarias.
    
    Analiza la siguiente prestación:
    - Código de Práctica/Estudio: {factura.codigo_practica}
    - Diagnóstico CIE-10: {factura.diagnostico_cie10 if factura.diagnostico_cie10 else 'No especificado'}
    - Resumen Clínico presentado: "{factura.resumen_clinico}"
    
    Tarea:
    Determina si la práctica solicitada está clínica y médicamente justificada según el resumen presentado.
    
    Responde en un máximo de 2 oraciones concisas indicando:
    1. Si la justificación es SÓLIDA o DÉBIL.
    2. El motivo médico brevísimo.
    """

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error en IA Check: {str(e)}"


import json
from pypdf import PdfReader
from io import BytesIO

def extraer_datos_desde_pdf(pdf_bytes: bytes) -> dict:
    """
    Lee un archivo PDF, extrae su texto y usa Groq para convertirlo 
    en un objeto JSON estructurado con los datos de la factura.
    """
    if not client:
        return {"error": "GROQ_API_KEY no configurada."}

    try:
        # 1. Extraer texto plano del PDF
        reader = PdfReader(BytesIO(pdf_bytes))
        texto_pdf = ""
        for page in reader.pages:
            texto_pdf += page.extract_text() or ""

        if not texto_pdf.strip():
            return {"error": "No se pudo extraer texto del PDF (puede ser un escaneo o imagen)." }

        # 2. Prompt para pedir a Groq que ordene los datos en un JSON estricto
        prompt = f"""
        Actúa como un sistema de extracción de datos médicos.
        Lee el siguiente texto extraído de una orden médica/factura y extrae los campos requeridos.

        TEXTO DEL DOCUMENTO:
        \"\"\"
        {texto_pdf}
        \"\"\"

        REGLAS DE SALIDA:
        Devuelve ÚNICAMENTE un objeto JSON válido (sin Markdown, sin ```json ```, ni texto adicional) con esta estructura exacta:
        {{
            "id_factura": "ID o número de factura/orden si existe (de lo contrario 'FAC-AUTO-001')",
            "afiliado_id": "DNI o número de afiliado encontrado",
            "codigo_practica": "Código numérico de la práctica/estudio solicitado",
            "monto_reclamado": 0, (un número flotante/entero si existe, o 0 si no figura)
            "diagnostico_cie10": "Código CIE-10 (ej: J00, K80.2) o 'No especificado'",
            "resumen_clinico": "Texto breve resumiendo la historia clínica, síntomas e indicación médica expuesta en el documento"
        }}
        """

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.1
        )

        # 3. Convertir la respuesta de texto a diccionario Python
        contenido = response.choices[0].message.content.strip()
        return json.loads(contenido)

    except Exception as e:
        return {"error": f"Error procesando PDF: {str(e)}"}