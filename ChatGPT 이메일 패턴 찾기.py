#ChatGPT 이메일 패턴 찾기
import re

# Function to check if an email address is valid
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.search(pattern, email):
        return True
    else:
        return False

# List of sample email addresses
email_samples = [
    "user@example.com",       # Valid
    "john.doe@gmail.com",     # Valid
    "contact@website.co.uk",  # Valid
    "invalid_email",          # Invalid
    "missing@tld.",           # Invalid
    "name@domain",            # Invalid
    "user123@123.com",        # Valid
    "no_space@example.com",   # Valid
    "invalid@.com",           # Invalid
    "12345@gmail.com"         # Valid
]

# Iterate through each email address and check its validity
for email in email_samples:
    valid_status = "valid" if is_valid_email(email) else "invalid"
    print(f"{email} is {valid_status}")
