"""
 Extract surf from hallon invoice
"""
import re
from collections import defaultdict

import PyPDF2


def extract_surf_from_invoice(invoice_file: str) -> tuple:
    pdfreader = PyPDF2.PdfReader(invoice_file)
    usage_per_day = defaultdict(int)

    for page in pdfreader.pages:
        page_text = page.extract_text()
        surf_lines = [ln for ln in page_text.splitlines() if re.search(r'^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}Data', ln)]
        for line in surf_lines:
            date, byte_string = re.match(r'([0-9-]+\s).*(\s\d+\sbytes)', line).groups()
            usage_per_day[date] += int(byte_string[:byte_string.rfind(' ')])
    return sum(v for v in usage_per_day.values()), usage_per_day
