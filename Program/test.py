from PyPDF2 import PdfFileReader

file_path_reader = "D:\\College\\Artificial Intelligence\\Giao_trinh_TRI_TU_NHAN_TO_ARTIFICIAL_I.pdf"
file_object_reader = open(file_path_reader, 'rb')
file_path_writer = "D:\\College\\Artificial Intelligence\\test.txt"
pdf = PdfFileReader(file_object_reader, strict=False)

with open(file_path_writer, 'w', encoding='utf-8') as f:
    for page_num in range(pdf.numPages):
        # print("Page: {0}".format(page_num))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText().encode('utf-8')
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num + 1))
            f.write(''.center(100, '-'))
            f.write(txt.decode('utf-8'))
            txt.decode('utf-8')

    f.close()
