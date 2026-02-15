import numpy as np


def compute_metrics(df):

    polmap = {"positive": 1, "neutral": 0, "negative": -1}
    df["sent_pol"] = df["sent_label"].map(polmap).fillna(0)

    emo_cols = [c for c in df.columns if c.startswith("emo_")]
    tox_cols = [c for c in df.columns if c.startswith("tox_")]

    df["emo_peak"] = df[emo_cols].max(axis=1)
    df["tox_mean"] = df[tox_cols].mean(axis=1)

    df["psych_index"] = (
        0.4 * np.abs(df["sent_pol"]) +
        0.3 * df["emo_peak"] +
        0.3 * df["tox_mean"]
    )

    return df
