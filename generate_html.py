import re

with open('HO_SO_NCKH_HOAN_CHINH.md', 'r', encoding='utf-8') as f:
    text = f.read()

html = []
html.append('''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Hồ sơ NCKH 2026-2027 - Gia sư AI Khoa học Tự nhiên & Tin học</title>
<style>
  @page { size: A4; margin: 20mm 15mm 20mm 15mm; }
  body { font-family: 'Times New Roman', Times, serif; font-size: 13pt; line-height: 1.45; color: #000; margin: 0 auto; max-width: 860px; padding: 24px; background: #fff; }
  h1 { font-size: 15.5pt; font-weight: bold; text-align: center; text-transform: uppercase; margin-top: 24px; margin-bottom: 8px; line-height: 1.3; }
  h2 { font-size: 13.5pt; font-weight: bold; margin-top: 18px; margin-bottom: 6px; border-bottom: 1px solid #444; padding-bottom: 3px; }
  h3 { font-size: 13pt; font-weight: bold; margin-top: 12px; margin-bottom: 4px; }
  p, li { text-align: justify; margin: 4px 0; }
  ul { margin: 4px 0 8px 24px; padding: 0; }
  table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 11pt; page-break-inside: auto; }
  tr { page-break-inside: avoid; page-break-after: auto; }
  th, td { border: 1px solid #333; padding: 6px 8px; text-align: left; vertical-align: top; }
  th { background-color: #f2f2f2; font-weight: bold; text-align: center; }
  blockquote { font-style: italic; background: #f9f9f9; border-left: 4px solid #0056b3; padding: 8px 12px; margin: 10px 0; }
  .page-break { page-break-after: always; break-after: page; }
  @media print {
    body { padding: 0; }
    .no-print { display: none !important; }
  }
  .print-btn { position: fixed; top: 16px; right: 16px; padding: 10px 18px; background: #0056b3; color: #fff; font-family: sans-serif; font-size: 14px; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.3); z-index: 1000; }
</style>
</head>
<body>
<button class="print-btn no-print" onclick="window.print()">🖨️ In toàn bộ hồ sơ (Ctrl + P)</button>
''')

in_table = False
table_data = []

lines = text.split('\n')
for line in lines:
    line_s = line.strip()
    if not line_s:
        if in_table:
            html.append('<table>')
            for r_idx, row in enumerate(table_data):
                html.append('<tr>')
                tag = 'th' if r_idx == 0 else 'td'
                for cell in row:
                    c_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', cell.strip())
                    c_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', c_text)
                    c_text = c_text.replace('<br>', '<br/>')
                    html.append(f'<{tag}>{c_text}</{tag}>')
                html.append('</tr>')
            html.append('</table>')
            in_table = False
            table_data = []
        continue

    if line_s.startswith('---'):
        if in_table:
            html.append('<table>')
            for r_idx, row in enumerate(table_data):
                html.append('<tr>')
                tag = 'th' if r_idx == 0 else 'td'
                for cell in row:
                    c_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', cell.strip())
                    c_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', c_text)
                    html.append(f'<{tag}>{c_text}</{tag}>')
                html.append('</tr>')
            html.append('</table>')
            in_table = False
            table_data = []
        html.append('<div class="page-break"></div>')
        continue

    if line_s.startswith('|'):
        in_table = True
        parts = [p.strip() for p in line_s.strip('|').split('|')]
        if len(parts) > 0 and not all(set(p).issubset({'-', ':', ' '}) for p in parts):
            table_data.append(parts)
        continue

    if in_table:
        html.append('<table>')
        for r_idx, row in enumerate(table_data):
            html.append('<tr>')
            tag = 'th' if r_idx == 0 else 'td'
            for cell in row:
                c_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', cell.strip())
                c_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', c_text)
                html.append(f'<{tag}>{c_text}</{tag}>')
            html.append('</tr>')
        html.append('</table>')
        in_table = False
        table_data = []

    if line_s.startswith('# '):
        html.append(f'<h1>{line_s[2:]}</h1>')
    elif line_s.startswith('## '):
        html.append(f'<h2>{line_s[3:]}</h2>')
    elif line_s.startswith('### '):
        html.append(f'<h3>{line_s[4:]}</h3>')
    elif line_s.startswith('> '):
        c_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line_s[2:])
        html.append(f'<blockquote>{c_text}</blockquote>')
    elif line_s.startswith('- '):
        c_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line_s[2:])
        c_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', c_text)
        html.append(f'<li>{c_text}</li>')
    else:
        c_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line_s)
        c_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', c_text)
        html.append(f'<p>{c_text}</p>')

if in_table:
    html.append('<table>')
    for r_idx, row in enumerate(table_data):
        html.append('<tr>')
        tag = 'th' if r_idx == 0 else 'td'
        for cell in row:
            c_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', cell.strip())
            c_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', c_text)
            html.append(f'<{tag}>{c_text}</{tag}>')
        html.append('</tr>')
    html.append('</table>')

html.append('</body></html>')

with open('HO_SO_NCKH_IN_AN.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(html))

print('SUCCESS')
