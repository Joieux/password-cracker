"""
Hash utility functions for password cracking.

This module provides functions to generate and compare password hashes
using various algorithms (MD5, SHA-1, SHA-256, SHA-512).
"""

import hashlib
from typing import Optional


class HashUtils:
    """Utility class for hash generation and comparison."""
    
    SUPPORTED_ALGORITHMS = ['md5', 'sha1', 'sha256', 'sha512']
    
    @staticmethod
    def generate_hash(password: str, algorithm: str = 'md5', salt: Optional[str] = None) -> str:
        """
        Generate a hash for a given password.
        
        Args:
            password: The password to hash
            algorithm: Hash algorithm to use (md5, sha1, sha256, sha512)
            salt: Optional salt to add before hashing
            
        Returns:
            Hexadecimal hash string
            
        Raises:
            ValueError: If algorithm is not supported
        """
        if algorithm.lower() not in HashUtils.SUPPORTED_ALGORITHMS:
            raise ValueError(f"Unsupported algorithm. Use one of: {HashUtils.SUPPORTED_ALGORITHMS}")
        
        # Add salt if provided
        data = f"{salt}{password}" if salt else password
        
        # Generate hash based on algorithm
        hash_obj = hashlib.new(algorithm.lower())
        hash_obj.update(data.encode('utf-8'))
        return hash_obj.hexdigest()
    
    @staticmethod
    def verify_hash(password: str, target_hash: str, algorithm: str = 'md5', 
                   salt: Optional[str] = None) -> bool:
        """
        Verify if a password matches a target hash.
        
        Args:
            password: Password to verify
            target_hash: Hash to compare against
            algorithm: Hash algorithm used
            salt: Optional salt that was used
            
        Returns:
            True if password matches the hash, False otherwise
        """
        generated_hash = HashUtils.generate_hash(password, algorithm, salt)
        return generated_hash.lower() == target_hash.lower()
    
    @staticmethod
    def identify_hash_type(hash_string: str) -> str:
        """
        Try to identify hash type based on length.
        
        Args:
            hash_string: Hash to identify
            
        Returns:
            Likely hash algorithm name
        """
        hash_length = len(hash_string)
        
        hash_types = {
            32: 'md5',
            40: 'sha1',
            64: 'sha256',
            128: 'sha512'
        }
        
        return hash_types.get(hash_length, 'unknown')
