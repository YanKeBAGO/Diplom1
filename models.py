import numpy as np
from transformers import pipeline
from config import MODEL_SENTIMENT, MODEL_EMOTION, MODEL_TOXICITY


def build_pipelines(device):
    device_idx = -1 if device == "cpu" else 0

    sentiment = pipeline("text-classification", model=MODEL_SENTIMENT, device=device_idx)
    emotions = pipeline("text-classification", model=MODEL_EMOTION, device=device_idx, top_k=None)
    toxicity = pipeline("text-classification", model=MODEL_TOXICITY, device=device_idx, top_k=None)

    return sentiment, emotions, toxicity


def split_long_text(text, max_words=300):
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]


def run_with_chunking(pipe, texts):
    results = []

    for text in texts:
        chunks = split_long_text(text)
        outputs = pipe(chunks)

        if isinstance(outputs[0], list):
            avg_scores = {}
            for ch in outputs:
                for p in ch:
                    avg_scores.setdefault(p["label"], []).append(p["score"])
            results.append([
                {"label": k, "score": float(np.mean(v))}
                for k, v in avg_scores.items()
            ])
        else:
            labels = [o["label"] for o in outputs]
            scores = [o["score"] for o in outputs]
            majority = max(set(labels), key=labels.count)
            results.append({"label": majority, "score": float(np.mean(scores))})

    return results
