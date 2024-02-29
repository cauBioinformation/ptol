import pandas as pd
from selenium import webdriver
import time
import os
import random

def run_download_pdfs(args):
    # chrome_driver_path = "D:/Chrome Downloads/chromedriver.exe"
    chrome_driver_path = args.inputChromedriverPath

    # file_path = 'all_database_literatures_data_single.txt'
    file_path = args.inputFilePath

    table = pd.read_csv(file_path, sep='\t', header=None)

    titles = table[0].copy(deep=True)
    dois = table[1].copy(deep=True)

    def clean_filename(filename):
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        for ch in invalid_chars:
            filename = filename.replace(ch, '_')
        return filename

    def scihub_get(doi, download_path):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": download_path}
        chromeOptions.add_experimental_option("prefs", prefs)
        wd = webdriver.Chrome(executable_path=chrome_driver_path, options=chromeOptions)

        scihub = ['https://sci-hub.ru/', 'https://sci-hub.st/', 'https://sci-hub.se/']
        root = scihub[random.randint(0, 2)]

        wd.get(root + doi)
        time.sleep(1)

        try:
            b = wd.find_element_by_xpath('//*[@id="buttons"]/button')
            b.click()
            time.sleep(20)  # Wait for the download to start
        except:
            print('Access failed. DOI = ' + doi)
            wd.quit()
            return False

        wd.quit()
        return True

    def rename_file(download_path, title, doi):
        time.sleep(5)  # Wait a bit for the download to finish

        # Wait until the download is finished
        temp_file = max([download_path + f for f in os.listdir(download_path)], key=os.path.getctime)
        while '.crdownload' in temp_file:
            time.sleep(1)
            temp_file = max([download_path + f for f in os.listdir(download_path)], key=os.path.getctime)

        clean_title = clean_filename(title)
        clean_doi = clean_filename(doi).replace('/', '_')
        new_file_name = f"{clean_title}_{clean_doi}.pdf"
        os.rename(temp_file, download_path + new_file_name)

    def article_get(titles, dois, i):
        script_directory = os.path.dirname(os.path.abspath(__file__))

        download_path = os.path.join(script_directory, 'download_literatures')

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        title = titles[i]
        doi = dois[i]

        # Visit Sci-Hub
        if doi == 'nan' or title == 'nan':
            print('Missing information. Index = ' + str(i))
        else:
            if scihub_get(doi, download_path):
                rename_file(download_path, title, doi)

    for i in range(len(dois)):
        article_get(titles, dois, i)
