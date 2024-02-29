import os

def run_pdf_to_text(args):
    folder1 = args.inputFolderPath
    dirList1 = os.listdir(folder1)
    dirPath1 = os.path.abspath(folder1)

    folder2 = args.outputFolderPath
    def mkdir(path):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
        else:
            pass
    mkdir(folder2)
    dirPath2 = os.path.abspath(folder2)

    if '1' == args.method:
        import PyPDF2
    elif '2' == args.method:
        import pdfplumber
    elif '3' == args.method:
        import fitz
    elif '4' == args.method:
        # from pdfminer.high_level import extract_text
        import io
        from pdfminer.converter import TextConverter
        # from pdfminer.pdfdocument import PDFTextExtractionNotAllowed
        from pdfminer.layout import LAParams
        from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
        from pdfminer.pdfpage import PDFPage

    def pdfToTextMethod1(filePath):
        with open(filePath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
        return text

    def pdfToTextMethod2(filePath):
        with pdfplumber.open(filePath) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
            return text

    def pdfToTextMethod3(filePath):
        # with fitz.open(filePath) as pdf:
        #     text = ''
        #     for page in pdf.pages():
        #         text += page.get_text()
        #     return text
        document = fitz.open(filePath)
        text = ""
        for page in document:
            page_text = page.get_text()
            text += page_text
        document.close()

    def pdfToTextMethod4(filePath):
        # text = extract_text(filePath)
        # return text
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        laparams = LAParams(line_overlap=0.5, char_margin=2.0, line_margin=0.5, word_margin=0.1, boxes_flow=0.5,
                            detect_vertical=False, all_texts=False)
        converter = TextConverter(resource_manager, fake_file_handle, laparams=laparams)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        with open(filePath, 'rb') as fh:
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                page_interpreter.process_page(page)
            text = fake_file_handle.getvalue()
        converter.close()
        fake_file_handle.close()
        return text


    for fileName1 in dirList1:
        filePath1 = os.path.join(dirPath1, fileName1)
        textResultPathName = dirPath2 + '/' + fileName1 + '.txt'
        try:
            if '1' == args.method:
                pdfText = pdfToTextMethod1(filePath1)
            elif '2' == args.method:
                pdfText = pdfToTextMethod2(filePath1)
            elif '3' == args.method:
                pdfText = pdfToTextMethod3(filePath1)
            elif '4' == args.method:
                pdfText = pdfToTextMethod4(filePath1)

            outFile = open(textResultPathName, 'w', encoding='utf-8')
            outFile.write(pdfText)
            outFile.close()
        except BaseException as e:
            print('failed:', fileName1, '|',  e)

    # Created by Huilong Chen.
