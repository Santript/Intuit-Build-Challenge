"""
Producer-Consumer Pattern - Pytest Test Suite

Run with: pytest test_producer_consumer.py -v -s
  -v: verbose output
  -s: show print statements
"""

import threading
import time
import queue
import pytest
from producer_consumer import ProducerConsumer


@pytest.mark.basic
def test_basic_synchronization():
    """
    Test 1: Basic Thread Synchronization
    Demonstrates basic concurrent data transfer with thread-safe queue operations.
    Producer reads from source container that contains numbers 1-10 and adds them to the shared queue.
    Consumer reads from the shared queue and adds the items to the destination container.
    """
    print("=" * 70)
    print("TEST 1: BASIC THREAD SYNCHRONIZATION")
    print("=" * 70)
    print("Objective: Demonstrate thread-safe operations with shared queue")
    print()
    
    source = list(range(1, 11))  # Numbers 1-10
    pc = ProducerConsumer(source)
    
    print(f"Initial state:")
    print(f"  Source: {pc.source_container}")
    print(f"  Destination: {pc.destination_container}")
    print()
    
    # Create and start threads
    producer_thread = threading.Thread(target=pc.producer, name="Producer")
    consumer_thread = threading.Thread(target=pc.consumer, name="Consumer")
    
    producer_thread.start()
    consumer_thread.start()
    
    # Wait for completion
    producer_thread.join()
    consumer_thread.join()
    
    print(f"\nFinal state:")
    print(f"  Source: {pc.source_container}")
    print(f"  Destination: {pc.get_destination()}")
    print(f"  ✓ All {len(pc.get_destination())} items transferred successfully!")
    print()
    
    # Pytest assertions
    assert len(pc.get_destination()) == 10, "Should transfer all 10 items"
    assert pc.get_destination() == source, "Destination should match source"
    assert pc.get_destination() == list(range(1, 11)), "Items should be 1-10 in order"


@pytest.mark.edge_case
def test_empty_source():
    """
    Test 2: Empty Source Container
    Demonstrates proper handling when source is empty.
    """
    print("=" * 70)
    print("TEST 2: EMPTY SOURCE CONTAINER")
    print("=" * 70)
    print("Objective: Test synchronization with no items to transfer")
    print()
    
    source = []  # Empty source
    pc = ProducerConsumer(source)
    
    print(f"Initial state:")
    print(f"  Source: {pc.source_container} (empty)")
    print(f"  Destination: {pc.destination_container}")
    print()
    
    producer_thread = threading.Thread(target=pc.producer, name="Producer")
    consumer_thread = threading.Thread(target=pc.consumer, name="Consumer")
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()
    
    print(f"\nFinal state:")
    print(f"  Destination: {pc.get_destination()}")
    print(f"  ✓ Handled empty source correctly!")
    print()
    
    # Pytest assertions
    assert len(pc.get_destination()) == 0, "Destination should be empty"
    assert pc.get_destination() == [], "Should handle empty source gracefully"


