import os
from config import SEQUENCE_1, SEQUENCE_2
from utils.plot_encoding import plot_signal
from .nrzi_encode import nrzi
from config import OUTPUT_DIR_NRZI as output_dir


def plot_nrzi():
    os.makedirs(output_dir, exist_ok=True)

    # Processar as sequências
    signal_1 = nrzi(SEQUENCE_1)
    signal_2 = nrzi(SEQUENCE_2)

    print("NRZI")
    print(f"Sequência 1: {''.join(str(bit) for bit in signal_1)}\nSequência 2: {''.join(str(bit) for bit in signal_2)}\n")

    # Gráfico do sinal NZRI codificado
    plot_signal(SEQUENCE_1, signal_1, "NRZI Encoded Sequence", os.path.join(output_dir, "nrzi_encoded_signal1"))

    # Gráfico do sinal 2 NZRI codificado
    plot_signal(SEQUENCE_2, signal_2, "NRZI Encoded Sequence", os.path.join(output_dir, "nrzi_encoded_signal2"))
