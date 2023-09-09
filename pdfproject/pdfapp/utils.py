import pandas as pd
import pdfplumber

def extract_dataframes_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # Use pdfplumber's table extraction feature
        tables = [page.extract_table() for page in pdf.pages]
        dataframes = [pd.DataFrame(table[1:], columns=table[0]) for table in tables if table]
    return dataframes


def extract_text_from_coordinates(pdf_path, coords):
    extracted_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words()
            for word in words:
                if coords['x0'] <= word['x0'] <= coords['x1'] and coords['y0'] <= word['top'] <= coords['y1']:
                    extracted_text += word['text'] + ' '
    return extracted_text.strip()