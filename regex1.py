import re

# Define the regex pattern for UK postcodes
uk_postcode_pattern = r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b'

# Example addresses
addresses = [
    "123 Some Road Name, Town, City, County, PA23 6NH",
    "456 Another Street, Village, PA2 6NH",
    "789 Test Avenue, City, London, EC1R 1UB"
]

# Find postcodes in the addresses
for address in addresses:
    match = re.search(uk_postcode_pattern, address)
    if match:
        print(f"Postcode found: {match.group()}")
    else:
        print("No postcode found in this address")