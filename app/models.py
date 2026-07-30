from pydantic import BaseModel, Field
from typing import Optional

class FacturaMedica(BaseModel):
    id_factura: str = Field(..., description="Identificador único de la factura", example="FAC-2026-001")
    afiliado_id: str = Field(..., description="ID o DNI del afiliado", example="38492011")
    codigo_practica: str = Field(..., description="Código del nomenclador médico", example="180101")
    monto_reclamado: float = Field(..., gt=0, description="Monto cobrado por el prestador", example=40000.0)
    diagnostico_cie10: Optional[str] = Field(None, description="Código CIE-10 del diagnóstico", example="K80.2")
    fecha_prestacion: str = Field(..., description="Fecha de realización (AAAA-MM-DD)", example="2026-03-15")
    resumen_clinico: Optional[str] = Field(None, description="Texto libre con el resumen del cuadro clínico", example="Paciente de 45 años ingresa con dolor agudo en hipocondrio derecho tras ingesta grasa.")

class DictamenAuditoria(BaseModel):
    status: str
    factura_id: str
    dictamen: str
    motivo: str
    monto_evaluado: float
    analisis_ia: Optional[str] = Field(None, description="Evaluación semántica generada por la IA")