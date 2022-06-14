# Simple Python Script that Hashes Passwords In Python

### What does this program do?
This program utilises a 256-bit Secure Hash Algorithm (SHA-256) to produce irreversible and unique hashes.
It generates a random salt using the `os.urandom`.
Hash key is then generated using the SHA-256 algorithm for HMAC. The users password is converted to bytes.
The salt and the hash are then stored.

### Files included
There are currently two files included.

1) hasher.py
2) password_hasher.py