#!/usr/bin/env python3
"""
Demo script to showcase password cracker capabilities.
Creates sample hashes and cracks them using different methods.
"""

from hash_utils import HashUtils
import subprocess
import os

def run_demo():
    """Run comprehensive demo of password cracker features."""
    
    print("=" * 70)
    print(" PASSWORD CRACKER DEMO ".center(70, "="))
    print("=" * 70)
    print()
    
    # Demo 1: Simple dictionary attack
    print("\n" + "─" * 70)
    print("DEMO 1: Dictionary Attack")
    print("─" * 70)
    print("Creating hash for password 'admin'...")
    hash1 = HashUtils.generate_hash('admin', 'md5')
    print(f"Hash: {hash1}")
    print("\nCracking with dictionary attack...")
    
    os.system(f'python3 main.py -H {hash1} -m dictionary -w wordlists/common.txt -t 2')
    
    # Demo 2: Dictionary with mutations
    print("\n\n" + "─" * 70)
    print("DEMO 2: Dictionary Attack with Mutations")
    print("─" * 70)
    print("Creating hash for password 'Password1'...")
    hash2 = HashUtils.generate_hash('Password1', 'md5')
    print(f"Hash: {hash2}")
    print("\nNote: 'Password1' won't be in wordlist, but mutations will find it")
    print("Cracking with dictionary attack + mutations...")
    
    os.system(f'python3 main.py -H {hash2} -m dictionary -w wordlists/common.txt --mutations -t 2')
    
    # Demo 3: Brute force
    print("\n\n" + "─" * 70)
    print("DEMO 3: Brute Force Attack")
    print("─" * 70)
    print("Creating hash for password 'test'...")
    hash3 = HashUtils.generate_hash('test', 'md5')
    print(f"Hash: {hash3}")
    print("\nCracking with brute force (1-4 chars, lowercase)...")
    
    os.system(f'python3 main.py -H {hash3} -m brute_force --min-len 1 --max-len 4 --charset lowercase -t 2')
    
    # Demo 4: Different hash algorithm
    print("\n\n" + "─" * 70)
    print("DEMO 4: Different Hash Algorithm (SHA-256)")
    print("─" * 70)
    print("Creating SHA-256 hash for password 'hello'...")
    hash4 = HashUtils.generate_hash('hello', 'sha256')
    print(f"Hash: {hash4}")
    print("\nCracking with auto-detection...")
    
    os.system(f'python3 main.py -H {hash4} -m brute_force --max-len 5 --charset lowercase -t 2')
    
    # Demo 5: Salted hash
    print("\n\n" + "─" * 70)
    print("DEMO 5: Salted Hash")
    print("─" * 70)
    print("Creating salted hash for password 'secret' with salt 'mysalt'...")
    hash5 = HashUtils.generate_hash('secret', 'md5', salt='mysalt')
    print(f"Hash: {hash5}")
    print("\nCracking with salt parameter...")
    
    os.system(f'python3 main.py -H {hash5} -m dictionary -w wordlists/common.txt -s mysalt -t 2')
    
    print("\n\n" + "=" * 70)
    print(" DEMO COMPLETE ".center(70, "="))
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. Dictionary attacks are fast for common passwords")
    print("2. Mutations catch common variations (caps, numbers, symbols)")
    print("3. Brute force works for short passwords but gets slow quickly")
    print("4. Different hash algorithms are automatically detected")
    print("5. Salts add security but can still be cracked if known")
    print("\nSecurity Lesson: Use long, random, unique passwords!")
    print()

if __name__ == '__main__':
    run_demo()
