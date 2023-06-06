import numpy as np
import matplotlib.pyplot as grafico

a,b,c = np.loadtxt('trajetoria.dat', dtype=(str), unpack=True)

figura, (ax, ax2) = grafico.subplots(nrows=1, ncols=2, figsize=(30, 15), sharey=True)

ax.set_title('Evolução da posição x em função do tempo', fontsize=20)
ax.set_xlabel('t(s)', fontsize=20)
ax.set_ylabel('x(m)', fontsize=20)
ax.xaxis.grid(True)
ax.yaxis.grid(True)
ax.scatter(list(map(float,a)),list(map(float,b)), c='blue')


ax2.set_title('Evolução da posição y em função do tempo', fontsize=20)
ax2.set_xlabel('t(s)', fontsize=20)
ax2.set_ylabel('y(m)', fontsize=20)
ax2.xaxis.grid(True)
ax2.yaxis.grid(True)
ax2.scatter(list(map(float,a)),list(map(float,c)), c='red')
grafico.show()
figura.savefig('posicao_f(t).png')

figura2 = grafico.figure(figsize=(30,15))
ax3=figura2.add_subplot(111)
ax3.set_title('Gráfico Y(x)', fontsize=20)
ax3.set_xlabel('x(m)', fontsize=20)
ax3.set_ylabel('y(m)', fontsize=20)
ax3.xaxis.grid(True)
ax3.yaxis.grid(True)
ax3.scatter(list(map(float,b)),list(map(float,c)), color='crimson')
grafico.show()
figura2.savefig('y(t).png')
