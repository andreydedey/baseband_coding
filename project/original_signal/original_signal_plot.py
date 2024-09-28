import os
from config import SEQUENCE_1, SEQUENCE_2
from utils.plot_encoding import plot_signal
from config import OUTPUT_DIR_ORIGINAL_SIGNAL as output_dir


def convert_sequence_to_int_list(sequence):
    return [int(bit) for bit in sequence]


def plot_original_signal():
    os.makedirs(output_dir, exist_ok=True)

    # Processar as sequências
    signal_1 = convert_sequence_to_int_list(SEQUENCE_1)
    signal_2 = convert_sequence_to_int_list(SEQUENCE_2)

    print("Original Signal")
    print(f"Sequência 1: {SEQUENCE_1}\nSequência 2: {SEQUENCE_2}\n")

    # Gráfico do sinal NZRI codificado
    plot_signal(SEQUENCE_1, signal_1, "Original Sequence", os.path.join(output_dir, "original_signal1"))

    # Gráfico do sinal 2 NZRI codificado
    plot_signal(SEQUENCE_2, signal_2, "Original Sequence", os.path.join(output_dir, "original_signal2"))
