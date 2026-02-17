import customtkinter as ctk
import asyncio
import threading
import time

from monitor import monitor_sites
from charts import init_chart, actualizar_grafica
from pdf_export import exportar_pdf

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Web Control Center")
app.geometry("1000x720")

sites = []
logs = []

start_time = None
monitor_activo = False


def agregar_sitio():
    url = entry.get()

    if url:
        sites.append(url)
        textbox.insert("end", f"Agregado ✔ -> {url}\n")
        entry.delete(0, "end")


async def loop_monitor():
    global monitor_activo

    while monitor_activo:

        if sites:

            resultados = await monitor_sites(sites)

            for url, online, latency, status in resultados:

                if online:
                    msg = f"🟢 {url} -> ONLINE ({status}) | {latency}s"
                else:
                    msg = f"🔴 {url} -> OFFLINE"

                logs.append(msg)

                app.after(0, lambda m=msg: textbox.insert("end", m + "\n"))
                app.after(0, lambda: textbox.see("end"))

            app.after(0, actualizar_grafica)

        app.after(0, lambda:
            progress.set((progress.get() + 0.1) % 1)
        )

        if start_time:
            app.after(0, lambda:
                contador.set(f"Tiempo activo: {int(time.time() - start_time)}s")
            )

        await asyncio.sleep(5)


def start_monitor():
    global start_time, monitor_activo

    if not sites:
        textbox.insert("end", "⚠ Agrega al menos una URL\n")
        return

    if not monitor_activo:
        monitor_activo = True

        if start_time is None:
            start_time = time.time()

        threading.Thread(
            target=lambda: asyncio.run(loop_monitor()),
            daemon=True
        ).start()


def detener_monitor():
    global monitor_activo
    monitor_activo = False
    textbox.insert("end", "⏹ Monitoreo detenido\n")


def exportar():
    exportar_pdf(logs)
    textbox.insert("end", "Reporte PDF generado ✔\n")



title = ctk.CTkLabel(app, text="⚡ WEB CONTROL CENTER", font=("Arial", 26))
title.pack(pady=10)

frame_input = ctk.CTkFrame(app)
frame_input.pack(pady=10)

entry = ctk.CTkEntry(frame_input, width=400, placeholder_text="https://...")
entry.pack(side="left", padx=10)

btn_add = ctk.CTkButton(frame_input, text="Agregar URL", command=agregar_sitio)
btn_add.pack(side="left")


textbox = ctk.CTkTextbox(app, width=900, height=260)
textbox.pack(pady=15)


progress = ctk.CTkProgressBar(app, width=600)
progress.pack(pady=10)
progress.set(0)


contador = ctk.StringVar()
contador.set("Tiempo activo: 0s")

label_time = ctk.CTkLabel(app, textvariable=contador)
label_time.pack()


frame_buttons = ctk.CTkFrame(app)
frame_buttons.pack(pady=10)

btn_start = ctk.CTkButton(frame_buttons, text="▶ Iniciar", command=start_monitor)
btn_start.pack(side="left", padx=10)

btn_stop = ctk.CTkButton(frame_buttons, text="⏹ Detener", command=detener_monitor)
btn_stop.pack(side="left", padx=10)

btn_pdf = ctk.CTkButton(frame_buttons, text="📄 Exportar PDF", command=exportar)
btn_pdf.pack(side="left", padx=10)


frame_chart = ctk.CTkFrame(app)
frame_chart.pack(fill="both", expand=True, padx=20, pady=10)

init_chart(frame_chart)

app.mainloop()
