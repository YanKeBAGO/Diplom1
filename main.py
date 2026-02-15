import argparse
from config import SEED
from utils import set_seed, safe_mkdir
from data_loader import load_json_dialog
from models import build_pipelines, run_with_chunking
from metrics import compute_metrics
from roles import compute_roles
from charts import create_charts
from llm import generate_llm_analysis
from report import build_pdf


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("json_path")
    parser.add_argument("--outdir", default="out")
    parser.add_argument("--device", default="cpu")
    args = parser.parse_args()

    set_seed(SEED)
    safe_mkdir(args.outdir)

    df = load_json_dialog(args.json_path)

    sentiment, emotions, toxicity = build_pipelines(args.device)

    sent_out = run_with_chunking(sentiment, df["text"].tolist())
    df["sent_label"] = [o["label"] for o in sent_out]

    emo_out = run_with_chunking(emotions, df["text"].tolist())
    for i, item in enumerate(emo_out):
        for p in item:
            df.loc[i, f"emo_{p['label']}"] = p["score"]

    tox_out = run_with_chunking(toxicity, df["text"].tolist())
    for i, item in enumerate(tox_out):
        for p in item:
            df.loc[i, f"tox_{p['label']}"] = p["score"]

    df = compute_metrics(df)
    roles = compute_roles(df)
    charts = create_charts(df, args.outdir)

    summary = {
        "total_messages": len(df),
        "participants": df["sender"].nunique(),
        "roles": roles
    }

    llm_text = generate_llm_analysis(summary)

    build_pdf(args.outdir + "/report.pdf", summary, charts, llm_text)

    print("Готово.")


if __name__ == "__main__":
    main()
