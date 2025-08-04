#!/usr/bin/env python


from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.energy import Energy
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation
import warnings
warnings.filterwarnings("ignore", message=".*Matplotlib GUI outside of the main thread.*")

battery_width = 0.1
battery_height = 0.3
battery_head_height = 0.05
battery_head_width = battery_width * 0.375
nivel_maximo = 0.000003  # Wh

# Positions
nodos = [
    (1.1, 0.590),
    (1.828, 0.705),
    (3.41, 0.705),
    (3.93, 0.590),
    (4.73, 0.705),
    (6.43, 0.475),
    (7.76, 0.610),
    (8.36, 0.705),
    (9.8, 0.610),
    (10.44, 0.59),
    (11.02, 0.5),
]

def run_plot(sensores,titulo="Monitoring System"):
    img = mpimg.imread('images/plant.png')
    fig, ax = plt.subplots(figsize=(12, 3), num=titulo)
    ax.imshow(img, extent=[0, 12, 0, 3])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3)
    ax.set_title(titulo)
    ax.axis('off')

    bar_level = []
    sensor_map = {}  # sensor -> (bar, y, text)

    for i, sensor in enumerate(sensores):
        x, y = nodos[i]

        body = patches.Rectangle((x - battery_width / 2, y), battery_width, battery_height,
                                  edgecolor='black', facecolor='none', lw=1.5)
        ax.add_patch(body)

        head = patches.Rectangle((x - battery_head_width / 2, y + battery_height),
                                   battery_head_width, battery_head_height, color='black')
        ax.add_patch(head)

        bar = patches.Rectangle((x - battery_width / 2 + 0.02, y),
                                  battery_width - 0.04, battery_height,
                                  color='green')
        ax.add_patch(bar)
        bar_level.append(bar)

        text = ax.text(x + 0.02, y + battery_height + 0.15, "100%", ha='center', va='bottom', fontsize=12)
        sensor_map[sensor] = (bar, y, text)

    def update(frame):
        for sensor in sensores:
            bar, base_y, text = sensor_map[sensor]
            consumo = getattr(sensor, 'consumption', 0)
            battery_capacity = getattr(sensor, 'battery_capacity', 0.000003)

            carga = max(0.0, min(1.0, 1 - (consumo / battery_capacity)))
            altura = carga * battery_height
            bar.set_height(altura)
            bar.set_y(base_y)

            if carga > 0.6:
                bar.set_color('green')
            elif carga > 0.3:
                bar.set_color('orange')
            else:
                bar.set_color('red')

            percentage = int(carga * 100)
            text.set_text(f"{percentage}%")
            text.set_y(base_y + battery_height + 0.15)

        return list(bar_level) + [text for _, _, text in sensor_map.values()]

    ani = FuncAnimation(fig, update, interval=1000)
    plt.show()