from io import BytesIO
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT

def generate_diagnoses_report(diagnoses: list):
    buffer = BytesIO()

    # Horizontal porque hay muchas columnas
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(letter),
        rightMargin=30,
        leftMargin=30,
        topMargin=40,
        bottomMargin=30
    )

    elements = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        name="TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        spaceAfter=10
    )

    date_style = ParagraphStyle(
        name="DateStyle",
        parent=styles["Normal"],
        alignment=TA_RIGHT,
        fontSize=9,
        textColor=colors.grey,
        spaceAfter=15
    )

    text_style = ParagraphStyle(
        name="TextStyle",
        parent=styles["Normal"],
        alignment=TA_JUSTIFY,
        leading=12,
        spaceAfter=15
    )

    # Fecha
    meses = [
        "enero","febrero","marzo","abril","mayo","junio",
        "julio","agosto","septiembre","octubre","noviembre","diciembre"
    ]
    now = datetime.now()
    fecha = f"{now.day} de {meses[now.month - 1]} de {now.year}"

    # Título y fecha
    elements.append(Paragraph("Reporte de Diagnósticos de Diabetes", title_style))
    elements.append(Paragraph(f"Fecha: {fecha}", date_style))

    # Introducción
    intro = """
    Este informe contiene los últimos diagnósticos registrados en el sistema de predicción de diabetes.
    Se incluyen variables clínicas relevantes utilizadas por el modelo para determinar el riesgo del paciente.
    """
    elements.append(Paragraph(intro, text_style))
    elements.append(Spacer(1, 10))

    # Encabezados de tabla
    data = [[
        "ID", "Usuario", "Embarazos", "Glucosa", "Presión",
        "Piel", "Insulina", "IMC", "DPF", "Edad", "Resultado"
    ]]

    # Datos
    for d in diagnoses:
        data.append([
            d["id"],
            d["user_id"],
            d["pregnancies"],
            d["glucose"],
            d["blood_pressure"],
            d["skin_thickness"],
            d["insulin"],
            round(d["bmi"], 2),
            round(d["dpf"], 3),
            d["age"],
            d["result"]
        ])

    table = Table(data, repeatRows=1)

    table.setStyle(TableStyle([
        # Header
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F618D")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),

        # Body
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8),
        ("ALIGN", (0, 1), (-1, -1), "CENTER"),

        # Padding
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),

        # Grid
        ("GRID", (0, 0), (-1, -1), 0.3, colors.grey),

        # Filas alternas
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey]),
    ]))

    elements.append(table)

    doc.build(elements)
    buffer.seek(0)

    return buffer