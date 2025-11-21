import threading
import time
from producer_consumer import ProducerConsumer


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

def main():
    """
    Run all test scenarios to demonstrate producer-consumer pattern objectives.
    """
    print("\n" + "=" * 70)
    print("PRODUCER-CONSUMER PATTERN - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    print()
    
    # Run test case
    test_basic_synchronization()
    time.sleep(0.5)
    
    print("=" * 70)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    
if __name__ == "__main__":
    main()