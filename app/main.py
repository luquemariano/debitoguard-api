from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.models import FacturaMedica, DictamenAuditoria
from app.rules import evaluar_factura

app = FastAPI(
    title="DebitoGuard API",
    description="Pre-Auditor Algorítmico de Facturas Médicas con IA",
    version="0.1.0"
)

# Servir archivos estáticos (HTML, CSS, JS) desde la carpeta 'static'
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
async def serve_frontend():
    return FileResponse("static/index.html")

@app.post("/auditar-factura/", response_model=DictamenAuditoria)
def auditar_factura(factura: FacturaMedica):
    return evaluar_factura(factura)