import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf(output_path):
    # Standard margins: 0.5 in (36 pt)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    primary_color = colors.HexColor("#7e22ce") # deep purple
    dark_color = colors.HexColor("#0f172a") # slate 900
    muted_color = colors.HexColor("#475569") # slate 600
    border_color = colors.HexColor("#cbd5e1") # slate 300

    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=21,
        textColor=dark_color
    )

    role_style = ParagraphStyle(
        'RoleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=primary_color
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=muted_color
    )

    section_header = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=dark_color,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#1e293b")
    )

    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=11.5,
        textColor=dark_color
    )

    job_meta_style = ParagraphStyle(
        'JobMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=10.5,
        alignment=2, # Right aligned
        textColor=muted_color
    )

    tech_style = ParagraphStyle(
        'TechStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=primary_color
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.3,
        leading=11,
        leftIndent=12,
        firstLineIndent=-8,
        textColor=colors.HexColor("#1e293b")
    )

    story = []

    # Header section
    story.append(Paragraph("M. Arif Iqbal Hidayatullah", name_style))
    story.append(Paragraph("Software Quality Assurance &amp; Test Automation Engineer", role_style))
    story.append(Spacer(1, 3))
    
    contact_line = "+62 851-5885-1926 &nbsp;|&nbsp; iqbalsfsz@gmail.com &nbsp;|&nbsp; linkedin.com/in/iqbaalmuhmd &nbsp;|&nbsp; github.com/iqbalsz &nbsp;|&nbsp; Jakarta, Indonesia"
    story.append(Paragraph(contact_line, contact_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceBefore=0, spaceAfter=8))

    # Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_header))
    summary_text = (
        "Software Quality Assurance and Test Automation Engineer with a Computer Science background "
        "and proven track record safeguarding mission-critical fintech and enterprise platforms (Flip, PT Astra International Tbk). "
        "Specialized in shifting quality left, architecting scalable web and mobile E2E automation suites (TypeScript, Playwright, Appium), "
        "validating complex backend REST API schemas via Postman, and verifying large-scale enterprise data landing pipelines across SQL, SAP, and Cloudera."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 7))

    # Technical Skills
    story.append(Paragraph("TECHNICAL EXPERTISE", section_header))
    skills_data = [
        [
            Paragraph("<b>Test Automation:</b>", body_style),
            Paragraph("Playwright, TypeScript, Appium (Android &amp; iOS), WebdriverIO, Jest, Cypress, Katalon Studio", body_style)
        ],
        [
            Paragraph("<b>API &amp; Backend:</b>", body_style),
            Paragraph("Postman API Testing, Payload &amp; Contract Validation, SQL, SAP, Cloudera Data Landing", body_style)
        ],
        [
            Paragraph("<b>QA Methodologies:</b>", body_style),
            Paragraph("E2E Testing, CI/CD Pipeline Optimization, Flaky Test Reduction, Test Plans, JIRA, UAT", body_style)
        ],
        [
            Paragraph("<b>Languages &amp; Tools:</b>", body_style),
            Paragraph("TypeScript, JavaScript, Python fundamentals, HTML5, CSS3/SCSS, React basics, Git / GitLab, n8n", body_style)
        ]
    ]
    t = Table(skills_data, colWidths=[110, 430])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))

    # Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_header))

    # Job 1: Flip
    job1_header = [
        [
            Paragraph("<b>Test Engineer</b> &mdash; Flip", job_title_style),
            Paragraph("March 2026 &ndash; Present | South Jakarta", job_meta_style)
        ]
    ]
    t1 = Table(job1_header, colWidths=[360, 180])
    t1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t1)
    story.append(Paragraph("Tech Stack: TypeScript, WebdriverIO, Appium, Playwright, Postman, n8n, Slack, Git", tech_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("&bull; Took over as <b>PIC test engineer</b> for gold investment, insurance and Super Flip after a team restructuring, owning all testing and the biweekly regression as the team’s only test engineer.", bullet_style))
    story.append(Paragraph("&bull; Raised the regression pass rate from 60% to <b>90%</b> and automation coverage from 60% to <b>80%</b> by stabilising flaky tests (selector fixes, async handling, retry logic) and automating more test cases.", bullet_style))
    story.append(Paragraph("&bull; Migrated the full Appium mobile test suite to <b>Syntinel</b>, the company’s internal test platform, making biweekly regression manageable for a single engineer.", bullet_style))
    story.append(Paragraph("&bull; Built and maintained mobile automation for critical transaction journeys using <b>WebdriverIO, Appium and TypeScript</b>.", bullet_style))
    story.append(Paragraph("&bull; Tested REST APIs with <b>Postman and Playwright</b>, validating payloads, status codes and responses across payment, gold investment and insurance services.", bullet_style))
    story.append(Paragraph("&bull; Built an <b>n8n workflow and Slack bot</b> that creates fully verified staging test accounts, replacing a 15-step manual process that took about 30 minutes.", bullet_style))
    story.append(Spacer(1, 6))

    # Job 2: Astra
    job2_header = [
        [
            Paragraph("<b>Software Quality Assurance</b> &mdash; PT Astra International Tbk", job_title_style),
            Paragraph("Dec 2023 &ndash; Dec 2024 | North Jakarta", job_meta_style)
        ]
    ]
    t2 = Table(job2_header, colWidths=[360, 180])
    t2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t2)
    story.append(Paragraph("Tech Stack: SQL, SAP, Cloudera Databases, Jest, JIRA, Test Plans, UAT", tech_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("&bull; Formulated end-to-end Test Cases and Test Plans, maintaining structured test documentation and defect tracking directly in JIRA.", bullet_style))
    story.append(Paragraph("&bull; Validated data landing pipelines across <b>SQL, SAP, and Cloudera</b> environments, writing <b>Jest</b> scripts to automate data reconciliation by comparing source and target datasets exported as CSV.", bullet_style))
    story.append(Paragraph("&bull; Led cross-functional User Acceptance Testing (UAT) sessions with business stakeholders and authored comprehensive user operation manuals.", bullet_style))
    story.append(Spacer(1, 6))

    # Job 3: Coding.ID & Freelance
    job3_header = [
        [
            Paragraph("<b>QA Automation Trainee &amp; Freelance Developer</b> &mdash; Coding.ID / Elgatama", job_title_style),
            Paragraph("2022 &ndash; 2023 | Indonesia", job_meta_style)
        ]
    ]
    t3 = Table(job3_header, colWidths=[360, 180])
    t3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t3)
    story.append(Spacer(1, 2))
    story.append(Paragraph("&bull; <b>Coding.ID:</b> Completed comprehensive QA automation bootcamp specializing in automated testing for Web, API, and Mobile using Katalon Studio and Cypress.", bullet_style))
    story.append(Paragraph("&bull; <b>Elgatama:</b> Designed and deployed responsive client corporate web platform using clean semantic HTML5, CSS3, and JavaScript.", bullet_style))
    story.append(Spacer(1, 8))

    # Education
    story.append(Paragraph("EDUCATION", section_header))
    edu_table = [
        [
            Paragraph("<b>Universitas Sriwijaya</b> &mdash; S1, Computer Science (Teknik Informatika)", body_style),
            Paragraph("2015 - 2020", job_meta_style)
        ]
    ]
    t_edu = Table(edu_table, colWidths=[420, 120])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)
    story.append(Spacer(1, 7))

    # Certifications
    story.append(Paragraph("CERTIFICATIONS &amp; TRAININGS", section_header))
    cert_text = (
        "&bull; <b>Quality Assurance Professional Certification</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        "&bull; <b>HTML, CSS, and Javascript for Web Developers</b><br/>"
        "&bull; <b>Foundations of User Experience (UX) Design</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        "&bull; <b>Coding.ID QA Automation Trainee Certification</b>"
    )
    story.append(Paragraph(cert_text, body_style))

    doc.build(story)
    print("PDF generated successfully:", output_path)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(current_dir, "CV M.Arif Iqbal_QA.pdf")
    generate_pdf(target)
