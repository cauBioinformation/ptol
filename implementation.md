# Pipleline to literature

#### A Pipeline for Obtaining Relevant Literature Based on Given Keywords

It's a pipeline to help researchers accelerate literature searches and information acquisition

Let's start following the steps!

## Step 1

#### Syntax for obtaining query syntaxes for databases such as PubMed based on keywords

1. ##### Common approach

Take PubMed as an example.

Take the subject keywords of our current study (e.g. **Mycotoxin, enzyme, degrade**, degradation, etc.) as an example.

**Website:** https://pubmed.ncbi.nlm.nih.gov/advanced/

###### Search based on search keyword statements

![1](https://figshare.com/ndownloader/files/44639644)

**Note:** When you use a literature database to search for relevant literature resources, we recommend that you optimize your keywords. For example, if your research area of interest is a physician topic, you should perform keyword validation at the MeSH URL (http://www.nlm.nih.gov/mesh/). This is to ensure that the most accurate research vocabulary is used. This maximizes the chance of ensuring that the literature resources searched in the database are the most accurate and relevant.

###### Download all retrieved literature information

![2](https://figshare.com/ndownloader/files/44639641)



For Web of Science:

Website: https://www.webofscience.com/wos/woscc/advanced-search

![3](https://figshare.com/ndownloader/files/44639650)

![4](https://figshare.com/ndownloader/files/44639635)

![5](https://figshare.com/ndownloader/files/44639656)

You can also supplement the relevant literature in other databases such as Google Scholar, Science Direct, etc.

2. ##### Common approach

In order to minimize manual operations, we hereby create a homemade tool, **ptol**, which can be downloaded and installed directly via **pip install ptol**. Once you have installed it, you can view the initial introduction to the subroutine with the **ptol -h** or **ptol --help** commands. Below:

![image-20240222220620104](https://figshare.com/ndownloader/files/44639647)

The subroutine **query_syntax** in ptol automatically generates all possible lexical variations, PubMed and Web of Science query syntaxes, and corresponding download links based on keywords provided by the user.

**Module name:** query_syntax

Usage:

Enter the following command in the terminal to see help on using the program:

```shell
ptol query_syntax -h
```

![image-20240222221454817](https://figshare.com/ndownloader/files/44639638)

All parameters and descriptions are listed below:

| Parameters | Descriptions                                                 |
| ---------- | ------------------------------------------------------------ |
| -m         | When running the script for the first time, use -m init to download the dictionary library first. Once downloaded, use -m run for subsequent run parameters. |
| -i         | Setting the path to a file containing only keywords.         |
| -o         | Setting the output file path.                                |

**Enter the file format:**

keyword 1

keyword 2

keyword 3

...

As shown in the figure below:

![7](https://figshare.com/ndownloader/files/44639653)

**Initialization for the first run**

```shell
ptol query_syntax -m init -i keywords.txt -o my_result.txt
```

![image-20240222221903712](https://figshare.com/ndownloader/files/44639659)

When you see the last line of the terminal print "**Successfully downloaded wordnet and other thesaurus!**", indicating that the initialization is successful, then you can proceed to the use of the program.

**Practical training:**

```shell
ptol query_syntax -m run -i keywords.txt -o my_result.txt
```

Outputs the contents of the file:

![image-20240201150847147](https://figshare.com/ndownloader/files/44639662)

![image-20240201151148043](https://figshare.com/ndownloader/files/44639665)

![image-20240201151409344](https://figshare.com/ndownloader/files/44639668)

After that, according to the results given by this program, go directly from PubMed or Web of Science to download the results of searching literature information. You can refer to the next steps in the section **1. common approach**.

## Step 2

#### Consolidation of literature information

Literature collected from different databases was combined into one file through MS Excel. We keep only the Title and DOI number and save it as an xlsx file. Example:

![11](https://figshare.com/ndownloader/files/44639671)

The file was then processed to remove duplicates using the subroutine **remove_duplicates**.

**Module name:** remove_duplicates

Usage:

Enter the following command in the terminal to see help on using the program:

```shell
ptol remove_duplicates -h
```

![image-20240222222628982](https://figshare.com/ndownloader/files/44639674)

All parameters and descriptions are listed below:

| Parameters | Descriptions                                                 |
| ---------- | ------------------------------------------------------------ |
| -i         | Setting the path to MS Excel files ending in .xlsx extension |
| -o         | Setting the output file path.                                |

**Practical training:**

```shell
ptol remove_duplicates -i all_database_literatures_data.xlsx -o all_database_literatures_data_single.txt
```

Outputs the contents of the file:

![image-20240201192413535](https://figshare.com/ndownloader/files/44639677)

## Step 3

#### Download literatures

Based on the entirety of the relevant literature obtained earlier, a pdf of each piece of literature was downloaded.

**Note:** In order to get all the above literature as fast as possible, we suggest that a one-time batch download can be realized by tools such as **EndNote**, **crawler**, and so on. Please note that at all times, **please respect the copyrights of the authors and publishers of the literature. That is, the acquisition of the target literature is carried out through legal channels.**

Here, we provide the subroutine **download_pdfs** that can batch download pdf format literature. Just for reference.

**Module name:** download_pdfs

Usage:

Enter the following command in the terminal to see help on using the program:

```shell
ptol download_pdfs -h
```

![image-20240222223139589](https://figshare.com/ndownloader/files/44639680)

**Note:** This subroutine is for test use by interested parties only, and in order to comply with the publisher's copyright, please download it from the official link of the literature publisher, or purchase the target literature you need.

## Step 4

#### Convert pdf documents to text files

After downloading all the documents (pdf), use the subroutine **pdf_to_text** for batch processing to convert all the documents into text files.

**Module name:** pdf_to_text

Usage:

Enter the following command in the terminal to see help on using the program:

```shell
ptol pdf_to_text -h
```

![image-20240222223414148](https://figshare.com/ndownloader/files/44639686)

All parameters and descriptions are listed below:

| Parameters | Descriptions                                                 |
| ---------- | ------------------------------------------------------------ |
| -m         | The script provides four kinds of pdf files into text files, respectively, numbered 1, 2, 3, 4, the user can set up according to their own preferences. A run, only one of the methods can be set. The purpose of such a design is that when some of the pdf documents can not be converted into text files, you can put these documents into a separate directory, try another method of conversion. |
| -i         | Setting the path to the folder that includes only pdf-formatted literatures. |
| -o         | Setting the path of output folder, all the text files which are converted successfully will be stored in this directory. |

**Practical training:**

```shell
ptol pdf_to_text -m 4 -i literatures_pdf -o literatures_text
```

View a text-formatted document from the leteratures_text folder as follows:

![image-20240201195232993](https://figshare.com/ndownloader/files/44639683)

**Note:** The file name of the document is logged in the terminal for failed conversions. Convenient for users to follow up.

#### Access to large language modeling tools

After that, following the process described in our article, the research question is prepared manually and then the text file is copied and pasted into the input box of a big language model such as **ChatGPT**. The goal of capturing information from the literature by big language models instead of manually can be realized.

Finally, I sincerely hope that this pipeline can accelerate your research process and wish the best of luck in research.

