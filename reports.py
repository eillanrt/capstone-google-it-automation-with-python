from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_report(attachment, title, paragraph):
  styles = getSampleStyleSheet()
  paragraph_style = ParagraphStyle(name='Normal', fontSize=16, spaceBefore=6)

  report = SimpleDocTemplate(attachment)
  report_title = Paragraph(title, styles['title'])
  report_content = [report_title, Spacer(16, 16)]

  parsed_paragraph = [Spacer(16, 16) if line == '' else Paragraph(line, paragraph_style) for line in paragraph.split('\n')]

  for flowable in parsed_paragraph:
    report_content.append(flowable)

  report.build(report_content)
