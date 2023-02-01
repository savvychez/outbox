import imaplib, email, os
from dotenv import load_dotenv

def main():
    load_dotenv()

    ADDR = os.getenv("ADDR")
    PASS = os.getenv("PASS")
    IMAP = os.getenv("IMAP")

if __name__ == "__main__":
    main()