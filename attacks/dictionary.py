"""
Dictionary attack implementation.

This module implements a dictionary-based password cracking attack,
optionally with common mutations (capitalization, numbers, special chars).
"""

from typing import Optional, Generator, List
import itertools


class DictionaryAttack:
    """Implements dictionary-based password cracking."""
    
    def __init__(self, wordlist_path: str, use_mutations: bool = False):
        """
        Initialize dictionary attack.
        
        Args:
            wordlist_path: Path to wordlist file
            use_mutations: Whether to apply common mutations to words
        """
        self.wordlist_path = wordlist_path
        self.use_mutations = use_mutations
    
    def load_wordlist(self) -> Generator[str, None, None]:
        """
        Load and yield words from wordlist file.
        
        Yields:
            Words from the wordlist, one at a time
        """
        try:
            with open(self.wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    word = line.strip()
                    if word:
                        yield word
        except FileNotFoundError:
            raise FileNotFoundError(f"Wordlist not found: {self.wordlist_path}")
    
    def generate_mutations(self, word: str) -> List[str]:
        """
        Generate common mutations of a word.
        
        Common patterns:
        - Original word
        - Capitalized
        - Uppercase
        - With common number suffixes (1, 123, etc.)
        - With common special char suffixes (!, @, etc.)
        
        Args:
            word: Base word to mutate
            
        Returns:
            List of mutated versions
        """
        mutations = [word]
        
        # Capitalization variants
        mutations.append(word.capitalize())
        mutations.append(word.upper())
        mutations.append(word.lower())
        
        # Common number suffixes
        for num in ['1', '123', '12', '1234', '2024', '2025']:
            mutations.append(f"{word}{num}")
            mutations.append(f"{word.capitalize()}{num}")
        
        # Common special character suffixes
        for char in ['!', '@', '#', '$']:
            mutations.append(f"{word}{char}")
            mutations.append(f"{word.capitalize()}{char}")
        
        # Combined: capitalize + number + special
        for num in ['1', '123']:
            for char in ['!', '@']:
                mutations.append(f"{word.capitalize()}{num}{char}")
        
        # Remove duplicates while preserving order
        seen = set()
        unique_mutations = []
        for mutation in mutations:
            if mutation not in seen:
                seen.add(mutation)
                unique_mutations.append(mutation)
        
        return unique_mutations
    
    def generate_candidates(self) -> Generator[str, None, None]:
        """
        Generate password candidates from wordlist.
        
        Yields:
            Password candidates to try
        """
        for word in self.load_wordlist():
            if self.use_mutations:
                # Yield all mutations of the word
                for mutation in self.generate_mutations(word):
                    yield mutation
            else:
                # Yield just the word
                yield word
