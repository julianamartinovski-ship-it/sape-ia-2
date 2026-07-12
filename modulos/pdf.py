from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import datetime


def gerar_pdf_processo_enfermagem(texto):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    largura, altura = A4
    y = altura - 2 * cm

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(2 * cm, y, "SAPE IA 2.0")
    y -= 0.7 * cm

    pdf.setFont("Helvetica", 10)
    pdf.drawString(2 * cm, y, "Sistema de Apoio ao Processo de Enfermagem")
    y -= 0.5 * cm
    pdf.drawString(2 * cm, y, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    y -= 1 * cm

    pdf.setFont("Helvetica", 10)

    for linha in texto.split("\n"):
        if y < 2 * cm:
            pdf.showPage()
            y = altura - 2 * cm
            pdf.setFont("Helvetica", 10)

        if linha.strip().isupper() and linha.strip() != "":
            pdf.setFont("Helvetica-Bold", 11)
            pdf.drawString(2 * cm, y, linha[:95])
            pdf.setFont("Helvetica", 10)
        else:
            pdf.drawString(2 * cm, y, linha[:110])

        y -= 0.45 * cm

    pdf.save()
    buffer.seek(0)
    return buffer