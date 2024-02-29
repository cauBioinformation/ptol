#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

# open('README.md').read() # ChatGPT4用的这个，孙朋川自己改了下，为了预防没有自动关闭README.md的问题。
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='ptol',
    version='0.1.2',
    python_requires='>=3.8',
    author='Huilong Chen',
    author_email='chenhuilong131@163.com',
    description='A Pipeline for Obtaining Relevant Literature Based on Given Keywords',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT License",
    url="https://github.com/ChenHuilong1223/Pipeline_to_literature",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'selenium',
        'nltk',
        'inflect',
        'PyPDF2',
        'pdfplumber',
        'PyMuPDF', # 注意：fitz 现在是 PyMuPDF 的一部分
        'pdfminer.six'
    ],
    entry_points={
        'console_scripts': [
            'ptol=ptol.main:main',
        ],
    },
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)
