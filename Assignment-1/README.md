# Assignment 1: Producer-Consumer Pattern

## Overview
Implementation of a classic producer-consumer pattern demonstrating thread synchronization and communication using Python. Includes comprehensive pytest test suite with multiple scenarios.

## Files
- `producer_consumer.py` - Main implementation of the ProducerConsumer class
- `test_producer_consumer.py` - Pytest test suite with 5 different test scenarios
- `pytest.ini` - Pytest configuration with custom markers
- `requirements.txt` - Python dependencies

## Setup

### Install Dependencies

**Option 1: Using pip (recommended)**
```bash
pip install -r requirements.txt
```

**Option 2: Install pytest only**
```bash
pip install pytest
```

**Option 3: For macOS with externally managed environments**
```bash
# Install with user flag
pip install --user pytest

# Or use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Option 4: Using system packages**
```bash
# macOS with Homebrew
brew install python
pip3 install --break-system-packages pytest
```

## Running Tests

### Run All Tests
```bash
pytest test_producer_consumer.py -v -s
```

Options:
- `-v` or `--verbose`: Verbose output with test names
- `-s`: Show print statements (important for seeing thread execution)

### Run Specific Test Categories

Run only basic tests:
```bash
pytest test_producer_consumer.py -v -s -m basic
```

Run only blocking queue tests:
```bash
pytest test_producer_consumer.py -v -s -m blocking
```

Skip slow tests:
```bash
pytest test_producer_consumer.py -v -s -m "not slow"
```

### Run Individual Tests
```bash
pytest test_producer_consumer.py::test_basic_synchronization -v -s
pytest test_producer_consumer.py::test_blocking_queue -v -s
```

### Generate HTML Report
```bash
pytest test_producer_consumer.py -v -s --html=report.html --self-contained-html
```

## Test Scenarios

### Test 1: Basic Thread Synchronization (`@pytest.mark.basic`)
- **Source**: 10 items (numbers 1-10)
- **Demonstrates**: Basic thread-safe operations
- **Shows**: Concurrent data transfer
- **Assertions**: Verifies all items transferred in correct order

### Test 2: Empty Source Container (`@pytest.mark.edge_case`)
- **Source**: Empty list
- **Demonstrates**: Proper handling of edge cases
- **Shows**: Sentinel value mechanism works with no data
- **Assertions**: Verifies empty source handled gracefully

### Test 3: Blocking Queue Behavior (`@pytest.mark.blocking`, `@pytest.mark.slow`)
- **Source**: 15 items with max queue size of 3
- **Demonstrates**: Producer blocking when queue is full
- **Shows**: Wait/notify mechanism in action
- **Key Feature**: Fast producer (0.05s) vs slow consumer (0.5s) creates visible blocking
- **Assertions**: Verifies all items transferred despite blocking

### Test 4: Large Dataset Concurrent Transfer (`@pytest.mark.performance`, `@pytest.mark.slow`)
- **Source**: 50 items
- **Demonstrates**: Performance with larger datasets
- **Shows**: Efficiency of concurrent programming
- **Assertions**: Verifies all items transferred and measures execution time

### Test 5: Mixed Data Types (`@pytest.mark.data_types`)
- **Source**: Various types (int, string, float, dict, list, bool)
- **Demonstrates**: Queue handles any Python object
- **Shows**: Robustness of implementation
- **Assertions**: Verifies each data type preserved correctly

## Pytest Markers

Custom markers defined in `pytest.ini`:
- `basic` - Basic thread synchronization tests
- `edge_case` - Edge case handling tests
- `blocking` - Tests demonstrating blocking queue behavior
- `performance` - Performance and scalability tests
- `data_types` - Tests with various data types
- `slow` - Tests that take longer to run (>5 seconds)

## Implementation Details

### ProducerConsumer Class

**Constructor:**
```python
ProducerConsumer(source_container, max_queue_size=0)
```
- `source_container`: List of items to be produced
- `max_queue_size`: Maximum queue size (0 = unlimited)

**Methods:**
- `producer()`: Reads from source container and adds to queue, then sends sentinel value
- `consumer()`: Consumes from queue and stores in destination until sentinel received
- `get_destination()`: Returns the destination container with all consumed items

### Data Flow
```
Source Container → Producer Thread → Shared Queue → Consumer Thread → Destination Container
```

### Key Concepts Demonstrated

#### 1. Thread Synchronization ✓
- All queue operations are thread-safe
- No race conditions or data corruption
- Verified with pytest assertions

#### 2. Concurrent Programming ✓
- Producer and consumer run simultaneously
- Visible interleaving of operations in output
- Both threads execute independently

#### 3. Blocking Queues ✓
- **Test 3 specifically demonstrates blocking**
- Producer blocks when queue is full
- Consumer blocks when queue is empty
- Automatic wait mechanism built into `queue.Queue`

#### 4. Wait/Notify Mechanism ✓
- Python's `queue.Queue` uses condition variables internally
- `put()` notifies waiting consumers
- `get()` notifies waiting producers
- **Test 3 shows this clearly** with visible blocking messages

## Example Output

When you run the tests, you'll see:
```
test_producer_consumer.py::test_basic_synchronization PASSED
test_producer_consumer.py::test_empty_source PASSED
test_producer_consumer.py::test_blocking_queue PASSED
test_producer_consumer.py::test_large_dataset PASSED
test_producer_consumer.py::test_mixed_data_types PASSED

========================= 5 passed in 15.23s =========================
```

## Custom Usage

You can also use the ProducerConsumer class directly:

```python
from producer_consumer import ProducerConsumer
import threading

# Create with custom source
source = ["apple", "banana", "cherry"]
pc = ProducerConsumer(source, max_queue_size=2)

# Run threads
producer = threading.Thread(target=pc.producer)
consumer = threading.Thread(target=pc.consumer)

producer.start()
consumer.start()

producer.join()
consumer.join()

# Get results
print(pc.get_destination())  # ['apple', 'banana', 'cherry']
```

## Troubleshooting

**Tests running but not showing output?**
- Make sure to use `-s` flag: `pytest test_producer_consumer.py -v -s`

**Want to see which tests are available?**
```bash
pytest test_producer_consumer.py --collect-only
```

**Want to see all markers?**
```bash
pytest --markers
```

