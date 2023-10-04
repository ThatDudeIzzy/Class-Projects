import re

entry_count = 1

while True:
    print("\n" + "*" * 50)
    text = input(f"Entry {entry_count} - Copy paste entire text block (or type 'exit' to stop): ")
    if text.lower() == 'exit':
        break
    criteria_match = re.search(r"CRITERIA- Restriction= (.*?)(?=PREFERENCES)", text, re.I | re.S)
    preferences_match = re.search(r"PREFERENCES: (.*$)", text, re.I | re.S)
    criteria = criteria_match.group(1).strip() if criteria_match else "Not Found"
    preferences = preferences_match.group(1).strip() if preferences_match else "Not Found"
    name_match = re.search(r"Name: (.*?)(?=Date Established:)", preferences, re.I | re.S)
    date_established_match = re.search(r"Date Established: (.*?)(?=Date Terminated:)", preferences, re.I | re.S)
    amount_donated_match = re.search(r"Amount Donated to Establish Scholarship: (\$[\d,]+)", preferences, re.I | re.S)
    principle_donor_match = re.search(r"Principle Donor\(s\): (.*?)(?=Contact\(s\):)", preferences, re.I | re.S)
    contact_match = re.search(r"Contact\(s\): (.*?)(?=Comments:)", preferences, re.I | re.S)
    comments_match = re.search(r"Comments: (.*$)", preferences, re.I | re.S)
    name = name_match.group(1).strip() if name_match else "Not Found"
    date_established = date_established_match.group(1).strip() if date_established_match else "Not Found"
    amount_donated = amount_donated_match.group(1).strip() if amount_donated_match else "Not Found"
    principle_donor = principle_donor_match.group(1).strip() if principle_donor_match else "Not Found"
    contact = contact_match.group(1).strip() if contact_match else "Not Found"
    comments = comments_match.group(1).strip() if comments_match else "Not Found"

    print("\nExtracted Information:")
    print("Criteria Restriction:", criteria)
    print("Preferences:", preferences)
    print("\nFormatted Information:")
    print("Name:", name)
    print("Date Established:", date_established)
    print("Amount Donated to Establish Scholarship:", amount_donated)
    print("Principle Donor(s):", principle_donor)
    print("Contact(s):", contact)
    print("Comments:", comments)

    entry_count += 1