# alu_regex-data-extraction-ksheilla
This repository contains a Python-based tool that uses regular expressions (regex) to extract various types of data from a given input string. The tool can identify and extract email addresses, URLs, phone numbers, credit card numbers, times, HTML tags, hashtags, and currency amounts.

The code is designed to be modular, reusable, and easy to extend with additional regex patterns.
 Extracts the following data types:
  - Email Addresses
  - URLs
  - Phone Numbers
  - Credit Card Numbers
  - Times (12-hour and 24-hour formats)
  - HTML Tags
  - Hashtags
  - Currency Amounts
- Modular design for easy extension or modification.
- Supports Python 3.x.

And the expected output should be:
Email Addresses: ['user@example.com', 'firstname.lastname@company.co.uk']
URLs: ['https://www.example.com', 'http://subdomain.example.org/page']
Phone Numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890']
Credit Card Numbers: ['1234 5678 9012 3456', '1234-5678-9012-3456']
Times: ['14:30', '2:30 PM']
HTML Tags: ['<p>', '<div class="example">', '<img src="image.jpg" alt="description">']
Hashtags: ['#example', '#ThisIsAHashtag']
Currency Amounts: ['$19.99', '$1,234.56']