@pytest.mark.blocking
@pytest.mark.slow
def test_blocking_queue():
    """
    Test 3: Blocking Queue Behavior
    Demonstrates blocking when queue is full (producer waits) and empty (consumer waits).
    This test uses a slow consumer to clearly show producer blocking.
    """
    print("=" * 70)
    print("TEST 3: BLOCKING QUEUE BEHAVIOR")
    print("=" * 70)
    print("Objective: Demonstrate blocking operations with limited queue size")
    print("Producer is FAST (0.05s), Consumer is SLOW (0.5s)")
    print("Queue fills up quickly, forcing producer to BLOCK and WAIT")
    print()
    
    # Create components for blocking demonstration
    source = list(range(1, 16))  # 15 items
    shared_queue = queue.Queue(maxsize=3)  # Very small queue (max 3 items)
    destination = []
    
    def blocking_producer():
        """Fast producer that will be blocked by full queue."""
        print("Producer: Starting (FAST - 0.05s per item)...")
        for item in source:
            print(f"Producer: Attempting to add {item}...")
            # Check if queue is full before putting
            if shared_queue.full():
                print(f"Producer: ⚠️  QUEUE FULL! Waiting to add {item}... (BLOCKED)")
            shared_queue.put(item)  # This will BLOCK if queue is full
            print(f"Producer: ✓ Added {item} (queue size: ~{shared_queue.qsize()})")
            time.sleep(0.05)  # Fast producer
        
        shared_queue.put(None)  # Sentinel
        print("Producer: Finished. Sent sentinel value.")
    
    def blocking_consumer():
        """Slow consumer that creates backpressure."""
        print("Consumer: Starting (SLOW - 0.5s per item)...")
        time.sleep(0.2)  # Give producer time to fill queue
        
        while True:
            if shared_queue.empty():
                print("Consumer: Queue is empty, waiting for items...")
            
            item = shared_queue.get()  # This will BLOCK if queue is empty
            
            if item is None:
                print("Consumer: Received sentinel. Stopping.")
                break
            
            destination.append(item)
            print(f"Consumer: ✓ Consumed {item} (freeing space in queue)")
            time.sleep(0.5)  # Slow consumer - creates backpressure!
        
        print(f"Consumer: Finished. Processed {len(destination)} items.")
    
    print(f"Initial state:")
    print(f"  Source: {len(source)} items")
    print(f"  Queue max size: 3 (tiny!)")
    print(f"  Destination: {destination}")
    print()
    
    producer_thread = threading.Thread(target=blocking_producer, name="Producer")
    consumer_thread = threading.Thread(target=blocking_consumer, name="Consumer")
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()
    
    print(f"\nFinal state:")
    print(f"  Destination: {len(destination)} items")
    print(f"  ✓ Blocking demonstrated! Producer had to WAIT multiple times!")
    print()
    
    # Pytest assertions
    assert len(destination) == 15, "Should transfer all 15 items"
    assert destination == source, "Destination should match source"
    assert destination == list(range(1, 16)), "Items should be 1-15 in order"


@pytest.mark.performance
@pytest.mark.slow
def test_large_dataset():
    """
    Test 4: Large Dataset Transfer
    Demonstrates concurrent programming efficiency with larger dataset.
    """
    print("=" * 70)
    print("TEST 4: LARGE DATASET CONCURRENT TRANSFER")
    print("=" * 70)
    print("Objective: Demonstrate concurrent programming with larger dataset")
    print()
    
    source = list(range(1, 51))  # 50 items
    pc = ProducerConsumer(source)
    
    print(f"Initial state:")
    print(f"  Source: {len(pc.source_container)} items")
    print(f"  Destination: {pc.destination_container}")
    print()
    
    start_time = time.time()
    
    producer_thread = threading.Thread(target=pc.producer, name="Producer")
    consumer_thread = threading.Thread(target=pc.consumer, name="Consumer")
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()
    
    elapsed_time = time.time() - start_time
    
    print(f"\nFinal state:")
    print(f"  Destination: {len(pc.get_destination())} items")
    print(f"  Time elapsed: {elapsed_time:.2f} seconds")
    print(f"  ✓ Large dataset transferred successfully!")
    print()
    
    # Pytest assertions
    assert len(pc.get_destination()) == 50, "Should transfer all 50 items"
    assert pc.get_destination() == source, "Destination should match source"
    assert elapsed_time > 0, "Should measure execution time"


@pytest.mark.data_types
def test_mixed_data_types():
    """
    Test 5: Mixed Data Types
    Demonstrates queue can handle different data types.
    """
    print("=" * 70)
    print("TEST 5: MIXED DATA TYPES")
    print("=" * 70)
    print("Objective: Verify thread synchronization works with various data types")
    print()
    
    source = [1, "hello", 3.14, {"key": "value"}, [1, 2, 3], True]
    pc = ProducerConsumer(source)
    
    print(f"Initial state:")
    print(f"  Source: {pc.source_container}")
    print(f"  Destination: {pc.destination_container}")
    print()
    
    producer_thread = threading.Thread(target=pc.producer, name="Producer")
    consumer_thread = threading.Thread(target=pc.consumer, name="Consumer")
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()
    
    print(f"\nFinal state:")
    print(f"  Destination: {pc.get_destination()}")
    print(f"  ✓ Mixed data types handled correctly!")
    print()
    
    # Pytest assertions
    assert len(pc.get_destination()) == 6, "Should transfer all 6 items"
    assert pc.get_destination() == source, "Destination should match source exactly"
    assert pc.get_destination()[0] == 1, "First item should be integer"
    assert pc.get_destination()[1] == "hello", "Second item should be string"
    assert pc.get_destination()[2] == 3.14, "Third item should be float"
    assert pc.get_destination()[3] == {"key": "value"}, "Fourth item should be dict"
    assert pc.get_destination()[4] == [1, 2, 3], "Fifth item should be list"
    assert pc.get_destination()[5] is True, "Sixth item should be boolean"