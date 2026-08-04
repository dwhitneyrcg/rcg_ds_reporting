import docx
import os

files = {
    'BIZ_AREA_SUMMARIZATION': r'C:\Users\133486\OneDrive - Royal Caribbean Group\Co-Pilot Demo\Weekly Report from Raw Team Reports (Single-Week Demo)\20251031 - Instruction Files (Business Area Summarization).docx',
    'BIZ_AREA_MAPPINGS': r'C:\Users\133486\OneDrive - Royal Caribbean Group\Co-Pilot Demo\Weekly Report from Raw Team Reports (Single-Week Demo)\20251031 - Instructions Files (Generate Business Area Mappings).docx',
}

out_path = r'C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\extracted_support.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    for label, path in files.items():
        out.write(f'\n\n========== {label} ==========\n')
        if os.path.exists(path):
            doc = docx.Document(path)
            for p in doc.paragraphs:
                out.write(p.text + '\n')
            for table in doc.tables:
                out.write('\n--- TABLE ---\n')
                for row in table.rows:
                    out.write(' | '.join(cell.text for cell in row.cells) + '\n')
        else:
            out.write(f'NOT FOUND: {path}\n')

print('Done. Output written to extracted_text.txt')
