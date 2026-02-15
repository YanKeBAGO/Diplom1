import re


def normalize_text(x):
    return re.sub(r"\s+", " ", x).strip()


def extract_message_text(msg_field):
    if isinstance(msg_field, str):
        return msg_field

    if isinstance(msg_field, list):
        parts = []
        for item in msg_field:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict) and "text" in item:
                parts.append(str(item["text"]))
        return "".join(parts)

    return ""
