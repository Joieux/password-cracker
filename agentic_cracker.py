#!/usr/bin/env python3
"""
Agentic Password Cracker - AI-Enhanced Security Tool

An intelligent password cracker that uses Claude AI to:
1. Analyze target systems and suggest optimal attack strategies
2. Generate custom wordlists based on target context
3. Adapt attack methods based on real-time results
4. Provide security recommendations

For educational and authorized security testing only.
"""

import argparse
import sys
import os
import json
import time
from typing import Dict, List, Any, Optional
from cracker import PasswordCracker
from hash_utils import HashUtils


class AgenticPasswordCracker:
    """AI-enhanced password cracker using Claude for intelligent decision making."""
    
    def __init__(self, target_hash: str, algorithm: str = 'md5', 
                 salt: Optional[str] = None, num_threads: int = 4):
        """
        Initialize agentic password cracker.
        
        Args:
            target_hash: Hash to crack
            algorithm: Hash algorithm
            salt: Optional salt
            num_threads: Number of threads
        """
        self.cracker = PasswordCracker(target_hash, algorithm, salt, num_threads)
        self.target_hash = target_hash
        self.algorithm = algorithm
        self.context = {}
        self.attack_history = []
    
    def call_claude(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Make a request to Claude API for intelligent analysis.
        
        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            
        Returns:
            Claude's response text
        """
        try:
            import urllib.request
            import json
            
            # Prepare request
            url = "https://api.anthropic.com/v1/messages"
            
            messages = [{"role": "user", "content": prompt}]
            
            data = {
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 1000,
                "messages": messages
            }
            
            if system_prompt:
                data["system"] = system_prompt
            
            # Make request
            req = urllib.request.Request(
                url,
                data=json.dumps(data).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode('utf-8'))
                
            # Extract text from response
            if 'content' in result and len(result['content']) > 0:
                return result['content'][0]['text']
            else:
                return "Error: No response from Claude"
                
        except Exception as e:
            return f"Error calling Claude API: {e}"
    
    def analyze_target(self, context_info: str) -> Dict[str, Any]:
        """
        Use Claude to analyze target and recommend attack strategy.
        
        Args:
            context_info: Information about the target (username, system, etc.)
            
        Returns:
            Dictionary with recommended strategy
        """
        print("[*] Analyzing target with AI...")
        
        prompt = f"""You are a security expert helping with authorized penetration testing.

Target Information:
- Hash: {self.target_hash}
- Algorithm: {self.algorithm}
- Context: {context_info}

Based on this information, recommend the best password cracking strategy.

Provide your response as JSON with this structure:
{{
    "recommended_attack": "dictionary|brute_force|hybrid",
    "reasoning": "why this approach is best",
    "suggested_wordlists": ["list", "of", "keywords", "to", "try"],
    "estimated_difficulty": "easy|medium|hard",
    "tips": ["specific tips for this target"]
}}

Only respond with valid JSON, no other text."""

        response = self.call_claude(prompt)
        
        try:
            # Parse JSON response
            strategy = json.loads(response)
            return strategy
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return {
                "recommended_attack": "dictionary",
                "reasoning": "Default strategy",
                "suggested_wordlists": ["password", "admin", "test"],
                "estimated_difficulty": "medium",
                "tips": ["Try common passwords first"]
            }
    
    def generate_contextual_wordlist(self, context: str) -> List[str]:
        """
        Generate a custom wordlist based on target context using Claude.
        
        Args:
            context: Context about the target
            
        Returns:
            List of password candidates
        """
        print("[*] Generating contextual wordlist with AI...")
        
        prompt = f"""Generate a list of 50 likely passwords for this target:

Context: {context}

Consider:
- Common patterns (name + year, name + number)
- Keyboard patterns
- Common substitutions (@ for a, 3 for e, etc.)
- Company/personal relevant terms
- Common password patterns

Return ONLY a JSON array of passwords, no other text.
Example: ["password123", "admin2024", ...]"""

        response = self.call_claude(prompt)
        
        try:
            # Try to parse as JSON
            wordlist = json.loads(response)
            if isinstance(wordlist, list):
                return wordlist[:50]  # Limit to 50
        except:
            pass
        
        # Fallback: extract words from response
        words = []
        for line in response.split('\n'):
            line = line.strip().strip('"\'[],' )
            if line and len(line) < 30:
                words.append(line)
        
        return words[:50] if words else ["password", "admin", "test"]
    
    def adapt_strategy(self, attempts: int, time_elapsed: float) -> str:
        """
        Use Claude to adapt attack strategy based on progress.
        
        Args:
            attempts: Number of attempts so far
            time_elapsed: Time elapsed
            
        Returns:
            Recommended next action
        """
        print("[*] Consulting AI for strategy adaptation...")
        
        rate = attempts / time_elapsed if time_elapsed > 0 else 0
        
        prompt = f"""You are analyzing an ongoing password cracking attempt.

Current Status:
- Attempts: {attempts:,}
- Time: {time_elapsed:.1f} seconds
- Rate: {rate:.0f} attempts/second
- Hash algorithm: {self.algorithm}
- Previous attacks: {len(self.attack_history)}

Should we:
1. Continue current attack
2. Switch to different attack method
3. Try a more targeted approach
4. Stop (password unlikely to be simple)

Respond with JSON:
{{
    "recommendation": "continue|switch|targeted|stop",
    "reasoning": "why",
    "next_action": "specific next step if changing approach"
}}

Only respond with valid JSON."""

        response = self.call_claude(prompt)
        
        try:
            decision = json.loads(response)
            return decision.get('recommendation', 'continue')
        except:
            return 'continue'
    
    def run_intelligent_crack(self, context: str, wordlist_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Run an AI-guided password cracking session.
        
        Args:
            context: Context information about target
            wordlist_path: Optional path to initial wordlist
            
        Returns:
            Cracking results
        """
        print("\n" + "="*60)
        print("AGENTIC PASSWORD CRACKER")
        print("="*60)
        
        # Step 1: Analyze target
        strategy = self.analyze_target(context)
        print(f"\n[AI] Recommended Attack: {strategy['recommended_attack']}")
        print(f"[AI] Reasoning: {strategy['reasoning']}")
        print(f"[AI] Difficulty: {strategy['estimated_difficulty']}")
        print(f"[AI] Tips: {', '.join(strategy['tips'])}")
        
        # Step 2: Generate contextual wordlist
        ai_wordlist = self.generate_contextual_wordlist(context)
        print(f"\n[AI] Generated {len(ai_wordlist)} contextual password candidates")
        
        # Save AI wordlist to temporary file
        ai_wordlist_path = '/tmp/ai_wordlist.txt'
        with open(ai_wordlist_path, 'w') as f:
            for word in ai_wordlist:
                f.write(f"{word}\n")
        
        # Step 3: Try AI-generated wordlist first
        print("\n[*] Phase 1: Trying AI-generated wordlist...")
        result = self.cracker.crack(
            'dictionary',
            wordlist_path=ai_wordlist_path,
            use_mutations=True
        )
        
        if result['success']:
            print(f"\n[+] SUCCESS! Password found: {result['password']}")
            self._print_security_recommendations(result['password'], context)
            return result
        
        print(f"[*] AI wordlist exhausted ({result['attempts']:,} attempts)")
        
        # Step 4: Try standard wordlist if provided
        if wordlist_path:
            print("\n[*] Phase 2: Trying standard wordlist...")
            result = self.cracker.crack(
                'dictionary',
                wordlist_path=wordlist_path,
                use_mutations=True
            )
            
            if result['success']:
                print(f"\n[+] SUCCESS! Password found: {result['password']}")
                self._print_security_recommendations(result['password'], context)
                return result
        
        # Step 5: Consult AI for next steps
        decision = self.adapt_strategy(result['attempts'], result['time_elapsed'])
        
        if decision == 'stop':
            print("\n[AI] Recommendation: Password likely not simple. Consider:")
            print("    - More specialized wordlists")
            print("    - Longer brute force (may take hours/days)")
            print("    - Social engineering for more context")
        elif decision == 'switch':
            print("\n[*] Phase 3: Switching to brute force (short passwords)...")
            result = self.cracker.crack(
                'brute_force',
                min_length=1,
                max_length=4,
                charset='alphanumeric'
            )
            
            if result['success']:
                print(f"\n[+] SUCCESS! Password found: {result['password']}")
                self._print_security_recommendations(result['password'], context)
                return result
        
        return result
    
    def _print_security_recommendations(self, cracked_password: str, context: str):
        """
        Use Claude to provide security recommendations based on cracked password.
        
        Args:
            cracked_password: The password that was cracked
            context: Context about the target
        """
        print("\n" + "="*60)
        print("AI SECURITY ANALYSIS")
        print("="*60)
        
        prompt = f"""A password was successfully cracked in a security test:

Password: {cracked_password}
Context: {context}
Hash Algorithm: {self.algorithm}

Provide a brief security analysis:
1. Why was this password weak?
2. What made it easy to crack?
3. Three specific recommendations for a stronger password

Keep response under 200 words."""

        response = self.call_claude(
            prompt,
            system_prompt="You are a cybersecurity expert providing constructive feedback."
        )
        
        print(f"\n{response}")
        print("="*60)


def main():
    """Main entry point for agentic cracker."""
    parser = argparse.ArgumentParser(
        description='Agentic Password Cracker - AI-Enhanced Security Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
This version uses Claude AI to:
- Analyze targets and recommend optimal strategies
- Generate contextual password candidates
- Adapt attack methods in real-time
- Provide security recommendations

Examples:
  # Crack with AI assistance
  python agentic_cracker.py -H 5f4dcc3b5aa765d61d8327deb882cf99 --context "User: john.smith, Company: TechCorp"
  
  # Use AI with existing wordlist
  python agentic_cracker.py -H hash.txt --context "Personal blog, owner loves cats" -w wordlists/common.txt

Note: Requires Claude API access. For educational purposes only.
        """
    )
    
    parser.add_argument('-H', '--hash', required=True,
                       help='Target hash to crack')
    parser.add_argument('--context', required=True,
                       help='Context about the target (username, company, interests, etc.)')
    parser.add_argument('-a', '--algorithm', default='md5',
                       choices=['md5', 'sha1', 'sha256', 'sha512'],
                       help='Hash algorithm (default: md5)')
    parser.add_argument('-s', '--salt', default=None,
                       help='Salt used in hashing (if any)')
    parser.add_argument('-w', '--wordlist', default=None,
                       help='Optional standard wordlist to try after AI wordlist')
    parser.add_argument('-t', '--threads', type=int, default=4,
                       help='Number of threads (default: 4)')
    
    args = parser.parse_args()
    
    # Read hash from file if it's a file path
    target_hash = args.hash
    if os.path.isfile(args.hash):
        with open(args.hash, 'r') as f:
            target_hash = f.read().strip()
    
    # Auto-detect algorithm
    detected = HashUtils.identify_hash_type(target_hash)
    if detected != 'unknown' and args.algorithm == 'md5':
        args.algorithm = detected
        print(f"[*] Auto-detected hash type: {detected}")
    
    # Initialize agentic cracker
    agentic = AgenticPasswordCracker(
        target_hash=target_hash,
        algorithm=args.algorithm,
        salt=args.salt,
        num_threads=args.threads
    )
    
    try:
        # Run intelligent cracking
        result = agentic.run_intelligent_crack(
            context=args.context,
            wordlist_path=args.wordlist
        )
        
        # Print final results
        print("\n" + "="*60)
        print("FINAL RESULTS")
        print("="*60)
        if result['success']:
            print(f"[+] Password: {result['password']}")
        else:
            print("[-] Password not found")
        print(f"[*] Total attempts: {result['attempts']:,}")
        print(f"[*] Time: {result['time_elapsed']:.2f} seconds")
        print(f"[*] Rate: {result['rate']:.0f} attempts/second")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\n[!] Attack interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
