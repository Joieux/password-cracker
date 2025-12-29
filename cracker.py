"""
Main password cracker implementation.

This module provides the core PasswordCracker class that orchestrates
different attack methods with progress tracking and multi-threading support.
"""

import time
from typing import Optional, Callable, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from hash_utils import HashUtils
from attacks import DictionaryAttack, BruteForceAttack, HybridAttack


class PasswordCracker:
    """Main password cracker orchestrator."""
    
    def __init__(self, target_hash: str, algorithm: str = 'md5', 
                 salt: Optional[str] = None, num_threads: int = 4):
        """
        Initialize password cracker.
        
        Args:
            target_hash: Hash to crack
            algorithm: Hash algorithm (md5, sha1, sha256, sha512)
            salt: Optional salt used in hashing
            num_threads: Number of threads for parallel processing
        """
        self.target_hash = target_hash.lower()
        self.algorithm = algorithm.lower()
        self.salt = salt
        self.num_threads = num_threads
        self.hash_utils = HashUtils()
        
        # Statistics
        self.attempts = 0
        self.start_time = None
        self.found_password = None
    
    def _check_password(self, password: str) -> bool:
        """
        Check if a password matches the target hash.
        
        Args:
            password: Password to check
            
        Returns:
            True if match found, False otherwise
        """
        self.attempts += 1
        return self.hash_utils.verify_hash(password, self.target_hash, 
                                          self.algorithm, self.salt)
    
    def _crack_batch(self, candidates: list) -> Optional[str]:
        """
        Try to crack password from a batch of candidates.
        
        Args:
            candidates: List of password candidates to try
            
        Returns:
            Found password or None
        """
        for candidate in candidates:
            if self._check_password(candidate):
                return candidate
        return None
    
    def crack(self, attack_method: str, **attack_params) -> Dict[str, Any]:
        """
        Attempt to crack the password using specified attack method.
        
        Args:
            attack_method: 'dictionary', 'brute_force', or 'hybrid'
            **attack_params: Parameters specific to the attack method
            
        Returns:
            Dictionary with results (password, time, attempts, success)
        """
        self.start_time = time.time()
        self.attempts = 0
        self.found_password = None
        
        # Initialize attack based on method
        if attack_method == 'dictionary':
            attack = DictionaryAttack(**attack_params)
        elif attack_method == 'brute_force':
            attack = BruteForceAttack(**attack_params)
        elif attack_method == 'hybrid':
            attack = HybridAttack(**attack_params)
        else:
            raise ValueError(f"Unknown attack method: {attack_method}")
        
        # Single-threaded approach for simpler attacks
        if attack_method == 'brute_force' or self.num_threads == 1:
            for candidate in attack.generate_candidates():
                if self._check_password(candidate):
                    self.found_password = candidate
                    break
        else:
            # Multi-threaded approach for dictionary and hybrid attacks
            self._crack_multithreaded(attack)
        
        elapsed_time = time.time() - self.start_time
        
        return {
            'success': self.found_password is not None,
            'password': self.found_password,
            'attempts': self.attempts,
            'time_elapsed': elapsed_time,
            'rate': self.attempts / elapsed_time if elapsed_time > 0 else 0
        }
    
    def _crack_multithreaded(self, attack) -> None:
        """
        Crack password using multiple threads.
        
        Args:
            attack: Attack instance that generates candidates
        """
        batch_size = 1000
        batch = []
        
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = []
            
            for candidate in attack.generate_candidates():
                batch.append(candidate)
                
                if len(batch) >= batch_size:
                    # Submit batch for processing
                    future = executor.submit(self._crack_batch, batch.copy())
                    futures.append(future)
                    batch = []
                    
                    # Check if any thread found the password
                    for future in as_completed(futures):
                        result = future.result()
                        if result:
                            self.found_password = result
                            # Cancel remaining futures
                            for f in futures:
                                f.cancel()
                            return
                    
                    futures = []
            
            # Process remaining batch
            if batch and not self.found_password:
                result = self._crack_batch(batch)
                if result:
                    self.found_password = result
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get current cracking statistics.
        
        Returns:
            Dictionary with current statistics
        """
        elapsed_time = time.time() - self.start_time if self.start_time else 0
        
        return {
            'attempts': self.attempts,
            'time_elapsed': elapsed_time,
            'rate': self.attempts / elapsed_time if elapsed_time > 0 else 0,
            'found': self.found_password is not None
        }
