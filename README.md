# Password Cracker - Educational Security Tool

A multi-threaded password cracking tool built in Python for educational purposes and authorized security testing. Supports dictionary attacks, brute force attacks, and hybrid approaches with various hash algorithms.

## ⚠️ Ethical Use Warning

This tool is designed **exclusively for educational purposes and authorized security testing**. 

**Legal Use Only:**
- Testing your own passwords and systems
- Authorized penetration testing with written permission
- Security research in controlled environments
- Educational demonstrations and learning

**Never use this tool for:**
- Unauthorized access to systems or accounts
- Cracking passwords you don't own
- Any illegal activity

Unauthorized access to computer systems is illegal in most jurisdictions. Always obtain proper authorization before testing.

## Features

- **Multiple Attack Methods**
  - Dictionary attack with wordlist support
  - Brute force attack with configurable character sets
  - Hybrid attack (dictionary + brute force combinations)
  
- **Hash Algorithm Support**
  - MD5
  - SHA-1
  - SHA-256
  - SHA-512
  - Salt support for all algorithms

- **Performance**
  - Multi-threaded processing
  - Configurable thread count
  - Real-time statistics (attempts, rate, time)
  
- **Dictionary Enhancements**
  - Common password mutations (capitalization, numbers, special chars)
  - Efficient memory usage with generators

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/password-cracker.git
cd password-cracker
```

2. No external dependencies required - uses Python standard library only!

3. Requires Python 3.6 or higher

## Usage

### Basic Syntax

```bash
python main.py -H <hash> -m <method> [options]
```

### Examples

#### 1. Dictionary Attack
```bash
# Basic dictionary attack
python main.py -H 5f4dcc3b5aa765d61d8327deb882cf99 -m dictionary -w wordlists/common.txt

# Dictionary attack with mutations (adds numbers, caps, special chars)
python main.py -H 5f4dcc3b5aa765d61d8327deb882cf99 -m dictionary -w wordlists/common.txt --mutations

# Dictionary attack with SHA-256
python main.py -H 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 -m dictionary -w wordlists/common.txt -a sha256
```

#### 2. Brute Force Attack
```bash
# Brute force up to 4 characters (lowercase)
python main.py -H 098f6bcd4621d373cade4e832627b4f6 -m brute_force --min-len 1 --max-len 4

# Brute force with digits only
python main.py -H 098f6bcd4621d373cade4e832627b4f6 -m brute_force --min-len 1 --max-len 6 --charset digits

# Brute force with custom character set
python main.py -H <hash> -m brute_force --max-len 3 --charset "abc123"
```

#### 3. Hybrid Attack
```bash
# Dictionary + 2 digit suffix (e.g., "password01", "admin99")
python main.py -H <hash> -m hybrid -w wordlists/common.txt --append-len 2

# Dictionary + 2 digit prefix
python main.py -H <hash> -m hybrid -w wordlists/common.txt --append-len 2 --hybrid-mode prefix

# Dictionary + both prefix and suffix
python main.py -H <hash> -m hybrid -w wordlists/common.txt --append-len 1 --hybrid-mode both
```

#### 4. Advanced Options
```bash
# Use 8 threads for faster processing
python main.py -H <hash> -m dictionary -w wordlists/common.txt -t 8

# Crack salted hash
python main.py -H <hash> -m dictionary -w wordlists/common.txt -s "mysalt" -a sha256

