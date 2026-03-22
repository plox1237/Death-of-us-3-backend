from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_diagnoses_report(diagnoses: list):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    elements.append(Paragraph("Reporte de Usuarios", styles["Title"]))

    # Construir datos
    data = [["ID", "Nombre", "Edad"]]

    for d in diagnoses:
        data.append([d["id"], d["nombre"], d["edad"]])

    table = Table(data)
    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ]))

    elements.append(table)

    doc.build(elements)

    buffer.seek(0)
    return buffer