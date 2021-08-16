#!/usr/bin/env python3


from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet




def generate_report(attachment, title, paragraph ):
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles['h2'])
    report_body = Paragraph(paragraph, styles['p1'])
    report.build(report_title, report_body)
