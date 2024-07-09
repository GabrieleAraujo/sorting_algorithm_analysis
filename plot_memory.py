import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("result_final.csv")


plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = (14, 8)

# Plotar gráficos individuais para cada algoritmo
algorithms = data['algoritmo'].unique()

for algorithm in algorithms:
    df_algo = data[data['algoritmo'] == algorithm]
    plt.figure()
    for case in ['best', 'average', 'worst']:
        df_case = df_algo[df_algo['caso'] == case]
        plt.plot(df_case['n'], df_case['memoria'], marker='o', label=f'{case} case')
    plt.title(f'memory do {algorithm}')
    plt.xlabel('Tamanho do Input (n)')
    plt.ylabel('Memória de Execução (MB)')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylim(1e-6, 1e1)  # Ajustando a escala do eixo y
    plt.yticks([1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10])
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{algorithm}_memory.png', bbox_inches='tight')
    plt.show()

# # Plotar gráfico final comparando todos os algoritmos e casos
# plt.figure()
# cases = ['best', 'average', 'worst']
# for algorithm in algorithms:
#     for case in cases:
#         df_case = data[(data['algoritmo'] == algorithm) & (data['caso'] == case)]
#         plt.plot(df_case['n'], df_case['memoria'], marker='o', label=f'{algorithm} - {case}')

# plt.title('Comparação de Algoritmos de Ordenação')
# plt.xlabel('Tamanho do Input (n)')
# plt.ylabel('memoria de Execução (MB)')
# plt.xscale('log')
# plt.yscale('log')
# plt.ylim(1e-4, 1e4)  # Ajustando a escala do eixo y
# plt.yticks([1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100, 1000, 10000])
# plt.legend()
# plt.grid(True)
# plt.savefig('comparison_memory.png', bbox_inches='tight')

# plt.show()

# # Plotar gráfico final comparando todos os algoritmos apenas para o caso "best"
# plt.figure()
# for algorithm in algorithms:
#     df_case = data[(data['algoritmo'] == algorithm) & (data['caso'] == 'best')]
#     plt.plot(df_case['n'], df_case['memoria'], marker='o', label=f'{algorithm} - best')

# plt.title('Comparação de Algoritmos de Ordenação - Melhor Caso')
# plt.xlabel('Tamanho do Input (n)')
# plt.ylabel('memoria de Execução (MB)')
# plt.xscale('log')
# plt.yscale('log')
# plt.ylim(1e-6, 1e4)  # Ajustando a escala do eixo y
# plt.yticks([1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100, 1000, 10000])
# plt.legend()
# plt.grid(True)
# plt.savefig('comparison_memory_best.png', bbox_inches='tight')

# plt.show()

# # Plotar gráfico final comparando todos os algoritmos apenas para o caso "average"
# plt.figure()
# for algorithm in algorithms:
#     df_case = data[(data['algoritmo'] == algorithm) & (data['caso'] == 'average')]
#     plt.plot(df_case['n'], df_case['memoria'], marker='o', label=f'{algorithm} - average')

# plt.title('Comparação de Algoritmos de Ordenação - Médio Caso')
# plt.xlabel('Tamanho do Input (n)')
# plt.ylabel('memoria de Execução (MB)')
# plt.xscale('log')
# plt.yscale('log')
# plt.ylim(1e-6, 1e4)  # Ajustando a escala do eixo y
# plt.yticks([1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100, 1000, 10000])
# plt.legend()
# plt.grid(True)
# plt.savefig('comparison_memory_average.png', bbox_inches='tight')

# plt.show()

# # Plotar gráfico final comparando todos os algoritmos apenas para o caso "worst"
# plt.figure()
# for algorithm in algorithms:
#     df_case = data[(data['algoritmo'] == algorithm) & (data['caso'] == 'worst')]
#     plt.plot(df_case['n'], df_case['memoria'], marker='o', label=f'{algorithm} - worst')

# plt.title('Comparação de Algoritmos de Ordenação - Pior Caso')
# plt.xlabel('Tamanho do Input (n)')
# plt.ylabel('memoria de Execução (MB)')
# plt.xscale('log')
# plt.yscale('log')
# plt.ylim(1e-6, 1e4)  # Ajustando a escala do eixo y
# plt.yticks([1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100, 1000, 10000])
# plt.legend()
# plt.grid(True)
# plt.savefig('comparison_memory_worst.png', bbox_inches='tight')

# plt.show()