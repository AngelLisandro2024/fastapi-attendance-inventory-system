from datetime import datetime
from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import StreamingResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Empleado, MarcajeAsistencia, RegistroInventario
from pdf_generator import generar_pdf_reporte

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vico code - Sistema de Control de Asistencia e Inventario")
templates = Jinja2Templates(directory="templates")


def seed_data(db: Session):
    """Base de datos limpia: sin nombres predeterminados."""
    pass


@app.on_event("startup")
def startup_event():
    db = next(get_db())
    seed_data(db)


@app.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    total_empleados = db.query(Empleado).count()
    total_asistencias = db.query(MarcajeAsistencia).count()
    total_inventario = db.query(RegistroInventario).count()
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "total_empleados": total_empleados,
            "total_asistencias": total_asistencias,
            "total_inventario": total_inventario,
        },
    )


@app.get("/empleados")
def empleados_view(request: Request, db: Session = Depends(get_db)):
    empleados = db.query(Empleado.id, Empleado.cedula, Empleado.nombre, Empleado.apellido, Empleado.cargo).all()
    return templates.TemplateResponse(
        request,
        "empleados.html",
        {
            "empleados": empleados,
        },
    )


@app.post("/empleados/registrar")
def registrar_empleado(
    cedula: str = Form(...),
    nombre: str = Form(...),
    apellido: str = Form(...),
    cargo: str = Form(...),
    db: Session = Depends(get_db),
):
    nuevo_empleado = Empleado(
        cedula=cedula,
        nombre=nombre,
        apellido=apellido,
        cargo=cargo
    )
    db.add(nuevo_empleado)
    db.commit()
    return RedirectResponse(url="/empleados", status_code=303)


@app.get("/asistencia")
def asistencia_view(request: Request, db: Session = Depends(get_db)):
    empleados = db.query(Empleado).all()
    marcajes = db.query(MarcajeAsistencia).order_by(MarcajeAsistencia.fecha_hora.desc()).all()
    return templates.TemplateResponse(
        request,
        "asistencia.html",
        {
            "empleados": empleados,
            "marcajes": marcajes,
        },
    )


@app.post("/asistencia/registrar")
def registrar_asistencia(
    empleado_id: int = Form(...),
    tipo_movimiento: str = Form(...),
    db: Session = Depends(get_db),
):
    nuevo_marcaje = MarcajeAsistencia(
        empleado_id=empleado_id,
        tipo=tipo_movimiento,
        fecha_hora=datetime.now()
    )
    db.add(nuevo_marcaje)
    db.commit()
    return RedirectResponse(url="/asistencia", status_code=303)


@app.get("/inventario")
def inventario_view(request: Request, db: Session = Depends(get_db)):
    empleados = db.query(Empleado).all()
    inventario = db.query(RegistroInventario).order_by(RegistroInventario.id.desc()).all()
    return templates.TemplateResponse(
        request,
        "inventario.html",
        {
            "empleados": empleados,
            "inventario": inventario,
        },
    )


@app.post("/inventario/registrar")
def registrar_inventario(
    item_nombre: str = Form(...),
    cantidad: int = Form(...),
    empleado_id: int = Form(...),
    fecha_entrada: str = Form(...),
    fecha_salida: str = Form(None),
    observacion: str = Form(None),
    db: Session = Depends(get_db),
):
    f_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%dT%H:%M") if fecha_entrada else datetime.now()
    f_salida = datetime.strptime(fecha_salida, "%Y-%m-%dT%H:%M") if fecha_salida and fecha_salida.strip() else None

    nuevo_movimiento = RegistroInventario(
        item_nombre=item_nombre,
        cantidad=cantidad,
        empleado_id=empleado_id,
        fecha_entrada=f_entrada,
        fecha_salida=f_salida,
        observacion=observacion,
    )
    db.add(nuevo_movimiento)
    db.commit()
    return RedirectResponse(url="/inventario", status_code=303)


@app.get("/reporte/pdf")
def descargar_pdf(db: Session = Depends(get_db)):
    empleados = db.query(Empleado).all()
    marcajes = db.query(MarcajeAsistencia).all()
    inventario = db.query(RegistroInventario).all()

    pdf_buffer = generar_pdf_reporte(empleados, marcajes, inventario)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=reporte_vico_code.pdf"},
    )