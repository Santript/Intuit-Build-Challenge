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


# ==================== GROUPING OPERATIONS TESTS ====================

@pytest.mark.grouping
def test_group_by_category(analyzer):
    """
    Test grouping by category with aggregation.
    
    Demonstrates: groupby operation, functional aggregation
    """
    print("\n=== Test: Group By Category ===")
    
    category_revenue = analyzer.group_by_category()
    
    print("Revenue by Category:")
    for category, revenue in sorted(category_revenue.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category}: ${revenue:,.2f}")
    
    # Assertions
    assert 'Electronics' in category_revenue, "Electronics category should exist"
    assert 'Clothing' in category_revenue, "Clothing category should exist"
    assert 'Food' in category_revenue, "Food category should exist"
    assert 'Books' in category_revenue, "Books category should exist"
    
    # All revenues should be positive
    assert all(v > 0 for v in category_revenue.values()), "All revenues should be positive"
    
    # Electronics should have highest revenue (based on our data)
    assert category_revenue['Electronics'] > category_revenue['Food'], \
        "Electronics should have higher revenue than Food"
    
    print("✓ Grouping by category works correctly")


@pytest.mark.grouping
def test_group_by_region(analyzer):
    """
    Test multi-metric regional grouping.
    
    Demonstrates: complex aggregation with multiple functions
    """
    print("\n=== Test: Group By Region ===")
    
    regional_stats = analyzer.group_by_region()
    
    print("Regional Statistics:")
    for region, stats in regional_stats.items():
        print(f"\n  {region}:")
        print(f"    Total Revenue: ${stats['total_revenue']:,.2f}")
        print(f"    Avg Transaction: ${stats['avg_transaction']:.2f}")
        print(f"    Transaction Count: {stats['transaction_count']}")
    
    # Check all regions exist
    assert 'North' in regional_stats
    assert 'South' in regional_stats
    assert 'East' in regional_stats
    assert 'West' in regional_stats
    
    # Validate structure
    for region, stats in regional_stats.items():
        assert 'total_revenue' in stats
        assert 'avg_transaction' in stats
        assert 'transaction_count' in stats
        assert stats['total_revenue'] > 0
        assert stats['avg_transaction'] > 0
        assert stats['transaction_count'] > 0
    
    print("\n✓ Regional grouping with multiple metrics works correctly")


