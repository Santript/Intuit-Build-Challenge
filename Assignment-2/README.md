# Assignment 2: Sales Data Analysis with Functional Programming

## Overview
A comprehensive sales data analysis application demonstrating proficiency with functional programming paradigms, stream operations, data aggregation, and lambda expressions. The program performs various analytical queries on CSV sales data using pandas and pure functional approaches.

## 🎯 Testing Objectives Demonstrated

✅ **Functional Programming**: Pure functions, immutability, higher-order functions  
✅ **Stream Operations**: Map, filter, reduce patterns using pandas  
✅ **Data Aggregation**: Grouping, summing, averaging, counting  
✅ **Lambda Expressions**: Anonymous functions for filtering and transformations  

## 📁 Files

- `sales_data.csv` - 50 rows of realistic sales transaction data
- `sales_analyzer.py` - Main SalesAnalyzer class with functional operations
- `test_sales_analyzer.py` - Comprehensive pytest test suite (20+ tests)
- `pytest.ini` - Pytest configuration with custom markers
- `requirements.txt` - Python dependencies (pandas, pytest)

## 📊 Dataset Structure

The CSV contains 50 sales transactions with the following fields:

| Column | Description | Type |
|--------|-------------|------|
| `transaction_id` | Unique transaction identifier | String |
| `date` | Transaction date (YYYY-MM-DD) | Date |
| `product_category` | Product category | String |
| `product_name` | Specific product name | String |
| `quantity` | Number of items sold | Integer |
| `unit_price` | Price per unit | Float |
| `total_amount` | Total transaction value | Float |
| `region` | Geographic region | String |
| `customer_id` | Customer identifier | String |
| `payment_method` | Payment type | String |

**Categories**: Electronics, Clothing, Food, Books  
**Regions**: North, South, East, West  
**Payment Methods**: Credit Card, Cash, Debit Card, PayPal  
**Date Range**: January - March 2024  
**Total Revenue**: ~$10,000+

### Design Decisions & Assumptions

**Why This Dataset?**
- **Rich Dimensions**: Multiple grouping possibilities (category, region, date, customer)
- **Real-World Scenario**: Business analytics is common use case
- **Varied Data Types**: Numeric, string, date fields for diverse operations
- **Meaningful Analytics**: Supports business intelligence queries

**Assumptions**:
1. All prices in USD
2. Dates in ISO format (YYYY-MM-DD)
3. No missing critical fields (transaction_id, date, amounts)
4. Positive quantities and prices
5. Well-formed CSV structure

## 🚀 Setup

### Install Dependencies

**Option 1: Using pip (recommended)**
```bash
cd Assignment-2
pip install -r requirements.txt
```

