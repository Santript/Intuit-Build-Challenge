# Intuit Build Challenge

This repository contains solutions for the Intuit Build Challenge, demonstrating proficiency in concurrent programming, functional programming, data analysis, and comprehensive testing practices.

## 📁 Repository Structure

```
Intuit-Build-Challenge/
├── Assignment-1/          Producer-Consumer Pattern with Thread Synchronization
│   ├── producer_consumer.py
│   ├── test_producer_consumer.py (5 tests)
│   ├── pytest.ini
│   ├── requirements.txt
│   └── README.md
│
├── Assignment-2/          Sales Data Analysis with Functional Programming
│   ├── sales_analyzer.py
│   ├── sales_data.csv (50 rows)
│   ├── test_sales_analyzer.py (21 tests)
│   ├── pytest.ini
│   ├── requirements.txt
│   └── README.md
│
└── README.md             (this file)
```

---

## 🎯 Assignment 1: Producer-Consumer Pattern

**Objective:** Implement a classic producer-consumer pattern demonstrating thread synchronization and communication.

### Key Features
- ✅ Thread synchronization using Python's `queue.Queue`
- ✅ Concurrent programming with producer and consumer threads
- ✅ Blocking queue behavior with configurable size limits
- ✅ Wait/notify mechanism for thread communication
- ✅ Sentinel value pattern for clean thread termination

### Testing
- 5 comprehensive test scenarios
- Tests for: basic synchronization, empty source, blocking queue, large datasets, mixed data types
- 80+ print statements for detailed console output
- Custom pytest markers for test organization

### Quick Start
```bash
cd Assignment-1
pip install -r requirements.txt
pytest test_producer_consumer.py -v -s
```

**[📖 Full Documentation →](Assignment-1/README.md)**

---

## 🎯 Assignment 2: Sales Data Analysis with Functional Programming

**Objective:** Perform data analysis on CSV sales data using functional programming paradigms, demonstrating stream operations, data aggregation, and lambda expressions.

### Key Features
- ✅ Functional programming (pure functions, immutability, higher-order functions)
- ✅ Stream operations (map, filter, reduce patterns using pandas)
- ✅ Data aggregation (groupby, sum, mean, count, multi-metric)
- ✅ Lambda expressions throughout (filtering, mapping, sorting)
- ✅ 50-row CSV dataset with realistic business data
- ✅ 19 analytical methods covering various operations

### Testing
- 21 comprehensive tests across 6 categories
- Test categories: basic, grouping, filtering, complex, advanced, edge_case
- 86+ print statements for detailed analysis output
- Complete coverage of all analytical methods

### Dataset
- 50 sales transactions (Jan-Mar 2024)
- 4 product categories (Electronics, Clothing, Food, Books)
- 4 regions (North, South, East, West)
- 40 unique customers, 43 unique products
- Total revenue: ~$10,000

### Quick Start
```bash
cd Assignment-2
pip install -r requirements.txt
pytest test_sales_analyzer.py -v -s
```

**[📖 Full Documentation →](Assignment-2/README.md)**

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

**Clone the repository:**
```bash
git clone https://github.com/Santript/Intuit-Build-Challenge.git
cd Intuit-Build-Challenge
```

**For Assignment 1:**
```bash
cd Assignment-1

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies and run tests
pip install -r requirements.txt
pytest test_producer_consumer.py -v -s
```

**For Assignment 2:**
```bash
cd Assignment-2

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies and run tests
pip install -r requirements.txt
pytest test_sales_analyzer.py -v -s
```

---

## 🧪 Testing

Both assignments include comprehensive test suites using pytest.

### Run All Tests (Both Assignments)
```bash
# From Assignment-1
cd Assignment-1 && pytest test_producer_consumer.py -v -s

# From Assignment-2
cd Assignment-2 && pytest test_sales_analyzer.py -v -s
```

### Test Statistics
- **Total Tests:** 26 (5 + 21)
- **Total Print Statements:** 166+ (80 + 86)
- **Test Coverage:** 100% of implemented methods
- **Custom Markers:** Both assignments use pytest markers for test organization