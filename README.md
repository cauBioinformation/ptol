# Pipeline to literature (ptol)

#### A Pipeline for Obtaining Relevant Literature Based on Given Keywords

| Author  | Huilong Chen           |
| ------- | ---------------------- |
| Email   | chenhuilong131@163.com |
| License | MIT                    |

## Description

The ptol is a pipeline tool specifically designed for researchers to accelerate access to target literature and provide usable input files for large language models such as ChatGPT. The ptol is a python package that is divided into four main modules, namely query_syntax, remove_duplicates, download_pdfs, pdf_ to_text.

## Installation

The ptol can be deployed in Windows, Linux, and Mac OS operating systems and can be installed via pip:

```
pip install ptol
```

## Usage

Please look at the [ptol usage tutorial](https://github.com/cauBioinformation/ptol/blob/main/implementation.md) for detailed run instructions and examples.

Once all the dependencies are in place, running ptol is relatively simple. The main ptol script wraps around all of its individual modules, which you can call independently.

```
ptol -h
    Usage: ptol [module] --help
    Options:
    
    query_syntax      | Generate query statements for literature database searches
    remove_duplicates | Remove duplicate literature
    download_pdfs     | Batch download pdf from sci-hub database according to DOI number
    pdf_to_text       | Batch pdf file to text file
```

Each module is run separately. For example, to run the query_syntax module:

```
ptol query_syntax -h

Usage: ptol query_syntax [options] -m run -i keywords.txt -o my_result.txt
Options:
		
	-m | Mode: init for intialization, run for normal opetation
	-i | Input file path containing keywords
	-o | Output file path for query statements
```

I sincerely hope that this pipeline can accelerate your research process and wish the best of luck in research.