**Option 2: Using virtual environment**
```bash
cd Assignment-2
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Option 3: For macOS with externally managed environments**
```bash
pip install --user pandas pytest pytest-html
```

## 🧪 Running Tests

### Run All Tests
```bash
pytest test_sales_analyzer.py -v -s
```

Options:
- `-v` or `--verbose`: Verbose output with test names
- `-s`: Show print statements (important for seeing results)

### Run Specific Test Categories

**Basic aggregation tests:**
```bash
pytest test_sales_analyzer.py -v -s -m basic
```

**Grouping operations:**
```bash
pytest test_sales_analyzer.py -v -s -m grouping
```

**Filtering with predicates:**
```bash
pytest test_sales_analyzer.py -v -s -m filtering
```

**Complex multi-step operations:**
```bash
pytest test_sales_analyzer.py -v -s -m complex
```

**Advanced functional programming:**
```bash
pytest test_sales_analyzer.py -v -s -m advanced
```

**Edge cases:**
```bash
pytest test_sales_analyzer.py -v -s -m edge_case
```

### Run Individual Tests
```bash
pytest test_sales_analyzer.py::test_total_revenue_calculation -v -s
pytest test_sales_analyzer.py::test_group_by_category -v -s
pytest test_sales_analyzer.py::test_top_n_products_by_revenue -v -s
```

### Generate HTML Report
```bash
pytest test_sales_analyzer.py -v -s --html=report.html --self-contained-html
```

## 📝 Test Scenarios

### 1. Basic Aggregation Tests (`@pytest.mark.basic`)

**Test: Total Revenue Calculation**
- Demonstrates: `reduce` operation with lambda
- Validates: Functional sum across all transactions
- Assertion: Matches pandas sum, positive value

**Test: Average Transaction Value**
- Demonstrates: Chaining map and reduce operations
- Validates: Correct average calculation
- Assertion: Matches pandas mean

**Test: Transaction Count**
- Demonstrates: Basic counting
- Validates: Correct dataset size (50 rows)

**Test: Summary Statistics**
- Demonstrates: Multiple aggregations in one operation
- Validates: Comprehensive summary generation
- Returns: Revenue, avg, counts, unique values, date range

### 2. Grouping Operations (`@pytest.mark.grouping`)

**Test: Group By Category**
- Demonstrates: `groupby` with sum aggregation
- Validates: Revenue totals per category
- Assertion: All categories present, positive revenues

**Test: Group By Region**
- Demonstrates: Multi-metric aggregation (sum, mean, count)
- Validates: Comprehensive regional statistics
- Returns: Total revenue, avg transaction, count per region

**Test: Group By Payment Method**
- Demonstrates: Grouping with counting
- Validates: Transaction distribution by payment type
- Assertion: Counts sum to 50

### 3. Filtering Operations (`@pytest.mark.filtering`)

**Test: Filter By Region**
- Demonstrates: Lambda predicate filtering
- Validates: Region-specific extraction
- Assertion: All results match region, data immutability

**Test: Filter High Value Transactions**
- Demonstrates: Numeric threshold filtering
- Validates: Transactions above specified value
- Assertion: All above threshold, proper ordering

**Test: Filter By Category**
- Demonstrates: Categorical filtering
- Validates: Category-specific extraction

**Test: Filter By Date Range**
- Demonstrates: Complex multi-condition filtering
- Validates: Date range extraction
- Assertion: All dates within range

### 4. Complex Multi-Step Operations (`@pytest.mark.complex`)

**Test: Top N Products By Revenue**
- Demonstrates: Map → GroupBy → Sort → Slice pipeline
- Operation Flow: Group products → Sum revenue → Sort descending → Take top 5
- Validates: Correct ranking and ordering
- Assertion: Proper count, descending order

**Test: Top N Customers By Spending**
- Demonstrates: Customer analytics pipeline
- Operation Flow: Group by customer → Sum spending → Rank
- Validates: Customer segmentation

**Test: Category Performance Analysis**
- Demonstrates: Multi-metric aggregation
- Returns: Sum, mean, count per category
- Validates: Comprehensive performance metrics

**Test: Monthly Revenue**
- Demonstrates: Temporal aggregation
- Operation Flow: Extract month → Group → Sum
- Validates: Time-series analysis

**Test: Regional Best Sellers**
- Demonstrates: Nested grouping with max finding
- Operation Flow: Group by region+product → Find max per region
- Validates: Correct best-seller identification

### 5. Advanced Functional Programming (`@pytest.mark.advanced`)

**Test: Custom Aggregation**
- Demonstrates: **Higher-order functions** (functions as parameters)
- Accepts custom aggregation function
- Shows functional abstraction and reusability

**Test: Chain Operations**
- Demonstrates: **Function composition**
- Chains filter → aggregate operations
- Validates composability of pure functions

### 6. Edge Cases (`@pytest.mark.edge_case`)

**Test: Empty Filter Result**
- Validates: Graceful handling of no matches
- Assertion: Empty DataFrame returned

**Test: Non-existent Region**
- Validates: Robust filtering with invalid inputs

**Test: Data Immutability**
- Demonstrates: **Immutability principle**
- Validates: Original data unchanged after operations
- Critical: Proves functional purity

## 🎓 Functional Programming Concepts Demonstrated

### 1. Pure Functions ✓
All analysis methods are pure:
- No side effects
- Same input → same output
- Don't modify original data
- Easily testable and composable

```python
# Pure function - returns new result, doesn't modify input
def calculate_total_revenue(self) -> float:
    df = self.load_data()  # Get fresh copy
    return reduce(lambda acc, amount: acc + amount, df['total_amount'], 0.0)
```

### 2. Immutability ✓
Original data never modified:
- `load_data()` always returns copy
- All operations return new DataFrames
- Test validates immutability

```python
def load_data(self) -> pd.DataFrame:
    return self._raw_data.copy()  # Always return copy
```

### 3. Lambda Expressions ✓
Anonymous functions throughout:

```python
# Filtering with lambda
df[df.apply(lambda row: row['region'] == region, axis=1)]

# Reducing with lambda
reduce(lambda acc, x: acc + x, amounts, 0.0)

