import matplotlib.pyplot as plt

def plot_signal(bits, signal, title, file_path):
    time = list(range(len(signal)))
    plt.figure()
    plt.step(time, signal, where='post')
    plt.title(title)
    plt.ylim(-2, 2)
    plt.grid(True)
    plt.yticks([-1, 0, 1])
    plt.xticks(range(len(bits)), bits, rotation='vertical')
    plt.tight_layout()
    plt.savefig(file_path)
    plt.close()