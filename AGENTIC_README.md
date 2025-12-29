# Agentic Password Cracker - AI-Enhanced Version

An intelligent password cracking tool that leverages Claude AI to make smart decisions about attack strategies, generate contextual wordlists, and adapt in real-time.

## What Makes It "Agentic"?

Unlike the standard version which requires manual configuration, the agentic version:

1. **Analyzes targets intelligently** - Examines hash type, context, and target information to recommend optimal attack strategies
2. **Generates custom wordlists** - Creates contextual password candidates based on username, company, interests, etc.
3. **Adapts in real-time** - Monitors progress and dynamically adjusts strategy if initial approaches fail
4. **Provides security insights** - Explains why passwords were weak and how to improve them

## How It Works

### Phase 1: AI Analysis
Claude analyzes your target information and recommends:
- Best attack method (dictionary/brute force/hybrid)
- Estimated difficulty
- Specific tips for this target

### Phase 2: Contextual Wordlist Generation
Based on context like:
- Username (john.smith → johnsmith, jsmith, john123)
- Company (TechCorp → techcorp, tech123, techcorp2024)
- Interests (loves cats → fluffy, whiskers, meow123)

Claude generates 50 highly likely password candidates.

### Phase 3: Intelligent Attack
- Tries AI-generated wordlist with mutations
- Falls back to standard wordlist if provided
- Consults AI to decide next steps based on progress

### Phase 4: Security Analysis
When successful, Claude explains:
- Why the password was weak
- What made it easy to crack
- How to create stronger passwords

## Setup

### Prerequisites
- Python 3.6+
- Access to Anthropic's Claude API

### API Configuration
The agentic version uses Claude's API. In the artifact environment, API authentication is handled automatically. If running locally, you would need an API key.

## Usage

### Basic Command
```bash
python agentic_cracker.py -H <hash> --context "<target info>"
```

### Examples

#### 1. Crack with username context
```bash
python agentic_cracker.py \
  -H 5f4dcc3b5aa765d61d8327deb882cf99 \
  --context "User: john.smith, works at TechCorp, loves hiking"
```

#### 2. Personal account with interests
```bash
python agentic_cracker.py \
  -H e10adc3949ba59abbe56e057f20f883e \
  --context "Personal blog owner, cat lover, born 1990"
```

#### 3. Corporate context
```bash
python agentic_cracker.py \
  -H hash.txt \
  --context "Admin account for Acme Inc, created 2024" \
  -w wordlists/common.txt
```

#### 4. With SHA-256
```bash
python agentic_cracker.py \
  -H 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 \
  --context "Database admin, username: dbadmin" \
  -a sha256
```

### Command Line Options

Same as standard version, plus:
- `--context` **(required)** - Context about the target for AI analysis

## Example Output

```
============================================================
AGENTIC PASSWORD CRACKER
============================================================

[*] Analyzing target with AI...

[AI] Recommended Attack: dictionary
[AI] Reasoning: Given the username pattern and company context, 
     dictionary attack with mutations is most efficient
[AI] Difficulty: medium
[AI] Tips: Focus on name variations, company terms, common years

[AI] Generated 50 contextual password candidates

[*] Phase 1: Trying AI-generated wordlist...

[+] SUCCESS! Password found: JohnSmith2024!

============================================================
AI SECURITY ANALYSIS
============================================================

This password was weak because:
1. It follows a predictable pattern (Name + Year + Special char)
2. Contains personal information (username) making it guessable
3. Common substitution pattern is easily defeated by mutation rules

Recommendations:
1. Use a passphrase: "correct-horse-battery-staple" style
2. Avoid personal information (names, birthdates, company names)
3. Use a password manager to generate truly random passwords
============================================================

============================================================
FINAL RESULTS
============================================================
[+] Password: JohnSmith2024!
[*] Total attempts: 847
[*] Time: 2.34 seconds
[*] Rate: 362 attempts/second
============================================================
```

## Comparison: Standard vs Agentic

| Feature | Standard | Agentic |
|---------|----------|---------|
| **Attack Selection** | Manual | AI-recommended |
| **Wordlist** | Pre-made files | AI-generated + contextual |
| **Strategy Adaptation** | Fixed | Dynamic based on progress |
| **Context Awareness** | None | Analyzes target info |
| **Success Rate** | Good | Better (targeted approach) |
| **Setup Complexity** | Simpler | Requires API |
| **Educational Value** | High | Very High |

## When to Use Each Version

### Use Standard Version When:
- Learning password cracking fundamentals
- No API access available
- Testing with existing wordlists
- Need complete control over attack parameters
- Working offline

### Use Agentic Version When:
- Have specific target context
- Want optimized attack strategy
- Learning AI-enhanced security testing
- Need adaptive approach
- Demonstrating modern AI capabilities

## Educational Insights

This project demonstrates:

### AI Integration
- Using LLMs for decision-making in security tools
- Prompt engineering for structured outputs
- Combining AI with traditional algorithms

### Security Concepts
- Why context matters in password security
- How attackers use OSINT (Open Source Intelligence)
- Pattern-based password weaknesses

### Software Architecture
- Agent-based system design
- API integration best practices
- Fallback strategies for AI failures

## Limitations

1. **API Dependency**: Requires Claude API access
2. **Speed**: AI calls add latency (2-5 seconds per call)
3. **Cost**: API calls have usage costs (though minimal for this use)
4. **Determinism**: AI outputs vary slightly between runs
5. **Network**: Requires internet connection

## Advanced Tips

### Providing Better Context
More context = better AI recommendations:

**Good context:**
```
"Username: jsmith, Company: TechCorp, Department: Engineering, 
 Joined: 2023, Hobbies: photography, mountain biking"
```

**Basic context:**
```
"User: john"
```

### Combining with OSINT
Research target before running:
- LinkedIn profile
- Social media
- Company website
- Public databases

Feed this context to the AI for even better results.

## Security & Ethics

The agentic version makes it even easier to crack passwords, which highlights:

1. **Why strong passwords matter** - Personal info makes you vulnerable
2. **OSINT risks** - Public information aids attackers
3. **Defense strategies** - Use random passwords, 2FA, password managers

**Remember**: This tool is for education and authorized testing only.

## Future Enhancements

Potential improvements:
- [ ] Multi-model support (GPT-4, etc.)
- [ ] Learning from previous cracks
- [ ] Automated OSINT gathering
- [ ] Pattern analysis across multiple targets
- [ ] Real-time progress visualization
- [ ] Export detailed AI reasoning logs

## Troubleshooting

### "Error calling Claude API"
- Check API access/configuration
- Verify internet connection
- Check API rate limits

### AI generates invalid JSON
- The code includes fallback parsing
- Will default to reasonable strategies
- May generate fewer candidates

### Slow performance
- AI calls add 2-5 seconds each
- Use standard version for speed-critical tasks
- Consider caching AI responses

## Contributing

Ideas welcome:
- Better AI prompts
- Additional analysis features
- Integration with other AI models
- Performance optimizations

## License

Same MIT License as standard version - See LICENSE file.

## Resources

- [Anthropic Claude API](https://docs.anthropic.com/)
- [AI Safety in Security Tools](https://www.anthropic.com/index/claude-api)
- Standard Password Cracker README for baseline concepts

---

**Created as an educational demonstration of AI-enhanced security tooling.**
