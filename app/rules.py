from app.models import FacturaMedica, DictamenAuditoria
from app.ai_auditor import analizar_coherencia_clinica  # <-- Importamos el nuevo módulo

NOMENCLADOR_ARANCELES = {
    "420101": 20000.0,   # Consulta médica
    "180101": 45000.0,   # Ecografía abdominal
    "340201": 120000.0,  # Tomografía computada
}

def evaluar_factura(factura: FacturaMedica) -> DictamenAuditoria:
    resultado = "APROBADA"
    motivo = "Sin objeciones preliminares"

    # Regla 1: Validar si la práctica existe en el Nomenclador
    if factura.codigo_practica not in NOMENCLADOR_ARANCELES:
        return DictamenAuditoria(
            status="procesado",
            factura_id=factura.id_factura,
            dictamen="RECHAZADA",
            motivo=f"La práctica {factura.codigo_practica} no existe en el nomenclador convenido",
            monto_evaluado=factura.monto_reclamado,
            analisis_ia="No evaluado debido a rechazo por nomenclador"
        )

    # Regla 2: Validar sobreprecio
    precio_maximo = NOMENCLADOR_ARANCELES[factura.codigo_practica]
    if factura.monto_reclamado > precio_maximo:
        resultado = "OBSERVADA"
        motivo = f"Monto reclamado (${factura.monto_reclamado}) supera el arancel tope (${precio_maximo}) para la práctica {factura.codigo_practica}"

    # Regla 3: Diagnóstico obligatorio para la práctica 420101
    elif factura.codigo_practica == "420101" and not factura.diagnostico_cie10:
        resultado = "RECHAZADA"
        motivo = "La práctica 420101 requiere código de diagnóstico CIE-10 obligatorio"

    # Evaluamos la coherencia clínica mediante el módulo de IA
    evaluacion_ia = analizar_coherencia_clinica(factura)

    return DictamenAuditoria(
        status="procesado",
        factura_id=factura.id_factura,
        dictamen=resultado,
        motivo=motivo,
        monto_evaluado=factura.monto_reclamado,
        analisis_ia=evaluacion_ia  # <-- Retornamos el análisis del módulo IA
    )