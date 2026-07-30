from fastapi import FastAPI
from app.models import FacturaMedica, DictamenAuditoria
from app.rules import evaluar_factura

app = FastAPI(
    title="DebitoGuard API",
    description="Pre-Auditor Algorítmico de Facturas Médicas con IA",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"status": "ok", "system": "DebitoGuard API"}

@app.post("/auditar-factura/", response_model=DictamenAuditoria)
def auditar_factura(factura: FacturaMedica):
    # Delegamos toda la lógica de evaluación al módulo de reglas
    return evaluar_factura(factura)