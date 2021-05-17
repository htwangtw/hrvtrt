import matplotlib.pyplot as plt
import numpy as np
from hrvtrt.utils import read_tsv


data = read_tsv("results/motion_qc.tsv")

for qc in ["fd_mean", "fd_perc", "despike_perc"]:
    x_gitter = np.random.normal(1, 0.04, size=int(data.shape[0] / 2)).tolist()
    data_to_plot = [data[qc][data["session"] != "TRT"].tolist(),
                    data[qc][data["session"] == "TRT"].tolist()
    ]
    plt.figure(figsize=(10, 6))
    x_1 = np.random.normal(1, 0.04, size=int(data.shape[0] / 2))
    x_2 = x_1 + 1
    plt.plot(x_1, data_to_plot[0], 'r.', alpha=0.2)
    plt.plot(x_2, data_to_plot[1], 'b.', alpha=0.2)
    for x1, x2, y1, y2 in zip(x_1, x_2, data_to_plot[0], data_to_plot[1]):
        plt.plot([x1, x2], [y1, y2], 'k-', alpha=0.1)
    box = plt.boxplot(data_to_plot,
                    positions=[1, 2],
                    labels=['Baseline','One month'],
                    showfliers=False)

    plt.show()

np.corrcoef([data["fd_mean"][data["session"] != "TRT"], data["fd_perc"][data["session"] != "TRT"]])
np.corrcoef([data["fd_mean"][data["session"] == "TRT"], data["fd_perc"][data["session"] == "TRT"]])