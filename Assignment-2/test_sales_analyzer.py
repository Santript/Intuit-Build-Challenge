"""
Comprehensive test suite for Sales Analyzer
Demonstrates functional programming, stream operations, and data aggregation testing

Test Categories:
- basic: Basic aggregation tests
- grouping: Grouping operations
- filtering: Filter operations with predicates
- complex: Multi-step analysis operations
- edge_case: Edge cases and error handling
- performance: Large dataset operations
"""

import pytest
import pandas as pd
import os
from sales_analyzer import SalesAnalyzer


@pytest.fixture
def analyzer():
    """Fixture providing SalesAnalyzer instance with test data."""
    csv_path = os.path.join(os.path.dirname(__file__), 'sales_data.csv')
    return SalesAnalyzer(csv_path)


@pytest.fixture
def sample_data():
    """Fixture providing the raw DataFrame for validation."""
    csv_path = os.path.join(os.path.dirname(__file__), 'sales_data.csv')
    return pd.read_csv(csv_path)


# ==================== BASIC AGGREGATION TESTS ====================

@pytest.mark.basic
def test_total_revenue_calculation(analyzer, sample_data):
    """
    Test basic revenue aggregation using functional reduce.
    
    Demonstrates: reduce operation, lambda expressions
    """
    print("\n=== Test: Total Revenue Calculation ===")
    
    total = analyzer.calculate_total_revenue()
    expected = sample_data['total_amount'].sum()
    
    print(f"Total Revenue: ${total:,.2f}")
    print(f"Expected: ${expected:,.2f}")
    
    assert abs(total - expected) < 0.01, f"Expected {expected}, got {total}"
    assert total > 0, "Total revenue should be positive"
    print("✓ Total revenue calculated correctly using functional reduce")


@pytest.mark.basic
def test_average_transaction_value(analyzer, sample_data):
    """
    Test average calculation using functional operations.
    
    Demonstrates: chaining map and reduce
    """
    print("\n=== Test: Average Transaction Value ===")
    
    avg = analyzer.calculate_average_transaction_value()
    expected = sample_data['total_amount'].mean()
    
    print(f"Average Transaction: ${avg:.2f}")
    print(f"Expected: ${expected:.2f}")
    
    assert abs(avg - expected) < 0.01
    assert avg > 0
    print("✓ Average transaction value calculated correctly")


@pytest.mark.basic
def test_transaction_count(analyzer):
    """Test basic counting operation."""
    print("\n=== Test: Transaction Count ===")
    
    count = analyzer.get_transaction_count()
    
    print(f"Total Transactions: {count}")
    
    assert count == 50, f"Expected 50 transactions, got {count}"
    print("✓ Transaction count correct (50 rows)")