from PyPDF2 import PdfFileReader

file_path_reader = "D:\\College\\Artificial Intelligence\\New folder\\Text Detection\\listening-reading-sample-tests.pdf"
file_path_writer = "D:\\College\\Artificial Intelligence\\New folder\\Text Detection\\test.txt"
pdf = PdfFileReader(file_path_reader)

with open(file_path_writer, 'w', encoding='utf-8') as f:
    for page_num in range(pdf.numPages):
        # print("Page: {0}".format(page_num))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num + 1))
            f.write(''.center(100, '-'))
            f.write(txt)

    f.close()