# random_walk.py
#
# E 7.10: Caminatas al azar
#
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)
    return pasos.cumsum()

N = 100000
walks = []
for i in range(12):
    walks.append(randomwalk(N))

# considero como maximo la que en total (sumatoria) se alejó más del origen
# y mínimo la que en valor absoluto se alejo menos (menor sumatoria)
max_walk = 0.0
min_walk = np.inf
for i, walk in enumerate(walks):
    suma = np.sum(np.abs(walk))
    if suma > max_walk:
        max_idx  = i
        max_walk = suma
    if suma < min_walk:
        min_idx  = i
        min_walk = suma


""" graficos """
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
          'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan', 'lime',
          'lightseagreen']
max_walk = np.max(np.abs(walks[max_idx]))
# grafico superior: todas las caminatas
fig = plt.figure()
plt.subplot(2, 1, 1)
plt.xticks([])
plt.ylim(-max_walk * 1.2, max_walk * 1.2)
plt.ylabel("distancia al origen")
plt.title("Caminatas al azar")
for i, walk in enumerate(walks):
    plt.plot(walk, color=colors[i])

# grafico inferior izq: caminata que mas se aleja
plt.subplot(2, 2, 3)
plt.ylabel("distancia al origen")
plt.xticks([])
plt.ylim(-max_walk * 1.2, max_walk * 1.2)
plt.plot(walks[max_idx], color=colors[max_idx])
plt.title("La caminata que más se aleja")


# grafico inferior der: caminata que menos se aleja
plt.subplot(2, 2, 4)
plt.yticks([])
plt.xticks([])
plt.ylim(-max_walk * 1.2, max_walk * 1.2)
plt.plot(walks[min_idx], color=colors[min_idx])
plt.title("La caminata que menos se aleja")

plt.savefig("random_walk.png", dpi=500)
plt.show()
