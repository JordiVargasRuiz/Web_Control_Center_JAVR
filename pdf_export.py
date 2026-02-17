from reportlab.pdfgen import canvas

def exportar_pdf(datos):
    c = canvas.Canvas("reporte_monitor.pdf")

    y = 800
    c.drawString(200, y, "Reporte Web Monitor")

    for d in datos:
        y -= 20
        c.drawString(50, y, d)

    c.save()
