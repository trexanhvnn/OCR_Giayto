# import aspose.pdf as ap

# input_pdf = "test_convert_pdf.pdf"
# output_pdf = "test_convert_pdf.xlsx"

# # Mở tệp PDF
# document = ap.Document(input_pdf)

# # Tạo và đặt tùy chọn lưu
# save_option = ap.ExcelSaveOptions()

# # Lưu tệp thành định dạng MS Excel
# document.save(output_pdf, save_option)
import PyPDF2
import pandas as pd
from PyPDF2 import PdfReader

pdf_file = open('test_convert_pdf.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
df = pd.DataFrame()
for page_number in range(number_of_pages):
    page = read_pdf.getPage(page_number)
    page_content = page.extractText()
    df = df.append(pd.read_csv(StringIO(page_content), sep='\t'))
df.to_excel('file.xlsx', index=False)4
