import matplotlib.pyplot as plt

def plot_signal(bits, signal, title, file_path, negative_ylim=0.25, yticks=[0, 1], manchester=False):
    # Converte a string de bits em uma lista de caracteres
    bits = list(bits)
    
    # Adicionar Fonte
    bits = [None] + bits + [None] 
    signal = [0] + signal + [signal[-1]]  

    if manchester:
        # Criar o eixo do tempo e duplicar o sinal corretamente
        time = []
        signal_expanded = []
        
        for i in range(len(bits) - 2):  # Ajusta o loop para os bits extras
            # Cada bit deve ocupar dois espaços no eixo X
            time.append(i * 2)        # Primeiro espaço
            time.append(i * 2 + 1)    # Segundo espaço
            
            # Expande o sinal para duas amostras por bit
            signal_expanded.append(signal[2 * i])
            signal_expanded.append(signal[2 * i + 1])
        
        # Ajustando os rótulos do eixo X para que cada bit ocupe dois espaços
        ticks = []
        labels = []
        for i in range(len(bits)):
            ticks.append(i * 2)  # Coloca o rótulo no meio de cada par de espaços
            labels.append(bits[i] if bits[i] is not None else '') 
        
    else:
        # Código padrão para outros tipos de codificação
        time = list(range(len(signal)))
        signal_expanded = signal
        ticks = range(len(bits))
        labels = [bit if bit is not None else '' for bit in bits] 

    # Plot do sinal
    plt.figure()
    plt.step(time, signal_expanded, where='post')
    plt.title(title)
    plt.ylim(-negative_ylim, 1.25)
    plt.grid(True)
    plt.yticks(yticks)
    
    # Ajustando os rótulos dos bits no eixo X
    plt.xticks(ticks, labels)
    
    plt.tight_layout()
    plt.savefig(file_path)
    plt.close()
