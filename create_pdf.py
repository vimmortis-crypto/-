from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

# Создаем PDF документ
doc = SimpleDocTemplate("5_способов_отдохнуть.pdf", pagesize=A4)
styles = getSampleStyleSheet()

# Регистрируем шрифт с поддержкой кириллицы (используем встроенный шрифт)
# ReportLab имеет ограниченные встроенные шрифты, поэтому используем стандартный
# Для лучшей поддержки кириллицы можно зарегистрировать внешний шрифт

# Создаем стили
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#2c3e50'),
    spaceAfter=30,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#34495e'),
    spaceBefore=12,
    spaceAfter=6,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=12,
    textColor=colors.HexColor('#555555'),
    spaceBefore=6,
    spaceAfter=12,
    leading=18,
    fontName='Helvetica'
)

# Контент документа
story = []

# Заголовок
title = Paragraph("5 способов отдохнуть", title_style)
story.append(title)
story.append(Spacer(1, 20))

# Вступление
intro_text = """
В современном ритме жизни важно находить время для отдыха и восстановления сил. 
Предлагаем вам 5 эффективных способов отдохнуть и перезагрузиться:
"""
story.append(Paragraph(intro_text, body_style))
story.append(Spacer(1, 20))

# Способ 1
story.append(Paragraph("1. Прогулка на природе", heading_style))
way1_text = """
Проведите время на свежем воздухе в парке, лесу или у водоема. 
Природа помогает снять стресс, улучшить настроение и очистить мысли. 
Даже 30-минутная прогулка может значительно улучшить ваше самочувствие.
"""
story.append(Paragraph(way1_text, body_style))

# Способ 2
story.append(Paragraph("2. Медитация и дыхательные практики", heading_style))
way2_text = """
Уделите 10-15 минут медитации или глубоким дыхательным упражнениям. 
Это поможет успокоить ум, снизить уровень тревожности и восстановить внутреннее равновесие. 
Найдите тихое место, закройте глаза и сосредоточьтесь на дыхании.
"""
story.append(Paragraph(way2_text, body_style))

# Способ 3
story.append(Paragraph("3. Чтение книги", heading_style))
way3_text = """
Погрузитесь в интересный мир литературы. Чтение отвлекает от повседневных забот, 
развивает воображение и позволяет мысленно перенестись в другое место. 
Выберите жанр, который вам нравится, и наслаждайтесь процессом.
"""
story.append(Paragraph(way3_text, body_style))

# Способ 4
story.append(Paragraph("4. Теплая ванна или душ", heading_style))
way4_text = """
Теплая вода помогает расслабить мышцы, снять физическое напряжение и успокоиться. 
Добавьте ароматические масла, соль для ванн или включите приятную музыку 
для создания атмосферы полного релакса.
"""
story.append(Paragraph(way4_text, body_style))

# Способ 5
story.append(Paragraph("5. Общение с близкими", heading_style))
way5_text = """
Проведите время с семьей или друзьями в теплой обстановке. 
Искренние разговоры, совместные занятия и поддержка близких 
помогают почувствовать себя нужным и наполняют положительными эмоциями.
"""
story.append(Paragraph(way5_text, body_style))

# Заключение
story.append(Spacer(1, 20))
conclusion_text = """
Помните: регулярный отдых — залог продуктивности и хорошего настроения. 
Найдите то, что подходит именно вам, и сделайте заботу о себе привычкой!
"""
story.append(Paragraph(conclusion_text, body_style))

# Генерируем PDF
doc.build(story)
print("PDF успешно создан: 5_способов_отдохнуть.pdf")
