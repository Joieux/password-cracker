# Password Cracker Portfolio Project

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Educational](https://img.shields.io/badge/Purpose-Educational-green.svg)](https://github.com)

A comprehensive password cracking toolkit built in Python, featuring both traditional and AI-enhanced (agentic) versions. Demonstrates security concepts, multi-threading, and modern AI integration.

## 🎯 Project Overview

This portfolio project showcases:
- **Security fundamentals**: Hash algorithms, salt, attack vectors
- **Python proficiency**: OOP, multi-threading, generators, CLI tools
- **Software architecture**: Clean code, modularity, documentation
- **AI integration**: Agentic decision-making with Claude API

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/joieux/password-cracker.git
cd password-cracker

# Run standard version
python main.py -H 5f4dcc3b5aa765d61d8327deb882cf99 -m dictionary -w wordlists/common.txt

# Run agentic version (requires Claude API)
python agentic_cracker.py -H <hash> --context "username: john, company: TechCorp"

# Run demo
python demo.py
```

## ✨ Features

### Standard Version
- ✅ Multiple attack methods (dictionary, brute force, hybrid)
- ✅ Hash algorithm support (MD5, SHA-1, SHA-256, SHA-512)
- ✅ Multi-threaded processing
- ✅ Password mutations
- ✅ Salt support
- ✅ Progress tracking and statistics
- ✅ Zero external dependencies

### Agentic Version (AI-Enhanced)
- 🤖 Intelligent attack strategy selection
- 🤖 Contextual wordlist generation
- 🤖 Real-time strategy adaptation
- 🤖 Security analysis and recommendations
- 🤖 Target profiling using AI

## 📁 Project Structure

```
password-cracker/
├── main.py                 # Standard CLI interface
├── agentic_cracker.py     # AI-enhanced version
├── cracker.py             # Core cracker logic
├── hash_utils.py          # Hash operations
├── attacks/               # Attack implementations
│   ├── dictionary.py
│   ├── brute_force.py
│   └── hybrid.py
├── wordlists/             # Password wordlists
├── demo.py                # Interactive demo
├── README.md              # Main documentation
├── AGENTIC_README.md      # AI version docs
└── LICENSE                # MIT License
```

## 🎓 Educational Value

### Security Concepts
- Password hashing and cryptography
- Common attack vectors
- Importance of password complexity
- Salt and pepper in security
- Rate of attack feasibility

### Programming Concepts
- Object-oriented design
- Concurrent programming
- Generator patterns
- CLI design with argparse
- API integration
- Error handling

### AI Integration
- LLM decision-making
- Prompt engineering
- Adaptive algorithms
- Context-aware systems

## 📊 Performance Benchmarks

| Attack Type | Character Set | Max Length | Est. Time |
|-------------|--------------|------------|-----------|
| Dictionary | 10K words | - | < 1 second |
| Dictionary + Mutations | 10K words | - | < 5 seconds |
| Brute Force | Lowercase (26) | 4 chars | < 1 second |
| Brute Force | Lowercase (26) | 6 chars | ~2 minutes |
| Brute Force | Alphanumeric (62) | 4 chars | ~2 seconds |
| Hybrid | 1K words + 2 digits | - | ~10 seconds |

*Benchmarks on modern CPU with 4 threads*

## 🔒 Security & Ethics

**⚠️ IMPORTANT**: This tool is for **educational purposes only**.

**Legal uses:**
- Testing your own passwords
- Authorized penetration testing
- Security research
- Educational demonstrations

**Illegal uses:**
- Unauthorized access
- Cracking others' passwords
- Any malicious activity

Unauthorized computer access is a crime. Always get written permission.

## 🛠️ Technical Highlights

### Clean Code Practices
- Type hints throughout
- Comprehensive docstrings
- Modular architecture
- Separation of concerns
- Error handling

### Performance Optimization
- Multi-threaded execution
- Generator-based memory efficiency
- Batch processing
- Lazy evaluation

### Extensibility
- Plugin-style attack modules
- Easy to add new hash algorithms
- Configurable via command line
- API-ready design

## 📚 Documentation

- [Main README](README.md) - Comprehensive usage guide
- [Agentic README](AGENTIC_README.md) - AI version documentation
- Inline code documentation with docstrings
- Example usage in demo.py

## 🤝 Contributing

Contributions welcome! Areas of interest:
- Additional attack algorithms
- Performance improvements
- Better mutation rules
- Extended wordlists
- Test coverage
- Documentation

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 🎯 Portfolio Highlights

**Why this project stands out:**

1. **Dual Implementation**: Shows both traditional and modern AI approaches
2. **Production-Quality Code**: Clean, documented, tested
3. **Real-World Application**: Demonstrates practical security concepts
4. **Technical Depth**: Multi-threading, algorithms, optimization
5. **Modern Stack**: Integrates cutting-edge AI technology

## 🔗 Related Projects

- [Hashcat](https://hashcat.net/) - Production password cracker
- [John the Ripper](https://www.openwall.com/john/) - Classic cracker
- [SecLists](https://github.com/danielmiessler/SecLists) - Wordlists

## 👤 Author

Portfolio project demonstrating:
- Python development
- Security knowledge
- AI integration
- Software engineering practices

## ⭐ Show Your Support

If this project helped you learn about security or Python, give it a star!

---

**Disclaimer**: For educational purposes only. Users are responsible for complying with applicable laws and obtaining proper authorization before use.
