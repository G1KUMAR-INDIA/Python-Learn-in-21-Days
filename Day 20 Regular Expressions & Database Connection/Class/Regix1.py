'''
    What is regix?
        Regular expression (regex) is a sequence of characters that forms a search pattern.
        It is used to match or search for a specific pattern in a text or a string.
'''
import re
pattern=r"Hello"
string="Client Hello, Server!"
# matches=re.match(pattern,string)
matches=re.search(pattern,string)

if matches:
    print("Match found:",matches.group())
    print("Match found at:",matches.start())
else:
    print("No match found")

# using re.findall()
pattern=r"Hello"
string="Client Hello, Server!"
matches=re.findall(pattern,string)
print(matches)

# using re.sub()
text="The color is blue"
updated_text=re.sub(r"blue","red",text)
print(updated_text)

# validating email address
email_pattern=r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
email=input("Enter Email:")
if re.match(email_pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")

# validating phone number
phone_pattern=r"\d{10}$|\d{3}-\d{3}-\d{4}$"
phone=input("Enter Phone Number:")
if re.match(phone_pattern,phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

# extracting phone number from text
text="My phone number is 1234567890 or 123-456-7890"
phone=re.findall(r"\d{10}|\d{3}-\d{3}-\d{4}",text)
print(phone)