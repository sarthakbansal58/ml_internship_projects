from io import BytesIO
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER


def generate_pdf(
    title,
    genre,
    language,
    tone,
    character,
    setting,
    story
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading = styles["Heading2"]

    normal = styles["BodyText"]

    elements = []

    # App Title

    elements.append(Paragraph("AI Story Generator", title_style))
    elements.append(Spacer(1, 20))

    # Story Title

    elements.append(Paragraph(f"<b>{title}</b>", heading))
    elements.append(Spacer(1, 20))

    # Metadata

    elements.append(Paragraph(f"<b>Genre:</b> {genre}", normal))
    elements.append(Paragraph(f"<b>Language:</b> {language}", normal))
    elements.append(Paragraph(f"<b>Tone:</b> {tone}", normal))
    elements.append(Paragraph(f"<b>Main Character:</b> {character}", normal))
    elements.append(Paragraph(f"<b>Setting:</b> {setting}", normal))

    elements.append(Spacer(1, 20))

    elements.append(Paragraph("<b>Story</b>", heading))

    elements.append(Spacer(1, 10))

    # Preserve paragraphs

    for para in story.split("\n"):
        if para.strip():
            elements.append(Paragraph(para, normal))
            elements.append(Spacer(1, 8))

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf    