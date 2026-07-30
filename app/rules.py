from app.models import FacturaMedica, DictamenAuditoria
from app.ai_auditor import analizar_coherencia_clinica

def evaluar_factura(factura: FacturaMedica) -> DictamenAuditoria:
    # 1. Reglas duras de auditoría algorítmica
    if factura.monto_reclamado > 500000:
        return DictamenAuditoria(
            status="procesado",
            factura_id=factura.id_factura,
            dictamen="RECHAZADA",
            motivo="El monto supera el tope máximo de aprobación automática ($500.000).",
            monto_evaluado=factura.monto_reclamado,
            analisis_ia="No requerido por rechazo administrativo previo."
        )

    # 2. Análisis Semántico con IA (Groq / Llama 3)
    resultado_ia = analizar_coherencia_clinica(factura)

    # 3. Lógica cruzada: Si la IA encuentra la justificación DÉBIL u objetada
    if "DÉBIL" in resultado_ia.upper() or "NO JUSTIFICADA" in resultado_ia.upper():
        dictamen_final = "OBSERVADA"
        motivo_final = "Sugerencia de objeción clínica por inconsistencia médica detectada por IA."
    else:
        dictamen_final = "APROBADA"
        motivo_final = "Sin objeciones preliminares."

    return DictamenAuditoria(
        status="procesado",
        factura_id=factura.id_factura,
        dictamen=dictamen_final,
        motivo=motivo_final,
        monto_evaluado=factura.monto_reclamado,
        analisis_ia=resultado_ia
    )