import os
from config import SEQUENCE_1, SEQUENCE_2
from config import OUTPUT_DIR_MANCHESTER_DIFERENCIAL as output_dir
from utils.plot_encoding import plot_signal
from .manchester_differential_encode import manchester_differential


def plot_manchester_differential():
    os.makedirs(output_dir, exist_ok=True)

    # Processar as sequências
    signal_1 = manchester_differential(SEQUENCE_1)
    signal_2 = manchester_differential(SEQUENCE_2)

    print("MANCHESTER DIFERENCIAL")
    print(f"Sequência 1: {''.join(str(bit) for bit in signal_1)}\nSequência 2: {''.join(str(bit) for bit in signal_2)}\n")

    # Gráfico do sinal NZRI codificado
    plot_signal(SEQUENCE_1, signal_1, "Manchester Differential Encoded Sequence", os.path.join(output_dir, "manchester_differential_encoded_signal1"))

    # Gráfico do sinal 2 NZRI codificado
    plot_signal(SEQUENCE_2, signal_2, "Manchester Differential Encoded Sequence", os.path.join(output_dir, "manchester_differential_encoded_signal2"))
