


def register_font():

    # Windows системный Arial (ничего скачивать не нужно)
    font_path = r"C:\Windows\Fonts\arial.ttf"

    if os.path.exists(font_path):
        pdfmetrics.registerFont(TTFont("Arial", font_path))
        return "Arial"

    # fallback
    return "Helvetica"


def build_pdf(output_path, summary, charts, llm_text):

    font_name = register_font()

    doc = SimpleDocTemplate(output_path)
    elements = []

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontName=font_name,
        fontSize=18,
        spaceAfter=14
    )

    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["Normal"],
        fontName=font_name,
        fontSize=12,
        leading=16
    )

    section_style = ParagraphStyle(
        "SectionStyle",
        parent=styles["Heading2"],
        fontName=font_name,
        fontSize=14,
        textColor=colors.darkblue,
        spaceBefore=12,
        spaceAfter=6
    )

    # --- Заголовок ---
    elements.append(Paragraph("Психолингвистический анализ диалога", title_style))
    elements.append(Spacer(1, 12))
    elements.append(HRFlowable(width="100%"))
    elements.append(Spacer(1, 12))

    # --- Общая статистика ---
    elements.append(Paragraph("Общая статистика", section_style))
    elements.append(Paragraph(f"Количество сообщений: {summary['total_messages']}", normal_style))
    elements.append(Paragraph(f"Количество участников: {summary['participants']}", normal_style))
    elements.append(Spacer(1, 12))

    # --- Роли ---
    elements.append(Paragraph("Психологические роли участников", section_style))
    for role, person in summary["roles"].items():
        elements.append(Paragraph(f"{role}: {person}", normal_style))
    elements.append(Spacer(1, 18))

    # --- Диаграммы ---
    elements.append(PageBreak())
    elements.append(Paragraph("Визуализация показателей", section_style))
    elements.append(Spacer(1, 12))

    if "toxicity" in charts:
        elements.append(Image(charts["toxicity"], width=6 * inch, height=4 * inch))
        elements.append(Spacer(1, 16))

    if "psych" in charts:
        elements.append(Image(charts["psych"], width=6 * inch, height=4 * inch))
        elements.append(Spacer(1, 16))

    # --- Итоговый вывод LLM ---
    elements.append(PageBreak())
    elements.append(Paragraph("Итоговый аналитический вывод", section_style))
    elements.append(Spacer(1, 12))

    # Разбиваем длинный текст на абзацы
    for paragraph in llm_text.split("\n"):
        paragraph = paragraph.strip()
        if paragraph:
            elements.append(Paragraph(paragraph, normal_style))
            elements.append(Spacer(1, 10))

    # --- Сборка PDF ---
    doc.build(elements)
import os
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable
from reportlab.platypus import PageBreak
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet


def register_font():

    # Windows системный Arial
    font_path = r"C:\Windows\Fonts\arial.ttf"

    if os.path.exists(font_path):
        pdfmetrics.registerFont(TTFont("Arial", font_path))
        return "Arial"

    # fallback
    return "Helvetica"


def build_pdf(output_path, summary, charts, llm_text):

    font_name = register_font()

    doc = SimpleDocTemplate(output_path)
    elements = []

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontName=font_name,
        fontSize=18,
        spaceAfter=14
    )

    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["Normal"],
        fontName=font_name,
        fontSize=12,
        leading=16
    )

    section_style = ParagraphStyle(
        "SectionStyle",
        parent=styles["Heading2"],
        fontName=font_name,
        fontSize=14,
        textColor=colors.darkblue,
        spaceBefore=12,
        spaceAfter=6
    )

    # Заголовок
    elements.append(Paragraph("Психолингвистический анализ диалога", title_style))
    elements.append(Spacer(1, 12))
    elements.append(HRFlowable(width="100%"))
    elements.append(Spacer(1, 12))

    # Общая статистика
    elements.append(Paragraph("Общая статистика", section_style))
    elements.append(Paragraph(f"Количество сообщений: {summary['total_messages']}", normal_style))
    elements.append(Paragraph(f"Количество участников: {summary['participants']}", normal_style))
    elements.append(Spacer(1, 12))

    # Роли
    elements.append(Paragraph("Психологические роли участников", section_style))
    for role, person in summary["roles"].items():
        elements.append(Paragraph(f"{role}: {person}", normal_style))
    elements.append(Spacer(1, 18))

    # Диаграммы
    elements.append(PageBreak())
    elements.append(Paragraph("Визуализация показателей", section_style))
    elements.append(Spacer(1, 12))

    if "toxicity" in charts:
        elements.append(Image(charts["toxicity"], width=6 * inch, height=4 * inch))
        elements.append(Spacer(1, 16))

    if "psych" in charts:
        elements.append(Image(charts["psych"], width=6 * inch, height=4 * inch))
        elements.append(Spacer(1, 16))

    # Итоговый вывод LLM
    elements.append(PageBreak())
    elements.append(Paragraph("Итоговый аналитический вывод", section_style))
    elements.append(Spacer(1, 12))

    # Разбиваем длинный текст на абзацы
    for paragraph in llm_text.split("\n"):
        paragraph = paragraph.strip()
        if paragraph:
            elements.append(Paragraph(paragraph, normal_style))
            elements.append(Spacer(1, 10))

    # PDF
    doc.build(elements)
