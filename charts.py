from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from monitor import historial
import statistics

plt.rcParams.update({
    "figure.facecolor": "#0d1117",
    "axes.facecolor": "#0d1117",
    "axes.labelcolor": "white",
    "text.color": "white",
    "xtick.color": "white",
    "ytick.color": "white"
})

fig, ax = plt.subplots(figsize=(6,4))
canvas = None

colores = ["#00FFFF", "#FF00FF", "#00FF9C", "#FFD700", "#FF4C4C"]


def init_chart(frame):
    global canvas
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)


def actualizar_grafica():

    ax.clear()

    if not historial:
        ax.set_title("Esperando datos...")
        canvas.draw()
        return

    for i, (site, datos) in enumerate(historial.items()):

        if not datos:
            continue

        color = colores[i % len(colores)]
        promedio = round(statistics.mean(datos), 2)

        ax.plot(datos, color=color, linewidth=2.5, marker="o",
                label=f"{site} | Avg {promedio}s")

        ax.plot(datos, color=color, linewidth=6, alpha=0.1)

    ax.set_title("⚡ Monitor Latencia")
    ax.grid(True, linestyle="--", alpha=0.3)
    ax.legend()

    canvas.draw()
