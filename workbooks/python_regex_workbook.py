# Python Regular Expressions Workbook

import re

print("==== 1. Simple Character Matches ====")
print(re.findall(r"cat", "cat catapult category"))

print("\n==== 2. Special Characters ====")
print(re.findall(r"c.t", "cat cot cut c@t c t"))

print("\n==== 3. Character Classes ====")
print(re.findall(r"\d+", "My phone number is 12345"))

print("\n==== 4. Quantifiers ====")
print(re.findall(r"a{2,4}", "aaaaaab"))

print("\n==== 5. Matching at Beginning or End ====")
print(re.match(r"Hello", "Hello World"))
print(re.search(r"World$", "Hello World"))

print("\n==== 6. Greedy vs Non-Greedy ====")
print(re.findall(r"<.*>", "<tag>content</tag>"))
print(re.findall(r"<.*?>", "<tag>content</tag>"))

print("\n==== 7. Compiling Regular Expressions ====")
pattern = re.compile(r"\d{3}")
print(pattern.findall("123 456 789"))

print("\n==== 8. Grouping ====")
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "2025-08-11")
print(m.groups())

print("\n==== 9. Match Objects ====")
m = re.search(r"cat", "The cat sat")
print(m.group(), m.start(), m.end(), m.span())

print("\n==== 10. match(), search(), sub() ====")
print(re.match(r"cat", "cat sat"))
print(re.search(r"cat", "The cat sat"))
print(re.sub(r"cat", "dog", "The cat sat"))

print("\n==== 11. Splitting a String ====")
print(re.split(r"\s+", "Python is awesome"))

print("\n==== 12. Replacing Text ====")
print(re.sub(r"\d", "*", "Phone: 12345"))

print("\n==== 13. Flags ====")
print(re.findall(r"python", "PYTHON rocks", re.I))

# ==============================
# Exercises
# ==============================

print("\n==== Exercises ====")
# 1. Extract all email addresses from a text
text = "Contact us at support@example.com or sales@example.co.in"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("Emails:", emails)

# 2. Find all words starting with 't'
sentence = "The tiger is chasing the turtle to the town"
t_words = re.findall(r"\bt\w+", sentence, re.I)
print("T words:", t_words)

# 3. Replace all digits in a string with '#'
data = "My ID is 12345 and PIN is 6789"
masked = re.sub(r"\d", "#", data)
print("Masked:", masked)

# 4. Split a string by commas and optional spaces
csv = "apple, banana,grape, mango"
fruits = re.split(r",\s*", csv)
print("Fruits:", fruits)

# 5. Extract dates in format DD/MM/YYYY
dates_text = "Today's date is 11/08/2025 and tomorrow is 12/08/2025"
dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", dates_text)
print("Dates:", dates)