# Sorting with lambda
sorted(items, key=lambda x: x[1], reverse=True)
```

### 4. Higher-Order Functions ✓
Functions accepting/returning functions:

```python
def apply_custom_aggregation(
    self, 
    group_by_column: str,
    aggregate_column: str,
    aggregation_func: Callable  # Function as parameter
) -> Dict[str, Any]:
    result = df.groupby(group_by_column)[aggregate_column].apply(aggregation_func)
    return result.to_dict()
```

### 5. Stream Operations ✓
Chained operations on data streams:

```python
# Map → Filter → Reduce pipeline
(df.groupby('product_name')['total_amount']
   .sum()                          # Aggregate (reduce)
   .sort_values(ascending=False)   # Transform (map)
   .head(n))                        # Filter
```

### 6. Function Composition ✓
Composing functions for complex operations:

```python
def chain_operations(
    self,
    filter_func: Callable,
    aggregate_func: Callable
) -> Any:
    df = self.load_data()
    filtered = filter_func(df)      # Apply first function
    return aggregate_func(filtered)  # Apply second function
```

## 🔧 Implementation Details

### SalesAnalyzer Class Architecture

**Core Methods Categories**:

1. **Data Loading**
   - `load_data()`: Lazy loading with immutability
   - `get_raw_data()`: Safe data access

2. **Aggregation Operations**
   - `calculate_total_revenue()`: Functional reduce
   - `calculate_average_transaction_value()`: Map + reduce
   - `get_transaction_count()`: Simple count

3. **Grouping Operations**
   - `group_by_category()`: Single-metric grouping
   - `group_by_region()`: Multi-metric grouping
   - `group_by_payment_method()`: Counting groups

4. **Filtering Operations**
   - `filter_by_region()`: Lambda predicate
   - `filter_high_value_transactions()`: Numeric predicate
   - `filter_by_category()`: Categorical filter
   - `filter_by_date_range()`: Multi-condition filter

5. **Complex Operations**
   - `get_top_n_products_by_revenue()`: Ranking pipeline
   - `get_top_n_customers_by_spending()`: Customer analytics
   - `analyze_category_performance()`: Multi-metric analysis
   - `calculate_monthly_revenue()`: Temporal aggregation
   - `get_regional_best_sellers()`: Nested grouping

6. **Functional Utilities**
   - `apply_custom_aggregation()`: Generic higher-order function
   - `chain_operations()`: Function composition
   - `get_summary_statistics()`: Comprehensive stats

## 📈 Analytical Queries Implemented

| Query | Input | Output | Functional Concept |
|-------|-------|--------|-------------------|
| Total Revenue | - | Float | Reduce |
| Average Transaction | - | Float | Map + Reduce |
| Category Breakdown | - | Dict[str, float] | GroupBy + Sum |
| Regional Stats | - | Dict[str, Dict] | GroupBy + Multiple Agg |
| High Value Filter | threshold | DataFrame | Filter with Lambda |
| Top N Products | n | List[Tuple] | Map→Group→Sort→Slice |
| Top N Customers | n | List[Tuple] | Group→Sort→Slice |
| Monthly Revenue | - | Dict[str, float] | Temporal GroupBy |
| Best Sellers by Region | - | Dict[str, str] | Nested GroupBy + Max |
| Custom Aggregation | func | Dict | Higher-Order Function |
| Chained Operations | 2 funcs | Any | Function Composition |

## 🎯 Usage Examples

### Basic Usage

```python
from sales_analyzer import SalesAnalyzer

# Initialize analyzer
analyzer = SalesAnalyzer('sales_data.csv')

# Calculate total revenue
total = analyzer.calculate_total_revenue()
print(f"Total Revenue: ${total:,.2f}")

# Get category breakdown
categories = analyzer.group_by_category()
for category, revenue in categories.items():
    print(f"{category}: ${revenue:,.2f}")

# Find top products
top_products = analyzer.get_top_n_products_by_revenue(5)
for product, revenue in top_products:
    print(f"{product}: ${revenue:,.2f}")
```

### Advanced Functional Usage

```python
# Custom aggregation with lambda
max_by_region = analyzer.apply_custom_aggregation(
    'region',
    'total_amount',
    lambda x: x.max()
)

# Chain operations functionally
electronics_revenue = analyzer.chain_operations(
    filter_func=lambda df: df[df['product_category'] == 'Electronics'],
    aggregate_func=lambda df: df['total_amount'].sum()
)

