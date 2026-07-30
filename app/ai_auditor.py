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