import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generar_pdf_reporte(empleados, marcajes, inventario):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, 
        pagesize=letter,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )
    elementos = []
    
    styles = getSampleStyleSheet()
    
    # Colores institucionales (Azul Vico Code)
    primary_color = colors.HexColor('#1e40af')
    dark_color = colors.HexColor('#1e293b')
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=primary_color,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        textColor=colors.HexColor('#64748b'),
        spaceAfter=15
    )
    
    heading_style = ParagraphStyle(
        'HeadingStyle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        textColor=dark_color,
        spaceBefore=12,
        spaceAfter=6
    )

    # Encabezado
    elementos.append(Paragraph("Vico code - Reporte General del Sistema", title_style))
    elementos.append(Paragraph("Control de Empleados, Asistencia e Inventario de Activos", subtitle_style))
    elementos.append(Spacer(1, 5))

    # Sección 1: Empleados
    elementos.append(Paragraph("1. Listado de Empleados", heading_style))
    emp_data = [["ID", "Cédula", "Nombre y Apellido", "Cargo"]]
    for emp in empleados:
        emp_data.append([str(emp.id), str(emp.cedula), f"{emp.nombre} {emp.apellido}", str(emp.cargo)])
    
    t_emp = Table(emp_data, colWidths=[30, 80, 240, 150])
    t_emp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dbeafe')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1e3a8a')),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
    ]))
    elementos.append(t_emp)
    elementos.append(Spacer(1, 10))

    # Sección 2: Asistencia
    elementos.append(Paragraph("2. Historial de Asistencia", heading_style))
    marc_data = [["Empleado", "Tipo de Marcaje", "Fecha y Hora"]]
    for m in marcajes:
        nombre_emp = f"{m.empleado.nombre} {m.empleado.apellido}" if m.empleado else "N/D"
        marc_data.append([nombre_emp, str(m.tipo), m.fecha_hora.strftime('%d/%m/%Y %I:%M %p')])
    
    t_marc = Table(marc_data, colWidths=[200, 100, 200])
    t_marc.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dbeafe')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1e3a8a')),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
    ]))
    elementos.append(t_marc)
    elementos.append(Spacer(1, 10))

    # Sección 3: Inventario
    elementos.append(Paragraph("3. Movimientos y Asignaciones de Inventario", heading_style))
    inv_data = [["Ítem", "Cant.", "Empleado Asignado", "F. Entrada", "F. Salida", "Estado"]]
    for inv in inventario:
        nombre_emp = f"{inv.empleado.nombre} {inv.empleado.apellido}" if inv.empleado else "N/D"
        f_entrada = inv.fecha_entrada.strftime('%d/%m/%Y %H:%M') if inv.fecha_entrada else "-"
        f_salida = inv.fecha_salida.strftime('%d/%m/%Y %H:%M') if inv.fecha_salida else "Pendiente"
        inv_data.append([
            str(inv.item_nombre), 
            str(inv.cantidad), 
            nombre_emp, 
            f_entrada, 
            f_salida, 
            str(inv.observacion or 'Asignado')
        ])
    
    t_inv = Table(inv_data, colWidths=[100, 35, 120, 85, 85, 75])
    t_inv.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dbeafe')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1e3a8a')),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7.5),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
    ]))
    elementos.append(t_inv)

    doc.build(elementos)
    buffer.seek(0)
    return buffer