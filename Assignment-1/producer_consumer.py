import queue
import time


class ProducerConsumer:
    """
    A simple producer-consumer pattern implementation using a shared queue
    with thread synchronization. Data flows from source -> queue -> destination.
    """
    
    def __init__(self, source_container, max_queue_size=0):
        """
        Initialize the ProducerConsumer with a source container.
        
        Args:
            source_container: List of items to be produced
            max_queue_size: Maximum size of the queue (0 = unlimited)
        """
        self.source_container = source_container
        self.shared_queue = queue.Queue(maxsize=max_queue_size)
        self.destination_container = []
    
    def producer(self):
        """
        Producer thread that reads from the source container and places items
        into the shared queue, then adds None as a sentinel value to signal completion.
        """
        print("Producer: Starting to produce items...")
        print(f"Producer: Source container has {len(self.source_container)} items")
        
        for item in self.source_container:
            self.shared_queue.put(item)
            print(f"Producer: Added {item} to queue")
            # Simulate some work
            time.sleep(0.1)
        
        # Add sentinel value to signal end
        self.shared_queue.put(None)
        print("Producer: Finished producing. Sent sentinel value.")
    
    def consumer(self):
        """
        Consumer thread that reads from the queue and stores items in the
        destination container until it receives the sentinel value (None).
        """
        print("Consumer: Starting to consume items...")
        while True:
            item = self.shared_queue.get()
            
            # Check for sentinel value
            if item is None:
                print("Consumer: Received sentinel value. Stopping.")
                break
            
            # Store item in destination container
            self.destination_container.append(item)
            print(f"Consumer: Consumed {item} and stored in destination")
            # Simulate some work
            time.sleep(0.15)
        
        print(f"Consumer: Finished consuming. Destination has {len(self.destination_container)} items.")