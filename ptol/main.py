import argparse
from ptol import query_syntax, remove_duplicates, download_pdfs, pdf_to_text

def main():
    parser = argparse.ArgumentParser(description="ptol: A pipeline for obtaining relevant literature based on given keywords")
    subparsers = parser.add_subparsers(dest='command')

    # query_syntax 子命令
    parser_qs = subparsers.add_parser('query_syntax', help='Generate query statements for literature database searches')
    parser_qs.add_argument('-m', '--mode', choices=['init', 'run'], required=True, help='Mode: init for initialization, run for normal operation')
    parser_qs.add_argument('-i', '--inputFilePath', required=True, help='Input file path containing keywords')
    parser_qs.add_argument('-o', '--outputFilePath', required=True, help='Output file path for query statements')
    parser_qs.set_defaults(func=query_syntax.run_query_syntax)

    # 为其他脚本重复以上步骤来添加子命令
    # remove_duplicates 子命令
    parser_rd = subparsers.add_parser('remove_duplicates', help='Remove duplicate literature')
    parser_rd.add_argument('-i', '--inputFilePath', required=True, help='Input the path to an excel file with a .xlsx extension')
    parser_rd.add_argument('-o', '--outputFilePath', required=True, help='Output file path')
    parser_rd.set_defaults(func=remove_duplicates.run_remove_duplicates)
    
    # download_pdfs 子命令
    parser_dp = subparsers.add_parser('download_pdfs', help='Batch download pdf from sci-hub database according to DOI number')
    parser_dp.add_argument('-i', '--inputFilePath', required=True,
                           help='Input the path to an text file')
    parser_dp.add_argument('-c', '--inputChromedriverPath', required=True, help='Specify the path to chromedriver.exe')
    parser_dp.set_defaults(func=download_pdfs.run_download_pdfs)

    # pdf_to_text 子命令
    parser_pt = subparsers.add_parser('pdf_to_text', help='Batch pdf to text')
    parser_pt.add_argument('-m', '--method', choices=['1', '2', '3', '4'], required=True,
                           help='Input pdf to text method number, there are 1, 2, 3, 4 optional, can only set one of them')
    parser_pt.add_argument('-i', '--inputFolderPath', required=True, help='Enter the path to the folder that contains only pdf literatures')
    parser_pt.add_argument('-o', '--outputFolderPath', required=True, help='Output folder path')
    parser_pt.set_defaults(func=pdf_to_text.run_pdf_to_text)



    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
