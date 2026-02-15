import json
import pandas as pd
from dateutil import parser as dateparser
from preprocessing import normalize_text, extract_message_text


def parse_dt(s):
    try:
        return dateparser.parse(s)
    except:
        return None


def load_json_dialog(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    rows = []

    for m in data["messages"]:
        if m.get("type") != "message":
            continue

        dt = parse_dt(m.get("date"))
        if not dt:
            continue

        text = normalize_text(extract_message_text(m.get("text")))
        if not text:
            continue

        rows.append({
            "dt": dt,
            "sender": m.get("from", "UNKNOWN"),
            "text": text
        })

    return pd.DataFrame(rows)
