"""Attack modules for password cracking."""

from .dictionary import DictionaryAttack
from .brute_force import BruteForceAttack
from .hybrid import HybridAttack

__all__ = ['DictionaryAttack', 'BruteForceAttack', 'HybridAttack']
