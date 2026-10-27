from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Empleado(Base):
    __tablename__ = "empleados"

    id = Column(Integer, primary_order=True, primary_key=True, index=True)
    cedula = Column(String(20), unique=True, index=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    cargo = Column(String(100), nullable=False)

    # Relaciones
    marcajes = relationship("MarcajeAsistencia", back_populates="empleado")
    inventario = relationship("RegistroInventario", back_populates="empleado")


class MarcajeAsistencia(Base):
    __tablename__ = "marcajes_asistencia"

    id = Column(Integer, primary_key=True, index=True)
    empleado_id = Column(Integer, ForeignKey("empleados.id"), nullable=False)
    tipo = Column(String(20), nullable=False)  # 'Entrada' o 'Salida'
    fecha_hora = Column(DateTime, default=datetime.now, nullable=False)

    # Relación
    empleado = relationship("Empleado", back_populates="marcajes")


class RegistroInventario(Base):
    __tablename__ = "registro_inventario"

    id = Column(Integer, primary_key=True, index=True)
    item_nombre = Column(String(150), nullable=False)
    cantidad = Column(Integer, default=1, nullable=False)
    empleado_id = Column(Integer, ForeignKey("empleados.id"), nullable=False)
    fecha_entrada = Column(DateTime, nullable=False)
    fecha_salida = Column(DateTime, nullable=True)
    observacion = Column(String(255), nullable=True)

    # Relación
    empleado = relationship("Empleado", back_populates="inventario")