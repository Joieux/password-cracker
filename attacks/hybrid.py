"""
Hybrid attack implementation.

This module combines dictionary and brute force approaches,
appending/prepending short brute force combinations to dictionary words.
"""

import itertools
from typing import Generator
from .dictionary import DictionaryAttack


class HybridAttack:
    """Implements hybrid dictionary + brute force attack."""
    
    def __init__(self, wordlist_path: str, append_length: int = 2, 
                 charset: str = '0123456789'):
        """
        Initialize hybrid attack.
        
        Args:
            wordlist_path: Path to wordlist file
            append_length: Length of brute force suffix/prefix
            charset: Characters to use for brute force portion
        """
        self.dictionary = DictionaryAttack(wordlist_path)
        self.append_length = append_length
        self.charset = charset
    
    def generate_candidates(self, mode: str = 'suffix') -> Generator[str, None, None]:
        """
        Generate hybrid password candidates.
        
        Args:
            mode: 'suffix' to append, 'prefix' to prepend, 'both' for both
            
        Yields:
            Password candidates combining dictionary words and brute force
        """
        # Generate all possible combinations for the brute force portion
        brute_combinations = [''.join(combo) 
                            for combo in itertools.product(self.charset, 
                                                          repeat=self.append_length)]
        
        # For each dictionary word
        for word in self.dictionary.load_wordlist():
            # Try word with suffix
            if mode in ['suffix', 'both']:
                for combo in brute_combinations:
                    yield f"{word}{combo}"
            
            # Try word with prefix
            if mode in ['prefix', 'both']:
                for combo in brute_combinations:
                    yield f"{combo}{word}"
