# 🔐 Password Cracker - Project Index

**Quick navigation guide for your complete password cracking toolkit**

---

## 🎯 START HERE

**New to the project?** Read these in order:
1. 📄 `PROJECT_SUMMARY.md` - Overview and quick start (you are here!)
2. 📄 `README.md` - Comprehensive documentation
3. 🎬 `demo.py` - Run this to see examples

**Setting up GitHub?** 
→ Read `GITHUB_SETUP.md`

**Using AI version?**
→ Read `AGENTIC_README.md`

---

## 🚀 Run The Tools

### Standard Version
```bash
# Quick test
python3 main.py -H 5f4dcc3b5aa765d61d8327deb882cf99 -m dictionary -w wordlists/common.txt

# Full options
python3 main.py --help
```

### AI-Enhanced Version
```bash
# With context
python3 agentic_cracker.py -H <hash> --context "username: john, company: TechCorp"

# Full options
python3 agentic_cracker.py --help
```

### Demo & Tests
```bash
# See examples
python3 demo.py

# Run tests
python3 tests/test_cracker.py

# Setup everything
./setup.sh
```

---

## 📁 File Guide

### 🎮 Executables (Run These)
| File | Purpose | Command |
|------|---------|---------|
| `main.py` | Standard cracker | `python3 main.py -H <hash> -m <method>` |
| `agentic_cracker.py` | AI version | `python3 agentic_cracker.py -H <hash> --context ""` |
| `demo.py` | See examples | `python3 demo.py` |
| `setup.sh` | Install/test | `./setup.sh` |

### 📚 Documentation (Read These)
| File | What's Inside |
|------|---------------|
| `README.md` | Complete usage guide |
| `AGENTIC_README.md` | AI version docs |
| `GITHUB_README.md` | Portfolio-focused overview |
| `GITHUB_SETUP.md` | Repository setup guide |
| `PROJECT_SUMMARY.md` | This summary! |

### 🔧 Core Code (The Engine)
| File | What It Does |
|------|--------------|
| `cracker.py` | Main cracking orchestrator |
| `hash_utils.py` | Hash generation/verification |
| `attacks/dictionary.py` | Dictionary attack logic |
| `attacks/brute_force.py` | Brute force logic |
| `attacks/hybrid.py` | Hybrid attack logic |

### 🧪 Testing (Verify Quality)
| File | Purpose |
|------|---------|
| `tests/test_cracker.py` | Unit tests |

### 📦 Configuration
| File | Purpose |
|------|---------|
| `requirements.txt` | Dependencies (none!) |
| `.gitignore` | Git exclusions |
| `LICENSE` | MIT License |

### 💾 Data
| File | Contents |
|------|----------|
| `wordlists/common.txt` | Sample passwords |

---

## 🎓 Learn By Example

### Example 1: Crack a Simple Password
```bash
# Create a hash
python3 -c "from hash_utils import HashUtils; print(HashUtils.generate_hash('test', 'md5'))"
# Output: 098f6bcd4621d373cade4e832627b4f6

# Crack it
python3 main.py -H 098f6bcd4621d373cade4e832627b4f6 -m brute_force --max-len 4
```

### Example 2: Use AI Assistant
```bash
# AI analyzes context and generates targeted wordlist
python3 agentic_cracker.py \
  -H 5f4dcc3b5aa765d61d8327deb882cf99 \
  --context "User loves cats, born 1990, works at PetCorp"
```

### Example 3: Dictionary with Mutations
```bash
# Will find "Password123!" even though wordlist just has "password"
python3 main.py -H <hash> -m dictionary -w wordlists/common.txt --mutations
```

---

## 🎨 Feature Matrix

### Standard vs Agentic Comparison

| Feature | Standard | Agentic |
|---------|----------|---------|
| **Speed** | ⚡⚡⚡ Fast | ⚡⚡ Slower (API calls) |
| **Setup** | ✅ Simple | 🔧 Needs API |
| **Targeting** | 🎯 Manual | 🎯🎯🎯 AI-optimized |
| **Adaptability** | ➡️ Fixed | 🔄 Dynamic |
| **Learning Value** | 📚 High | 📚📚 Very High |
| **Dependencies** | 0️⃣ None | 🌐 Internet + API |

---

## 🔍 Code Quality Highlights

```
✅ Type hints throughout
✅ Comprehensive docstrings  
✅ Modular architecture
✅ Unit tests included
✅ Error handling
✅ Multi-threading support
✅ Generator patterns (memory efficient)
✅ Clean code principles
✅ Professional structure
```

---

## 📊 Project Stats

- **Total Files:** 20+
- **Lines of Code:** ~2,500+
- **Documentation:** ~5,000+ words
- **Test Coverage:** Core functions
- **External Dependencies:** 0
- **Python Version:** 3.6+
- **Supported OS:** Linux, macOS, Windows

---

## 🎯 Use Cases

### Educational
- Learning password security
- Understanding hash algorithms
- Studying attack methodologies
- Practicing Python coding

### Professional
- Portfolio project
- Security demonstration
- Teaching tool
- Interview talking point

### Authorized Testing
- Personal password auditing
- Penetration testing (with permission)
- Security research
- Compliance checking

---

## ⚡ Quick Commands Cheatsheet

```bash
# Standard attacks
python3 main.py -H <hash> -m dictionary -w wordlists/common.txt
python3 main.py -H <hash> -m brute_force --max-len 4
python3 main.py -H <hash> -m hybrid -w wordlists/common.txt

# Add mutations
--mutations

# Change algorithm
-a sha256

# More threads
-t 8

# With salt
-s "mysalt"

# AI version
python3 agentic_cracker.py -H <hash> --context "user info"

# Utilities
./setup.sh                    # Setup
python3 demo.py              # Demo
python3 tests/test_cracker.py # Test
```

---

## 🌟 Portfolio Presentation

**Elevator Pitch:**
"An educational password cracking toolkit demonstrating both traditional cryptographic attacks and modern AI-enhanced optimization. Features clean architecture, comprehensive testing, and professional documentation."

**Key Selling Points:**
1. Shows evolution from traditional → AI-enhanced
2. Production-quality code
3. Strong security knowledge
4. Modern tech stack

---

## 📞 Next Steps

1. ✅ Review `PROJECT_SUMMARY.md` (you're here!)
2. ⚙️ Run `./setup.sh` to test everything
3. 🎬 Run `python3 demo.py` to see it in action
4. 📖 Read `README.md` for comprehensive details
5. 🚀 Follow `GITHUB_SETUP.md` to publish
6. 💼 Add to your portfolio!

---

## 🎉 You're All Set!

Your complete, professional password cracker project is ready to showcase your:
- Python skills
- Security knowledge  
- Software engineering practices
- Modern AI integration

**Remember: Educational use only! Always get authorization before testing systems.**

Good luck! 🚀

---

*Project created as an educational demonstration of password security concepts and AI-enhanced security tooling.*
