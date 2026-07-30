from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.models import FacturaMedica, DictamenAuditoria
from app.rules import evaluar_factura
from app.ai_auditor import extraer_datos_desde_pdf

app = FastAPI(
    title="DebitoGuard API",
    description="Pre-Auditor Algorítmico de Facturas Médicas con IA",
    version="0.1.0"
)

os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
async def serve_frontend():
    return FileResponse("static/index.html")

@app.post("/auditar-factura/", response_model=DictamenAuditoria)
def auditar_factura(factura: FacturaMedica):
    return evaluar_factura(factura)

# NUEVO ENDPOINT: Recibe el archivo PDF y devuelve los datos extraídos
@app.post("/extraer-pdf/")
async def procesar_pdf(file: UploadFile = File(...)):
    contenido_bytes = await file.read()
    datos_extraidos = extraer_datos_desde_pdf(contenido_bytes)
    return datos_extraidos