# Read hash from file
python main.py -H hash.txt -m dictionary -w wordlists/common.txt
```

### Command Line Options

#### Required Arguments
- `-H, --hash` - Target hash to crack (or path to file containing hash)
- `-m, --method` - Attack method: `dictionary`, `brute_force`, or `hybrid`

#### Hash Options
- `-a, --algorithm` - Hash algorithm: `md5`, `sha1`, `sha256`, `sha512` (default: md5)
- `-s, --salt` - Salt used in hashing (if any)

#### Dictionary Attack Options
- `-w, --wordlist` - Path to wordlist file (required for dictionary/hybrid)
- `--mutations` - Apply common mutations to dictionary words

#### Brute Force Options
- `--min-len` - Minimum password length (default: 1)
- `--max-len` - Maximum password length (default: 4)
- `--charset` - Character set: `lowercase`, `uppercase`, `digits`, `alphanumeric`, `all`, or custom string

#### Hybrid Attack Options
- `--append-len` - Length of brute force portion (default: 2)
- `--hybrid-mode` - Mode: `suffix`, `prefix`, or `both` (default: suffix)

#### Performance Options
- `-t, --threads` - Number of threads for parallel processing (default: 4)

## Project Structure

```
password-cracker/
├── main.py                 # CLI interface
├── cracker.py             # Main cracker orchestrator
├── hash_utils.py          # Hash generation and comparison
├── attacks/               # Attack implementations
│   ├── __init__.py
│   ├── dictionary.py      # Dictionary attack
│   ├── brute_force.py     # Brute force attack
│   └── hybrid.py          # Hybrid attack
├── wordlists/             # Password wordlists
│   └── common.txt         # Sample common passwords
├── tests/                 # Unit tests
└── README.md             # This file
```

## How It Works

### Dictionary Attack
1. Loads words from a wordlist file
2. Optionally applies mutations (capitalization, common number/symbol suffixes)
3. Hashes each candidate and compares to target
4. Uses multi-threading to process multiple words in parallel

### Brute Force Attack
1. Generates all possible combinations of characters up to specified length
2. Tries combinations in order (shortest to longest)
3. Configurable character sets for efficiency

### Hybrid Attack
1. Combines dictionary words with short brute force sequences
2. Can append/prepend digits or custom characters
3. Example: "password" → "password01", "password02", etc.

### Hash Comparison
- Supports multiple algorithms (MD5, SHA-1, SHA-256, SHA-512)
- Optional salt support
- Case-insensitive hash comparison

## Testing the Tool

Generate test hashes:

```python
# Create a test hash
from hash_utils import HashUtils

# MD5 hash of "test"
hash_obj = HashUtils.generate_hash("test", "md5")
print(hash_obj)  # 098f6bcd4621d373cade4e832627b4f6

# SHA-256 hash of "password"
hash_obj = HashUtils.generate_hash("password", "sha256")
print(hash_obj)  # 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8

# Salted hash
hash_obj = HashUtils.generate_hash("admin", "md5", salt="mysalt")
print(hash_obj)
```

Then crack them:
```bash
python main.py -H 098f6bcd4621d373cade4e832627b4f6 -m brute_force --max-len 4
```

## Performance Tips

1. **Use appropriate attack methods**
   - Short passwords (≤6 chars): Brute force
   - Dictionary words: Dictionary attack with mutations
   - Dictionary + numbers: Hybrid attack

2. **Optimize thread count**
   - Start with 4 threads
   - Increase for CPU-heavy systems
   - Too many threads can cause overhead

3. **Choose the right character set**
   - Lowercase only is fastest
   - Add uppercase/digits only if needed
   - Avoid "all" unless necessary

4. **Wordlist quality matters**
   - Use targeted wordlists
   - Smaller, focused lists are often better than huge generic ones

## Educational Value

This project demonstrates:
- **Security concepts**: Password hashing, salt, attack methods
- **Python skills**: Multi-threading, generators, OOP, CLI tools
- **Algorithm design**: Efficient candidate generation, parallel processing
- **Software architecture**: Clean code, modularity, separation of concerns

## Limitations

- **Not for production cracking**: Professional tools (hashcat, John the Ripper) are much faster
- **CPU-bound**: Uses CPU only, no GPU acceleration
- **Simple mutations**: Limited mutation rules compared to advanced tools
- **No rainbow tables**: Computes hashes on-the-fly

## Security Best Practices

When creating passwords:
1. Use at least 12 characters
2. Mix uppercase, lowercase, numbers, and symbols
3. Avoid dictionary words
4. Use unique passwords for each account
5. Consider using a password manager
6. Enable two-factor authentication

## Contributing

This is an educational project. Contributions welcome:
- Additional attack methods
- Performance improvements
- Better documentation
- Test cases
- Additional wordlists

## License

MIT License - See LICENSE file for details

## Disclaimer

This tool is provided for educational purposes only. The authors are not responsible for any misuse or damage caused by this program. Always obtain proper authorization before testing security on systems you don't own.

## Resources

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Hashcat](https://hashcat.net/hashcat/) - Professional password recovery tool
- [John the Ripper](https://www.openwall.com/john/) - Another professional tool
- [SecLists](https://github.com/danielmiessler/SecLists) - Password wordlists collection

## Author

Created as an educational portfolio project demonstrating Python programming, security concepts, and software engineering practices.