@pytest.mark.grouping
def test_group_by_payment_method(analyzer):
    """
    Test grouping by payment method with counting.
    
    Demonstrates: grouping with size/count operations
    """
    print("\n=== Test: Group By Payment Method ===")
    
    payment_counts = analyzer.group_by_payment_method()
    
    print("Transactions by Payment Method:")
    for method, count in sorted(payment_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {method}: {count} transactions")
    
    # Check payment methods exist
    assert len(payment_counts) > 0, "Should have payment methods"
    
    # All counts should be positive
    assert all(c > 0 for c in payment_counts.values())
    
    # Sum should equal total transactions
    total_count = sum(payment_counts.values())
    assert total_count == 50, f"Total count should be 50, got {total_count}"
    
    print("✓ Payment method grouping works correctly")


# ==================== FILTERING OPERATIONS TESTS ====================

@pytest.mark.filtering
def test_filter_by_region(analyzer):
    """
    Test filtering by region using lambda predicate.
    
    Demonstrates: filter operation with lambda
    """
    print("\n=== Test: Filter By Region ===")
    
    region = 'North'
    filtered = analyzer.filter_by_region(region)
    
    print(f"Transactions in {region}: {len(filtered)}")
    print(f"Sample transactions:")
    for _, row in filtered.head(3).iterrows():
        print(f"  {row['transaction_id']}: {row['product_name']} - ${row['total_amount']:.2f}")
    
    # All filtered items should be from North
    assert all(filtered['region'] == region), "All transactions should be from North"
    assert len(filtered) > 0, "Should have transactions from North"
    
    # Test immutability - original data unchanged
    total_regions = len(analyzer.load_data())
    assert total_regions == 50, "Original data should remain unchanged"
    
    print("✓ Region filtering works correctly")


@pytest.mark.filtering
def test_filter_high_value_transactions(analyzer):
    """
    Test filtering with numeric predicate.
    
    Demonstrates: predicate-based filtering
    """
    print("\n=== Test: Filter High Value Transactions ===")
    
    threshold = 100.0
    high_value = analyzer.filter_high_value_transactions(threshold)
    
    print(f"Transactions above ${threshold}: {len(high_value)}")
    print("Top 5 high-value transactions:")
    top_5 = high_value.nlargest(5, 'total_amount')
    for _, row in top_5.iterrows():
        print(f"  {row['transaction_id']}: {row['product_name']} - ${row['total_amount']:,.2f}")
    
    # All should be above threshold
    assert all(high_value['total_amount'] > threshold), \
        f"All transactions should be above ${threshold}"
    
    # Should have some high-value transactions
    assert len(high_value) > 0, "Should have transactions above threshold"
    
    # Test with different threshold
    high_value_500 = analyzer.filter_high_value_transactions(500.0)
    assert len(high_value_500) < len(high_value), \
        "Higher threshold should return fewer results"
    
    print("✓ High-value filtering works correctly")


@pytest.mark.filtering
def test_filter_by_category(analyzer):
    """Test filtering by product category."""
    print("\n=== Test: Filter By Category ===")
    
    category = 'Electronics'
    filtered = analyzer.filter_by_category(category)
    
    print(f"{category} Transactions: {len(filtered)}")
    
    assert all(filtered['product_category'] == category)
    assert len(filtered) > 0
    
    print("✓ Category filtering works correctly")


@pytest.mark.filtering
def test_filter_by_date_range(analyzer):
    """
    Test filtering by date range.
    
    Demonstrates: complex filtering with multiple conditions
    """
    print("\n=== Test: Filter By Date Range ===")
    
    start_date = '2024-02-01'
    end_date = '2024-02-29'
    
    filtered = analyzer.filter_by_date_range(start_date, end_date)
    
    print(f"Transactions from {start_date} to {end_date}: {len(filtered)}")
    
    # Convert to datetime for comparison
    filtered_dates = pd.to_datetime(filtered['date'])
    assert all(filtered_dates >= pd.to_datetime(start_date))
    assert all(filtered_dates <= pd.to_datetime(end_date))
    assert len(filtered) > 0
    
    print("✓ Date range filtering works correctly")


# ==================== COMPLEX MULTI-STEP OPERATIONS ====================

@pytest.mark.complex
def test_top_n_products_by_revenue(analyzer):
    """
    Test multi-step product ranking operation.
    
    Demonstrates: map → groupby → sort → slice pipeline
    """
    print("\n=== Test: Top N Products By Revenue ===")
    
    n = 5
    top_products = analyzer.get_top_n_products_by_revenue(n)
    
    print(f"Top {n} Products by Revenue:")
    for i, (product, revenue) in enumerate(top_products, 1):
        print(f"  {i}. {product}: ${revenue:,.2f}")
    
    # Should return exactly n products (or less if not enough data)
    assert len(top_products) <= n
    assert len(top_products) > 0
    
    # Should be sorted in descending order
    revenues = [rev for _, rev in top_products]
    assert revenues == sorted(revenues, reverse=True), "Should be sorted by revenue"
    
    # All revenues should be positive
    assert all(rev > 0 for _, rev in top_products)
    
    print("✓ Top products ranking works correctly")


@pytest.mark.complex
def test_top_n_customers_by_spending(analyzer):
    """
    Test customer ranking by total spending.
    
    Demonstrates: customer analytics with functional approach
    """
    print("\n=== Test: Top N Customers By Spending ===")
    
    n = 5
    top_customers = analyzer.get_top_n_customers_by_spending(n)
    
    print(f"Top {n} Customers by Spending:")
    for i, (customer, spending) in enumerate(top_customers, 1):
        print(f"  {i}. {customer}: ${spending:,.2f}")
    
    assert len(top_customers) <= n
    assert len(top_customers) > 0
    
    # Should be sorted
    spending_values = [spend for _, spend in top_customers]
    assert spending_values == sorted(spending_values, reverse=True)
    
    print("✓ Top customers ranking works correctly")


@pytest.mark.complex
def test_category_performance_analysis(analyzer):
    """
    Test comprehensive category analysis.
    
    Demonstrates: complex multi-metric aggregation
    """
    print("\n=== Test: Category Performance Analysis ===")
    
    performance = analyzer.analyze_category_performance()
    
    print("Category Performance Metrics:")
    print(performance)
    
    # Should have multiple categories
    assert len(performance) >= 4  # At least 4 categories
    
    # Should have expected columns
    assert 'total_amount' in performance.columns
    assert 'quantity' in performance.columns
    
    print("✓ Category performance analysis works correctly")


@pytest.mark.complex
def test_monthly_revenue(analyzer):
    """
    Test temporal aggregation by month.
    
    Demonstrates: time-series grouping
    """
    print("\n=== Test: Monthly Revenue ===")
    
    monthly = analyzer.calculate_monthly_revenue()
    
    print("Monthly Revenue:")
    for month, revenue in sorted(monthly.items()):
        print(f"  {month}: ${revenue:,.2f}")
    
    assert len(monthly) > 0
    assert all(v > 0 for v in monthly.values())
    
    print("✓ Monthly revenue calculation works correctly")


@pytest.mark.complex
def test_regional_best_sellers(analyzer):
    """
    Test finding best-selling product per region.
    
    Demonstrates: nested grouping and max finding
    """
    print("\n=== Test: Regional Best Sellers ===")
    
    best_sellers = analyzer.get_regional_best_sellers()
    
    print("Best-Selling Products by Region:")
    for region, product in sorted(best_sellers.items()):
        print(f"  {region}: {product}")
    
    # Should have entry for each region
    assert len(best_sellers) == 4  # North, South, East, West
    assert all(isinstance(product, str) for product in best_sellers.values())
    
    print("✓ Regional best sellers analysis works correctly")


# ==================== FUNCTIONAL UTILITY TESTS ====================

@pytest.mark.advanced
def test_custom_aggregation(analyzer):
    """
    Test generic functional aggregation with custom function.
    
    Demonstrates: higher-order functions
    """
    print("\n=== Test: Custom Aggregation ===")
    
    # Test with max function
    max_by_category = analyzer.apply_custom_aggregation(
        'product_category',
        'total_amount',
        lambda x: x.max()
    )
    
    print("Max Transaction by Category:")
    for category, max_val in max_by_category.items():
        print(f"  {category}: ${max_val:.2f}")
    
    assert len(max_by_category) > 0
    assert all(v > 0 for v in max_by_category.values())
    
    print("✓ Custom aggregation with higher-order function works")


@pytest.mark.advanced
def test_chain_operations(analyzer):
    """
    Test function composition and chaining.
    
    Demonstrates: function composition, higher-order functions
    """
    print("\n=== Test: Chain Operations ===")
    
    # Chain: filter Electronics → calculate sum
    result = analyzer.chain_operations(
        filter_func=lambda df: df[df['product_category'] == 'Electronics'],
        aggregate_func=lambda df: df['total_amount'].sum()
    )
    
    print(f"Total Electronics Revenue: ${result:,.2f}")
    
    assert result > 0
    
    # Verify it matches direct calculation
    electronics = analyzer.filter_by_category('Electronics')
    expected = electronics['total_amount'].sum()
    assert abs(result - expected) < 0.01
    
    print("✓ Operation chaining works correctly")


# ==================== SUMMARY STATISTICS TEST ====================

@pytest.mark.basic
def test_summary_statistics(analyzer):
    """
    Test comprehensive summary statistics.
    
    Demonstrates: multiple aggregations in one operation
    """
    print("\n=== Test: Summary Statistics ===")
    
    summary = analyzer.get_summary_statistics()
    
    print("Sales Summary:")
    print(f"  Total Revenue: ${summary['total_revenue']:,.2f}")
    print(f"  Avg Transaction: ${summary['avg_transaction']:.2f}")
    print(f"  Transaction Count: {summary['transaction_count']}")
    print(f"  Unique Customers: {summary['unique_customers']}")
    print(f"  Unique Products: {summary['unique_products']}")
    print(f"  Date Range: {summary['date_range']['start']} to {summary['date_range']['end']}")
    
    # Validate summary
    assert summary['total_revenue'] > 0
    assert summary['avg_transaction'] > 0
    assert summary['transaction_count'] == 50
    assert summary['unique_customers'] > 0
    assert summary['unique_products'] > 0
    
    print("✓ Summary statistics generated correctly")


# ==================== EDGE CASES ====================

@pytest.mark.edge_case
def test_empty_filter_result(analyzer):
    """
    Test handling of filter that returns no results.
    
    Demonstrates: edge case handling
    """
    print("\n=== Test: Empty Filter Result ===")
    
    # Filter for impossibly high value
    result = analyzer.filter_high_value_transactions(999999.0)
    
    print(f"Transactions above $999,999: {len(result)}")
    
    assert len(result) == 0
    assert isinstance(result, pd.DataFrame)
    
    print("✓ Empty filter result handled correctly")


@pytest.mark.edge_case
def test_nonexistent_region_filter(analyzer):
    """Test filtering by non-existent region."""
    print("\n=== Test: Non-existent Region Filter ===")
    
    result = analyzer.filter_by_region('Antarctica')
    
    print(f"Transactions in Antarctica: {len(result)}")
    
    assert len(result) == 0
    assert isinstance(result, pd.DataFrame)
    
    print("✓ Non-existent region filter handled correctly")


@pytest.mark.edge_case
def test_data_immutability(analyzer):
    """
    Test that operations don't modify original data.
    
    Demonstrates: immutability principle
    """
    print("\n=== Test: Data Immutability ===")
    
    original = analyzer.load_data()
    original_len = len(original)
    original_sum = original['total_amount'].sum()
    
    # Perform various operations
    analyzer.filter_high_value_transactions(100)
    analyzer.filter_by_region('North')
    analyzer.get_top_n_products_by_revenue(5)
    
    # Check original data unchanged
    current = analyzer.load_data()
    assert len(current) == original_len
    assert abs(current['total_amount'].sum() - original_sum) < 0.01
    
    print("✓ Original data remains immutable after operations")