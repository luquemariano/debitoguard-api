import os
from dotenv import load_dotenv
from google import genai
from app.models import FacturaMedica

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def analizar_coherencia_clinica(factura: FacturaMedica) -> str:
    """
    Consulta a la API de Gemini para auditar la coherencia semántica 
    entre el diagnóstico CIE-10, la prestación solicitada y el resumen clínico.
    """
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

    # Intentamos primero con gemini-2.0-flash y si no con gemini-2.0-flash-exp
    modelos_a_probar = ['gemini-2.0-flash', 'gemini-2.0-flash-exp']

    for modelo in modelos_a_probar:
        try:
            response = client.models.generate_content(
                model=modelo,
                contents=prompt,
            )
            return response.text.strip()
        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                return "IA Check (En espera): Límite de cuota gratuita alcanzado temporalmente. Reintentar en 1 minuto."
            # Si el modelo no se encuentra, el bucle prueba el siguiente
            continue

    return "No se pudo conectar con el modelo de IA. Verifique disponibilidad de modelos en su cuenta de Google AI Studio."