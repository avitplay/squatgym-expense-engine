from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def build_expense_pdf_report(expenses, user_email: str) -> bytes:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Título del reporte
    elements.append(Paragraph("SquatGym - Executive Expense Audit Report", styles['Title']))
    elements.append(Paragraph(f"Audited by: {user_email}", styles['Normal']))
    elements.append(Spacer(1, 20))

    # Tabla de gastos
    data = [["ID", "Supplier", "Category", "Tax ID (CUIT)", "Amount ($)"]]
    total_amount = 0.0

    for exp in expenses:
        data.append([
            str(exp.id),
            exp.supplier_name,
            exp.category,
            exp.tax_id,
            f"${exp.amount:,.2f}"
        ])
        total_amount += exp.amount

    data.append(["", "", "", "TOTAL", f"${total_amount:,.2f}"])

    t = Table(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8FAFC')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))

    elements.append(t)
    doc.build(elements)
    
    buffer.seek(0)
    return buffer.getvalue()