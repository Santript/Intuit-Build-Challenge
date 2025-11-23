"""
Sales Data Analyzer - Functional Programming with Streams

Demonstrates proficiency with functional programming paradigms by performing
various aggregation and grouping operations on CSV sales data.

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
        Load CSV data into a pandas DataFrame (lazy evaluation pattern).
        
        Returns:
            DataFrame containing sales data
        """
        if self._raw_data is None:
            self._raw_data = pd.read_csv(self.csv_file_path)
            # Convert date string to datetime for better operations
            self._raw_data['date'] = pd.to_datetime(self._raw_data['date'])
        return self._raw_data.copy()  # Return copy to ensure immutability
    
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
    
    # ==================== GROUPING OPERATIONS ====================
    
    def group_by_category(self) -> Dict[str, float]:
        """
        Group sales by product category and calculate total revenue.
        
        Demonstrates: groupby operation, aggregation
        
        Returns:
            Dictionary mapping category to total revenue
        """
        df = self.load_data()
        # Functional grouping with aggregation
        result = df.groupby('product_category')['total_amount'].sum()
        return result.to_dict()
    
    def group_by_region(self) -> Dict[str, Dict[str, Any]]:
        """
        Group by region with multiple statistics.
        
        Demonstrates: complex aggregation with multiple functions
        
        Returns:
            Dictionary with region statistics (sum, avg, count)
        """
        df = self.load_data()
        grouped = df.groupby('region')['total_amount'].agg([
            ('total_revenue', 'sum'),
            ('avg_transaction', 'mean'),
            ('transaction_count', 'count')
        ])
        return grouped.to_dict('index')
    
    def group_by_payment_method(self) -> Dict[str, int]:
        """
        Count transactions by payment method.
        
        Demonstrates: grouping with counting
        
        Returns:
            Dictionary mapping payment method to count
        """
        df = self.load_data()
        return df.groupby('payment_method').size().to_dict()
    
    # ==================== FILTERING OPERATIONS ====================
    
    def filter_by_region(self, region: str) -> pd.DataFrame:
        """
        Filter transactions by region using lambda predicate.
        
        Demonstrates: filter operation with lambda
        
        Args:
            region: Region to filter by
            
        Returns:
            Filtered DataFrame
        """
        df = self.load_data()
        # Functional filtering with lambda
        return df[df.apply(lambda row: row['region'] == region, axis=1)]
    
    def filter_high_value_transactions(self, threshold: float = 100.0) -> pd.DataFrame:
        """
        Filter transactions above a certain value.
        
        Demonstrates: predicate-based filtering
        
        Args:
            threshold: Minimum transaction value
            
        Returns:
            Filtered DataFrame with high-value transactions
        """
        df = self.load_data()
        return df[df['total_amount'] > threshold]
    
    def filter_by_category(self, category: str) -> pd.DataFrame:
        """
        Filter transactions by product category.
        
        Args:
            category: Product category to filter
            
        Returns:
            Filtered DataFrame
        """
        df = self.load_data()
        return df[df['product_category'] == category]
    
    def filter_by_date_range(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Filter transactions within date range.
        
        Demonstrates: complex filtering with multiple conditions
        
        Args:
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            
        Returns:
            Filtered DataFrame
        """
        df = self.load_data()
        start = pd.to_datetime(start_date)
        end = pd.to_datetime(end_date)
        return df[(df['date'] >= start) & (df['date'] <= end)]
    
    # ==================== COMPLEX MULTI-STEP OPERATIONS ====================
    
    def get_top_n_products_by_revenue(self, n: int = 5) -> List[Tuple[str, float]]:
        """
        Get top N products by total revenue (chained operations).
        
        Demonstrates: map → groupby → sort → slice pipeline
        
        Args:
            n: Number of top products to return
            
        Returns:
            List of tuples (product_name, total_revenue)
        """
        df = self.load_data()
        # Functional pipeline: group → aggregate → sort → take top N
        product_revenue = (
            df.groupby('product_name')['total_amount']
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )
        return list(product_revenue.items())
    
    def get_top_n_customers_by_spending(self, n: int = 5) -> List[Tuple[str, float]]:
        """
        Identify top N customers by total spending.
        
        Demonstrates: customer analytics with functional approach
        
        Args:
            n: Number of top customers
            
        Returns:
            List of tuples (customer_id, total_spent)
        """
        df = self.load_data()
        customer_spending = (
            df.groupby('customer_id')['total_amount']
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )
        return list(customer_spending.items())
    
    def analyze_category_performance(self) -> pd.DataFrame:
        """
        Comprehensive category analysis with multiple metrics.
        
        Demonstrates: complex multi-metric aggregation
        
        Returns:
            DataFrame with category statistics
        """
        df = self.load_data()
        return df.groupby('product_category').agg({
            'total_amount': ['sum', 'mean', 'count'],
            'quantity': 'sum'
        }).round(2)
    
    def calculate_monthly_revenue(self) -> Dict[str, float]:
        """
        Calculate revenue by month (time-series aggregation).
        
        Demonstrates: temporal grouping and aggregation
        
        Returns:
            Dictionary mapping month to revenue
        """
        df = self.load_data()
        df['month'] = df['date'].dt.to_period('M')
        monthly = df.groupby('month')['total_amount'].sum()
        # Convert Period to string for serialization
        return {str(k): v for k, v in monthly.items()}
    
    def get_regional_best_sellers(self) -> Dict[str, str]:
        """
        Find best-selling product in each region.
        
        Demonstrates: nested grouping and finding max
        
        Returns:
            Dictionary mapping region to best-selling product
        """
        df = self.load_data()
        # Group by region and product, sum revenue, find max per region
        regional_products = (
            df.groupby(['region', 'product_name'])['total_amount']
            .sum()
            .reset_index()
        )
        
        # Use lambda to find product with max revenue per region
        best_sellers = (
            regional_products
            .loc[regional_products.groupby('region')['total_amount'].idxmax()]
            .set_index('region')['product_name']
        )
        
        return best_sellers.to_dict()
    
    # ==================== FUNCTIONAL UTILITY METHODS ====================
    
    def apply_custom_aggregation(
        self, 
        group_by_column: str, 
        aggregate_column: str,
        aggregation_func: Callable
    ) -> Dict[str, Any]:
        """
        Generic functional aggregation method.
        
        Demonstrates: higher-order functions accepting functions as parameters
        
        Args:
            group_by_column: Column to group by
            aggregate_column: Column to aggregate
            aggregation_func: Function to apply (e.g., sum, max, min)
            
        Returns:
            Dictionary with aggregation results
        """
        df = self.load_data()
        result = df.groupby(group_by_column)[aggregate_column].apply(aggregation_func)
        return result.to_dict()
    
    def chain_operations(
        self,
        filter_func: Callable[[pd.DataFrame], pd.DataFrame],
        aggregate_func: Callable[[pd.DataFrame], Any]
    ) -> Any:
        """
        Chain filter and aggregate operations.
        
        Demonstrates: function composition, higher-order functions
        
        Args:
            filter_func: Function to filter data
            aggregate_func: Function to aggregate filtered data
            
        Returns:
            Result of chained operations
        """
        df = self.load_data()
        filtered = filter_func(df)
        return aggregate_func(filtered)
    
    # ==================== STATISTICS ====================
    
    def get_summary_statistics(self) -> Dict[str, Any]:
        """
        Get comprehensive summary statistics.
        
        Returns:
            Dictionary with various statistics
        """
        df = self.load_data()
        return {
            'total_revenue': self.calculate_total_revenue(),
            'avg_transaction': self.calculate_average_transaction_value(),
            'transaction_count': len(df),
            'unique_customers': df['customer_id'].nunique(),
            'unique_products': df['product_name'].nunique(),
            'date_range': {
                'start': df['date'].min().strftime('%Y-%m-%d'),
                'end': df['date'].max().strftime('%Y-%m-%d')
            }
        }