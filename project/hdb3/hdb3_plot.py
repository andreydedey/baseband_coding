import os
from config import SEQUENCE_1, SEQUENCE_2
from config import OUTPUT_DIR_HDB3 as outpur_dir
from utils.plot_encoding import plot_signal
from .hdb3_encode import hdb3


def plot_hdb3():
    os.makedirs(outpur_dir, exist_ok=True)

    # Processar as sequências
    signal_1 = hdb3(SEQUENCE_1)
    signal_2 = hdb3(SEQUENCE_2)

    print("HDB3")
    print(f"Sequência 1: {''.join(str(bit) for bit in signal_1)}\nSequência 2: {''.join(str(bit) for bit in signal_2)}\n")

    # Gráfico do sinal HDB3 codificado
    plot_signal(SEQUENCE_1, signal_1, "HDB3 Encoded Sequence", os.path.join(outpur_dir, "hdb3_encoded_signal1"), negative_ylim=1.5)

    # Gráfico do sinal 2 HDB3 codificado
    plot_signal(SEQUENCE_2, signal_2, "HDB3 Encoded Sequence", os.path.join(outpur_dir, "hdb3_encoded_signal2"), negative_ylim=1.5)
