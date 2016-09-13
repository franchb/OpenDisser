#!/usr/bin/python3.5
# -*- coding: utf8 -*-
# Script for parcing Russian Dissertation Data
# Source:
# Destination: CSV file
#
# Python 3.5
# Concerting the http://docs.python-guide.org/en/latest/writing/style/
#
#
# CREDITS:
# Author: Ilya Rusin <franchb@protonmail.ch>
# Sergey Saltykov <sergey.saltykov@gmail.com>
#
# @Ageism Dev Team
# Created on 10 September 2016
##
##
# Code License: MIT
##


# Main OpenDisser Scraper

#Constants
url_domain = 'http://expertft.ru'
url_first_page = '/klassifikatory/tprf/'
csv_dir = '../csv/'
csv_fname = 'link-list-'
csv1 = 'link-list-2016-06-17_12-51-39.csv'

url = url_domain + url_first_page

# Set HTTP Headers following the Ethical Web Scraping Practice
# Note: site administrators stay healthy when our bot looks like a human

# Code snippet from @andriy-ivaneyko on StackOverflow
headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'ru-RU,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
           }