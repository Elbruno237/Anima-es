import numpy as np
import matplotlib.pyplot as plt

cont = 4  # Número de valores de n
L = 1e-2  # m
x = np.linspace(0, L, 100)

plt.style.use('dark_background')

linhas = 2
fig, ax = plt.subplots(linhas, cont, figsize=(15, 6))  # 2 linhas, N colunas
fig.suptitle('''Função de Onda e Densidade de Probabilidade para diferentes n \n
             em uma caixa de potencial infinito unidimensional ''', fontsize=16)

for i, n in enumerate(range(1, cont + 1)):
    psi = (2 / L)**0.5 * np.sin((n * np.pi / L) * x)
    psi2 = (2 / L) * np.sin((n * np.pi / L) * x)**2

    # Linha 0: função de onda ψ(x)
    ax[0][i].plot(x, psi, color='cyan')
    ax[0][i].set_title(f'ψ(x), n = {n}')
    ax[0][i].set_xlabel('x (m)')
    ax[0][i].set_ylabel(r'$\psi(x)$')
    ax[0][i].grid(True)

    # Linha 1: densidade de probabilidade ψ²(x)
    ax[1][i].plot(x, psi2, color='orange')
    ax[1][i].set_title(f'ψ²(x), n = {n}')
    ax[1][i].set_xlabel('x (m)')
    ax[1][i].set_ylabel(r'$\psi^2(x)$')
    ax[1][i].grid(True)

plt.tight_layout()
plt.show()
