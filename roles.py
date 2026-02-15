def compute_roles(df):
    grouped = df.groupby("sender")

    return {
        "Инициатор диалога": df.sort_values("dt").iloc[0]["sender"],
        "Наиболее активный участник": df["sender"].value_counts().idxmax(),
        "Эмоциональный драйвер": grouped["emo_peak"].mean().idxmax(),
        "Источник токсичности": grouped["tox_mean"].mean().idxmax(),
        "Психологически доминирующий участник": grouped["psych_index"].mean().idxmax(),
    }
