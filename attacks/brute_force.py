"""
Brute force attack implementation.

This module implements a brute force password cracking attack,
trying all possible combinations of characters up to a specified length.
"""

import itertools
import string
from typing import Generator, Set


class BruteForceAttack:
    """Implements brute force password cracking."""
    
    # Predefined character sets
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase
    DIGITS = string.digits
    SPECIAL = string.punctuation
    
    def __init__(self, min_length: int = 1, max_length: int = 4, 
                 charset: str = 'lowercase'):
        """
        Initialize brute force attack.
        
        Args:
            min_length: Minimum password length to try
            max_length: Maximum password length to try
            charset: Character set to use (lowercase, uppercase, digits, 
                    special, alphanumeric, all, or custom string)
        """
        self.min_length = min_length
        self.max_length = max_length
        self.charset = self._get_charset(charset)
    
    def _get_charset(self, charset: str) -> str:
        """
        Get the character set to use for brute forcing.
        
        Args:
            charset: Charset name or custom string
            
        Returns:
            String of characters to use
        """
        preset_charsets = {
            'lowercase': self.LOWERCASE,
            'uppercase': self.UPPERCASE,
            'digits': self.DIGITS,
            'special': self.SPECIAL,
            'alphanumeric': self.LOWERCASE + self.UPPERCASE + self.DIGITS,
            'all': self.LOWERCASE + self.UPPERCASE + self.DIGITS + self.SPECIAL
        }
        
        # Return preset charset if available, otherwise treat as custom
        return preset_charsets.get(charset.lower(), charset)
    
    def estimate_combinations(self) -> int:
        """
        Estimate total number of combinations to try.
        
        Returns:
            Estimated number of password combinations
        """
        total = 0
        charset_size = len(self.charset)
        
        for length in range(self.min_length, self.max_length + 1):
            total += charset_size ** length
        
        return total
    
    def generate_candidates(self) -> Generator[str, None, None]:
        """
        Generate all possible password combinations.
        
        Yields:
            Password candidates to try
        """
        for length in range(self.min_length, self.max_length + 1):
            # Generate all combinations of the current length
            for combination in itertools.product(self.charset, repeat=length):
                yield ''.join(combination)
