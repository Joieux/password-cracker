#!/usr/bin/env python3
"""
Password Cracker - Educational Tool

A multi-threaded password cracking tool supporting dictionary, brute force,
and hybrid attacks. For educational and authorized security testing only.
"""

import argparse
import sys
import os
from cracker import PasswordCracker
from hash_utils import HashUtils


def print_banner():
    """Print tool banner."""
    banner = """
    ╔═══════════════════════════════════════╗
    ║     Password Cracker - Educational    ║
    ║         Use Responsibly Only          ║
    ╚═══════════════════════════════════════╝
    """
    print(banner)


def format_time(seconds: float) -> str:
    """Format time in human-readable format."""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
    else:
        return f"{seconds / 3600:.2f} hours"


def format_rate(rate: float) -> str:
    """Format attempts per second."""
    if rate > 1000000:
        return f"{rate / 1000000:.2f}M/s"
    elif rate > 1000:
        return f"{rate / 1000:.2f}K/s"
    else:
        return f"{rate:.2f}/s"


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Password Cracker - Educational Security Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dictionary attack with MD5
  python main.py -H 5f4dcc3b5aa765d61d8327deb882cf99 -m dictionary -w wordlists/common.txt
  
  # Brute force attack (4 chars, lowercase)
  python main.py -H 098f6bcd4621d373cade4e832627b4f6 -m brute_force --min-len 1 --max-len 4
  
  # Dictionary attack with mutations
  python main.py -H hash.txt -m dictionary -w wordlists/common.txt --mutations
  
  # Hybrid attack (dictionary + 2 digits)
  python main.py -H hash.txt -m hybrid -w wordlists/common.txt --append-len 2

Note: This tool is for educational purposes and authorized security testing only.
        """
    )
    
    # Required arguments
    parser.add_argument('-H', '--hash', required=True,
                       help='Target hash to crack (or file containing hash)')
    parser.add_argument('-m', '--method', required=True,
                       choices=['dictionary', 'brute_force', 'hybrid'],
                       help='Attack method to use')
    
    # Hash options
    parser.add_argument('-a', '--algorithm', default='md5',
                       choices=['md5', 'sha1', 'sha256', 'sha512'],
                       help='Hash algorithm (default: md5)')
    parser.add_argument('-s', '--salt', default=None,
                       help='Salt used in hashing (if any)')
    
    # Dictionary attack options
    parser.add_argument('-w', '--wordlist', 
                       help='Path to wordlist file (required for dictionary/hybrid)')
    parser.add_argument('--mutations', action='store_true',
                       help='Apply common mutations to dictionary words')
    
    # Brute force attack options
    parser.add_argument('--min-len', type=int, default=1,
                       help='Minimum password length (default: 1)')
    parser.add_argument('--max-len', type=int, default=4,
                       help='Maximum password length (default: 4)')
    parser.add_argument('--charset', default='lowercase',
                       help='Character set: lowercase, uppercase, digits, alphanumeric, all, or custom (default: lowercase)')
    
    # Hybrid attack options
    parser.add_argument('--append-len', type=int, default=2,
                       help='Length of brute force suffix (default: 2)')
    parser.add_argument('--hybrid-mode', default='suffix',
                       choices=['suffix', 'prefix', 'both'],
                       help='Hybrid mode: suffix, prefix, or both (default: suffix)')
    
    # Performance options
    parser.add_argument('-t', '--threads', type=int, default=4,
                       help='Number of threads (default: 4)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.method in ['dictionary', 'hybrid'] and not args.wordlist:
        parser.error(f"{args.method} attack requires --wordlist")
    
    # Read hash from file if it's a file path
    target_hash = args.hash
    if os.path.isfile(args.hash):
        with open(args.hash, 'r') as f:
            target_hash = f.read().strip()
    
    # Auto-detect algorithm if not specified
    if args.algorithm == 'md5':
        detected = HashUtils.identify_hash_type(target_hash)
        if detected != 'unknown':
            args.algorithm = detected
            print(f"[*] Auto-detected hash type: {detected}")
    
    print_banner()
    print(f"[*] Target hash: {target_hash}")
    print(f"[*] Algorithm: {args.algorithm}")
    print(f"[*] Attack method: {args.method}")
    if args.salt:
        print(f"[*] Salt: {args.salt}")
    print(f"[*] Threads: {args.threads}")
    print()
    
    # Initialize cracker
    cracker = PasswordCracker(
        target_hash=target_hash,
        algorithm=args.algorithm,
        salt=args.salt,
        num_threads=args.threads
    )
    
    # Prepare attack parameters
    attack_params = {}
    
    if args.method == 'dictionary':
        attack_params = {
            'wordlist_path': args.wordlist,
            'use_mutations': args.mutations
        }
        print(f"[*] Wordlist: {args.wordlist}")
        if args.mutations:
            print("[*] Using mutations: enabled")
    
    elif args.method == 'brute_force':
        attack_params = {
            'min_length': args.min_len,
            'max_length': args.max_len,
            'charset': args.charset
        }
        from attacks.brute_force import BruteForceAttack
        bf = BruteForceAttack(**attack_params)
        total = bf.estimate_combinations()
        print(f"[*] Character set: {args.charset}")
        print(f"[*] Length range: {args.min_len}-{args.max_len}")
        print(f"[*] Estimated combinations: {total:,}")
    
    elif args.method == 'hybrid':
        attack_params = {
            'wordlist_path': args.wordlist,
            'append_length': args.append_len,
            'mode': args.hybrid_mode
        }
        print(f"[*] Wordlist: {args.wordlist}")
        print(f"[*] Hybrid mode: {args.hybrid_mode}")
        print(f"[*] Append length: {args.append_len}")
    
    print("\n[*] Starting attack...\n")
    
    # Run the attack
    try:
        result = cracker.crack(args.method, **attack_params)
        
        print("\n" + "="*50)
        if result['success']:
            print("[+] PASSWORD FOUND!")
            print(f"[+] Password: {result['password']}")
        else:
            print("[-] Password not found")
        
        print(f"[*] Attempts: {result['attempts']:,}")
        print(f"[*] Time: {format_time(result['time_elapsed'])}")
        print(f"[*] Rate: {format_rate(result['rate'])}")
        print("="*50)
        
    except KeyboardInterrupt:
        print("\n\n[!] Attack interrupted by user")
        stats = cracker.get_statistics()
        print(f"[*] Attempts made: {stats['attempts']:,}")
        print(f"[*] Time elapsed: {format_time(stats['time_elapsed'])}")
        sys.exit(1)
    
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