# Complex filtering and aggregation
high_value_electronics = (
    analyzer.filter_by_category('Electronics')
    .pipe(lambda df: df[df['total_amount'] > 100])
    ['total_amount'].sum()
)
```

## 📊 Expected Test Output

When running all tests, you should see:

```
========================= test session starts ==========================
test_sales_analyzer.py::test_total_revenue_calculation PASSED
test_sales_analyzer.py::test_average_transaction_value PASSED
test_sales_analyzer.py::test_transaction_count PASSED
test_sales_analyzer.py::test_group_by_category PASSED
test_sales_analyzer.py::test_group_by_region PASSED
test_sales_analyzer.py::test_group_by_payment_method PASSED
test_sales_analyzer.py::test_filter_by_region PASSED
test_sales_analyzer.py::test_filter_high_value_transactions PASSED
test_sales_analyzer.py::test_filter_by_category PASSED
test_sales_analyzer.py::test_filter_by_date_range PASSED
test_sales_analyzer.py::test_top_n_products_by_revenue PASSED
test_sales_analyzer.py::test_top_n_customers_by_spending PASSED
test_sales_analyzer.py::test_category_performance_analysis PASSED
test_sales_analyzer.py::test_monthly_revenue PASSED
test_sales_analyzer.py::test_regional_best_sellers PASSED
test_sales_analyzer.py::test_custom_aggregation PASSED
test_sales_analyzer.py::test_chain_operations PASSED
test_sales_analyzer.py::test_summary_statistics PASSED
test_sales_analyzer.py::test_empty_filter_result PASSED
test_sales_analyzer.py::test_nonexistent_region_filter PASSED
test_sales_analyzer.py::test_data_immutability PASSED

======================== 21 passed in 2.34s ===========================
```

## 🎨 Why Functional Programming?

### Benefits Demonstrated

1. **Testability**: Pure functions easy to unit test
2. **Composability**: Functions can be combined for complex operations
3. **Readability**: Declarative style (what, not how)
4. **Immutability**: No unexpected side effects
5. **Parallelization**: Pure functions can be parallelized
6. **Maintainability**: Changes don't affect other parts

### Comparison: Imperative vs Functional

**Imperative Approach** (Not used):
```python
total = 0
for transaction in transactions:
    total += transaction['amount']  # Mutation!
```

**Functional Approach** (Used):
```python
total = reduce(lambda acc, x: acc + x, df['amount'], 0.0)
```

## 🏆 Testing Best Practices

Following patterns from Assignment 1:

✓ **Comprehensive Coverage**: 21 tests across 6 categories  
✓ **Custom Markers**: Organized test categories  
✓ **Clear Assertions**: Validates expected behavior  
✓ **Edge Cases**: Tests error conditions  
✓ **Print Statements**: Verbose output with `-s` flag  
✓ **Fixtures**: Reusable test components  
✓ **Documentation**: Each test explains what it demonstrates  

## 🔍 Pytest Markers

Custom markers for test organization:

- `basic` - Basic aggregation and counting tests
- `grouping` - Grouping operations tests
- `filtering` - Filtering with predicates
- `complex` - Multi-step analysis operations
- `advanced` - Higher-order functions, composition
- `edge_case` - Edge case handling

## 🐛 Troubleshooting

**Tests not showing output?**
```bash
pytest test_sales_analyzer.py -v -s  # Use -s flag
```

**Want to see available tests?**
```bash
pytest test_sales_analyzer.py --collect-only
```

**Want to see all markers?**
```bash
pytest --markers
```

**Import errors?**
```bash
pip install -r requirements.txt
```

## 📚 Key Learnings

This assignment demonstrates:

1. **Functional Paradigms**: Map, filter, reduce patterns
2. **Stream Processing**: Pandas as stream operations
3. **Lambda Expressions**: Anonymous functions throughout
4. **Higher-Order Functions**: Functions accepting functions
5. **Immutability**: Pure functional programming
6. **Function Composition**: Building complex from simple
7. **Data Aggregation**: Multiple grouping strategies
8. **Test-Driven Development**: Comprehensive test coverage

## 🎓 Conclusion

This implementation showcases proficiency in:
- ✅ Functional programming paradigms
- ✅ Stream operations (pandas as functional API)
- ✅ Data aggregation (groupby, agg, apply)
- ✅ Lambda expressions (filtering, mapping, reducing)
- ✅ Comprehensive testing with pytest
- ✅ Clean code and documentation

The solution prioritizes **functional purity**, **immutability**, and **composability** while solving real-world data analysis problems using Python's functional capabilities combined with pandas' powerful stream-like operations.