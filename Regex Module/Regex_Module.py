import re

def main():
    text = input("Enter the text to perform regex operations on: ")
    while True:
        print("\nChoose an option:")
        print("1.  Match a pattern at the start of the string")
        print("2.  Search for a pattern in the string")
        print("3.  Find all occurrences of a pattern")
        print("4.  Replace a pattern with another string")
        print("5.  Split the string by a pattern")
        print("6.  Find email addresses in the text")
        print("7.  Find words with specific character length")
        print("8.  Extract words followed by 'in'")
        print("9.  Check if the text contains digits")
        print("10. Validate a phone number format")
        print("11. Find all uppercase words")
        print("12. Count occurrences of a specific pattern")
        print("13. Extract all hashtags from the text")
        print("14. Validate a URL format")
        print("15. Extract dates in various formats")
        print("16. Find words with repeated characters")
        print("17. Exit")

        choice = input("Enter your choice (1-17): ")

        if choice == '1':
            pattern = input("Enter the pattern to match: ")
            match = re.match(pattern, text)
            print("Match found:", match.group() if match else "No match found.")

        elif choice == '2':
            pattern = input("Enter the pattern to search: ")
            search = re.search(pattern, text)
            print("Search found:", search.group() if search else "No search found.")

        elif choice == '3':
            pattern = input("Enter the pattern to find all occurrences: ")
            findall = re.findall(pattern, text)
            print("Findall results:", findall)

        elif choice == '4':
            pattern = input("Enter the pattern to replace: ")
            replacement = input("Enter the replacement string: ")
            substituted = re.sub(pattern, replacement, text)
            print("Substituted text:", substituted)

        elif choice == '5':
            pattern = input("Enter the pattern to split the string: ")
            split_text = re.split(pattern, text)
            print("Split results:", split_text)

        elif choice == '6':
            email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
            emails = re.findall(email_pattern, text)
            print("Email found:", emails)

        elif choice == '7':
            length = input("Enter the length of words to find (e.g., 3, 4, 5): ")
            quantifier_example = re.findall(rf"\b\w{{{length}}}\b", text)
            print(f"Words with {length} characters:", quantifier_example)

        elif choice == '8':
            group_example = re.findall(r"(\b\w+)\s+in", text)
            print("Words followed by 'in':", group_example)

        elif choice == '9':
            if re.search(r'\d', text):
                print("The text contains digits.")
            else:
                print("No digits found in the text.")

        elif choice == '10':
            phone_pattern = r"^\+?\d{1,3}[- ]?\d{1,4}[- ]?\d{4,10}$"
            if re.match(phone_pattern, text):
                print("Valid phone number format.")
            else:
                print("Invalid phone number format.")

        elif choice == '11':
            uppercase_words = re.findall(r'\b[A-Z]+\b', text)
            print("Uppercase words found:", uppercase_words)

        elif choice == '12':
            pattern = input("Enter the pattern to count occurrences: ")
            count = len(re.findall(pattern, text))
            print(f"The pattern '{pattern}' occurs {count} times.")

        elif choice == '13':
            hashtags = re.findall(r'#\w+', text)
            print("Hashtags found:", hashtags)

        elif choice == '14':
            url_pattern = r"https?://[^\s/$.?#].[^\s]*"
            if re.match(url_pattern, text):
                print("Valid URL format.")
            else:
                print("Invalid URL format.")

        elif choice == '15':
            date_pattern = r"\b\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}\b"
            dates = re.findall(date_pattern, text)
            print("Dates found:", dates)

        elif choice == '16':
            repeat_char_pattern = r"\b\w*(\w)\1\w*\b"
            repeated_words = re.findall(repeat_char_pattern, text)
            print("Words with repeated characters:", repeated_words)

        elif choice == '17':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()