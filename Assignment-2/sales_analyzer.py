"""
Sales Data Analyzer - Functional Programming with Streams

Key Concepts:
- Functional programming (map, filter, reduce)
- Stream operations using pandas
- Lambda expressions
- Data aggregation and grouping
- Immutable operations
"""

from functools import reduce
from typing import List, Dict, Any, Callable, Tuple
import pandas as pd


class SalesAnalyzer:
    """
    Sales data analyzer implementing functional programming patterns.
    
    All methods are pure functions that don't modify original data.
    Uses functional paradigms: map, filter, reduce, and lambda expressions.
    """
    
    def __init__(self, csv_file_path: str):
        """
        Initialize the analyzer with CSV data.
        
        Args:
            csv_file_path: Path to the CSV file containing sales data
        """
        self.csv_file_path = csv_file_path
        self._raw_data = None
        
    def load_data(self) -> pd.DataFrame:
        """
        Load CSV data into a pandas DataFrame (lazy evaluation pattern). THIS IS IMPORTANT FOR IMMUTABILITY.
        
        Returns:
            DataFrame containing sales data
        """
        if self._raw_data is None:
            self._raw_data = pd.read_csv(self.csv_file_path)
            # Convert date string to datetime for better operations
            self._raw_data['date'] = pd.to_datetime(self._raw_data['date'])
        return self._raw_data.copy()
    
    def get_raw_data(self) -> pd.DataFrame:
        """Get a copy of the raw data (immutable access)."""
        return self.load_data()
    
    # ==================== AGGREGATION OPERATIONS ====================
    
    def calculate_total_revenue(self) -> float:
        """
        Calculate total revenue across all transactions using functional reduce.
        
        Demonstrates: reduce operation, lambda expression
        
        Returns:
            Total revenue as float
        """
        df = self.load_data()
        # Functional approach: reduce with lambda
        return reduce(
            lambda acc, amount: acc + amount,
            df['total_amount'],
            0.0
        )
    
    def calculate_average_transaction_value(self) -> float:
        """
        Calculate average transaction value using map and reduce.
        
        Demonstrates: chaining functional operations
        
        Returns:
            Average transaction value
        """
        df = self.load_data()
        total = reduce(lambda acc, x: acc + x, df['total_amount'], 0.0)
        count = len(df)
        return total / count if count > 0 else 0.0
    
    def get_transaction_count(self) -> int:
        """
        Get total number of transactions.
        
        Returns:
            Count of transactions
        """
        df = self.load_data()
        return len(df)