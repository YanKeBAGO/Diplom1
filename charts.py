import os
import matplotlib.pyplot as plt


def create_charts(df, outdir):

    paths = {}
    plt.style.use("seaborn-v0_8-whitegrid")

    tox = df.groupby("sender")["tox_mean"].mean()
    plt.figure(figsize=(8, 5), dpi=150)
    plt.bar(tox.index, tox.values)
    plt.title("Средний уровень токсичности")
    plt.xticks(rotation=45)
    plt.tight_layout()
    path1 = os.path.join(outdir, "toxicity.png")
    plt.savefig(path1)
    plt.close()
    paths["toxicity"] = path1

    psych = df.groupby("sender")["psych_index"].mean()
    plt.figure(figsize=(8, 5), dpi=150)
    plt.bar(psych.index, psych.values)
    plt.title("Интегральный психолингвистический индекс")
    plt.xticks(rotation=45)
    plt.tight_layout()
    path2 = os.path.join(outdir, "psych.png")
    plt.savefig(path2)
    plt.close()
    paths["psych"] = path2

    return paths
