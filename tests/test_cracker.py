#!/usr/bin/env python3
"""
Unit tests for password cracker components.
Run with: python -m pytest test_cracker.py
or: python test_cracker.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hash_utils import HashUtils
from attacks.dictionary import DictionaryAttack
from attacks.brute_force import BruteForceAttack
from cracker import PasswordCracker


class TestHashUtils:
    """Test hash utility functions."""
    
    def test_md5_generation(self):
        """Test MD5 hash generation."""
        result = HashUtils.generate_hash('test', 'md5')
        expected = '098f6bcd4621d373cade4e832627b4f6'
        assert result == expected, f"Expected {expected}, got {result}"
        print("✓ MD5 generation test passed")
    
    def test_sha256_generation(self):
        """Test SHA-256 hash generation."""
        result = HashUtils.generate_hash('password', 'sha256')
        expected = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
        assert result == expected, f"Expected {expected}, got {result}"
        print("✓ SHA-256 generation test passed")
    
    def test_salted_hash(self):
        """Test salted hash generation."""
        result = HashUtils.generate_hash('admin', 'md5', salt='salt123')
        # Hash of "salt123admin"
        expected = HashUtils.generate_hash('salt123admin', 'md5')
        assert result == expected
        print("✓ Salted hash test passed")
    
    def test_verify_hash(self):
        """Test hash verification."""
        target = '5f4dcc3b5aa765d61d8327deb882cf99'  # MD5 of "password"
        assert HashUtils.verify_hash('password', target, 'md5')
        assert not HashUtils.verify_hash('wrong', target, 'md5')
        print("✓ Hash verification test passed")
    
    def test_identify_hash_type(self):
        """Test hash type identification."""
        assert HashUtils.identify_hash_type('a' * 32) == 'md5'
        assert HashUtils.identify_hash_type('a' * 40) == 'sha1'
        assert HashUtils.identify_hash_type('a' * 64) == 'sha256'
        assert HashUtils.identify_hash_type('a' * 128) == 'sha512'
        print("✓ Hash identification test passed")


class TestDictionaryAttack:
    """Test dictionary attack."""
    
    def test_load_wordlist(self):
        """Test wordlist loading."""
        # Create temp wordlist
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("password\nadmin\ntest\n")
            temp_path = f.name
        
        try:
            attack = DictionaryAttack(temp_path)
            words = list(attack.load_wordlist())
            assert 'password' in words
            assert 'admin' in words
            assert 'test' in words
            print("✓ Wordlist loading test passed")
        finally:
            os.unlink(temp_path)
    
    def test_mutations(self):
        """Test password mutations."""
        attack = DictionaryAttack('dummy.txt', use_mutations=True)
        mutations = attack.generate_mutations('test')
        
        # Check for expected mutations
        assert 'test' in mutations
        assert 'Test' in mutations
        assert 'TEST' in mutations
        assert 'test123' in mutations
        assert 'test!' in mutations
        print("✓ Mutation generation test passed")


class TestBruteForceAttack:
    """Test brute force attack."""
    
    def test_charset_selection(self):
        """Test character set selection."""
        attack_lower = BruteForceAttack(charset='lowercase')
        assert attack_lower.charset == 'abcdefghijklmnopqrstuvwxyz'
        
        attack_digits = BruteForceAttack(charset='digits')
        assert attack_digits.charset == '0123456789'
        print("✓ Charset selection test passed")
    
    def test_combination_estimation(self):
        """Test combination count estimation."""
        attack = BruteForceAttack(min_length=1, max_length=2, charset='lowercase')
        # 26 (single) + 26^2 (double) = 702
        expected = 26 + 676
        assert attack.estimate_combinations() == expected
        print("✓ Combination estimation test passed")
    
    def test_candidate_generation(self):
        """Test candidate generation."""
        attack = BruteForceAttack(min_length=1, max_length=2, charset='ab')
        candidates = list(attack.generate_candidates())
        
        # Should generate: a, b, aa, ab, ba, bb (6 total)
        assert len(candidates) == 6
        assert 'a' in candidates
        assert 'ab' in candidates
        assert 'bb' in candidates
        print("✓ Candidate generation test passed")


class TestPasswordCracker:
    """Test main password cracker."""
    
    def test_simple_crack(self):
        """Test cracking a simple password."""
        import tempfile
        
        # Create temp wordlist
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("password\nadmin\ntest\n")
            temp_path = f.name
        
        try:
            # MD5 of "test"
            target = '098f6bcd4621d373cade4e832627b4f6'
            cracker = PasswordCracker(target, algorithm='md5', num_threads=1)
            
            result = cracker.crack('dictionary', wordlist_path=temp_path)
            
            assert result['success']
            assert result['password'] == 'test'
            assert result['attempts'] >= 1
            print("✓ Simple crack test passed")
        finally:
            os.unlink(temp_path)
    
    def test_failed_crack(self):
        """Test when password is not found."""
        import tempfile
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("wrong\nincorrect\n")
            temp_path = f.name
        
        try:
            # MD5 of "notinlist"
            target = HashUtils.generate_hash('notinlist', 'md5')
            cracker = PasswordCracker(target, algorithm='md5', num_threads=1)
            
            result = cracker.crack('dictionary', wordlist_path=temp_path)
            
            assert not result['success']
            assert result['password'] is None
            print("✓ Failed crack test passed")
        finally:
            os.unlink(temp_path)


def run_all_tests():
    """Run all test classes."""
    print("\n" + "=" * 60)
    print("Running Password Cracker Unit Tests")
    print("=" * 60 + "\n")
    
    # Test HashUtils
    print("Testing HashUtils...")
    hash_tests = TestHashUtils()
    hash_tests.test_md5_generation()
    hash_tests.test_sha256_generation()
    hash_tests.test_salted_hash()
    hash_tests.test_verify_hash()
    hash_tests.test_identify_hash_type()
    
    # Test DictionaryAttack
    print("\nTesting DictionaryAttack...")
    dict_tests = TestDictionaryAttack()
    dict_tests.test_load_wordlist()
    dict_tests.test_mutations()
    
    # Test BruteForceAttack
    print("\nTesting BruteForceAttack...")
    brute_tests = TestBruteForceAttack()
    brute_tests.test_charset_selection()
    brute_tests.test_combination_estimation()
    brute_tests.test_candidate_generation()
    
    # Test PasswordCracker
    print("\nTesting PasswordCracker...")
    cracker_tests = TestPasswordCracker()
    cracker_tests.test_simple_crack()
    cracker_tests.test_failed_crack()
    
    print("\n" + "=" * 60)
    print("All Tests Passed! ✓")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    run_all_tests()
