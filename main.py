class MemoryBlock:
    def _init_(self, blockID, size, status, location, rank):
        self.blockID = blockID
        self.size = size
        self.status = status
        self.location = location
        self.rank = rank
        self.distance = None

    def _repr_(self):
        return f"MemoryBlock(blockID={self.blockID}, size={self.size}, status={self.status}, location={self.location}, rank={self.rank})"

# Initialize memory blocks
memoryBlocks = [
    MemoryBlock(1, 1024, "deallocated", "0x1000", 3),
    MemoryBlock(2, 512, "allocated", "0x2000", 5),
    MemoryBlock(3, 2048, "deallocated", "0x3000", 2),
    MemoryBlock(4, 256, "allocated", "0x4000", 6),
    MemoryBlock(5, 4096, "deallocated", "0x5000", 1)
]

# Function to cache memory table
def cache_memory_table(memory_table):
    print("Memory table cached for quick access.")
    # Implement a real caching mechanism here if needed

# Function to handle memory allocation request
def allocate_memory(requested_size):
    print(f"Requesting allocation for size: {requested_size}")

    # Step 1: Filter deallocated blocks
    available_blocks = [block for block in memoryBlocks if block.status == "deallocated"]

    # Step 2: Calculate distance based on size
    for block in available_blocks:
        block.distance = abs(block.size - requested_size)

    # Step 3: Sort blocks based on proximity to requested size
    available_blocks.sort(key=lambda x: x.distance)

    # Step 4: Allocate memory if available
    if available_blocks:
        selected_block = available_blocks[0]
        if selected_block.size >= requested_size:
            selected_block.status = "allocated"
            selected_block.size -= requested_size  # Update size of selected block
            print(f"Allocated memory at location: {selected_block.location}")
        else:
            print("No block large enough for requested allocation.")
    else:
        print("No available memory block for allocation.")

    # Step 6: Cache management
    cache_memory_table(available_blocks)

# Main execution loop
while True:
    try:
        requested_size = int(input("Enter size to allocate (or -1 to exit): "))
        if requested_size == -1:  # Exit condition
            print("\nExiting allocation process.")
            break
        allocate_memory(requested_size)
    except ValueError:
        print("Please enter a valid integer size.")
    except KeyboardInterrupt:
        print("\nExiting program.")
        break

# Display updated memory block list
print("\nFinal Memory Block Status:")
for block in memoryBlocks:
    print(block)
