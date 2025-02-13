import re

def extract_matches(input_string, regex_pattern):
    return re.findall(regex_pattern, input_string)

input_string = """
user@example.com firstname.lastname@company.co.uk invalid-email
https://www.example.com http://subdomain.example.org/page ftp://not-a-valid-url
(123) 456-7890 123-456-7890 123.456.7890 not-a-phone-number
1234 5678 9012 3456 1234-5678-9012-3456 invalid-card
14:30 2:30 PM invalid-time
<p> <div class="example"> <img src="image.jpg" alt="description">
#example #ThisIsAHashtag invalid-hashtag
$19.99 $1,234.56 invalid-currency
"""

regex_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
regex_url = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/?[^\s]*"
regex_phone = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
regex_credit_card = r"(?:\d{4}[-\s]?){3}\d{4}"
regex_time = r"\b(?:\d{1,2}:\d{2}(?:\s?(?:AM|PM))?)\b"
regex_html_tag = r"<[^>]+>"
regex_hashtag = r"#\w+"
regex_currency = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"

emails = extract_matches(input_string, regex_email)
urls = extract_matches(input_string, regex_url)
phone_numbers = extract_matches(input_string, regex_phone)
credit_cards = extract_matches(input_string, regex_credit_card)
times = extract_matches(input_string, regex_time)
html_tags = extract_matches(input_string, regex_html_tag)
hashtags = extract_matches(input_string, regex_hashtag)
currency_amounts = extract_matches(input_string, regex_currency)

print("Email Addresses:", emails)
print("URLs:", urls)
print("Phone Numbers:", phone_numbers)
print("Credit Card Numbers:", credit_cards)
print("Times:", times)
print("HTML Tags:", html_tags)
print("Hashtags:", hashtags)
print("Currency Amounts:", currency_amounts)


