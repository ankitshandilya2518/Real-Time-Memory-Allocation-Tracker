'''
class MemoryManager:
    def __init__(self, total_pages=256, page_size=4):
        self.total_pages = total_pages
        self.page_size = page_size
        self.pages = [0] * total_pages  # 0 = free, 1 = allocated
        self.page_table = {}  # Maps process ID to allocated pages
        self.segment_table = {}  # Maps process ID to (base, limit) segments

    def allocate_paging(self, process_id, num_pages):
        """Allocates pages for a process"""
        allocated_pages = []
        for i in range(len(self.pages) - num_pages + 1):
            if all(p == 0 for p in self.pages[i:i+num_pages]):
                for j in range(num_pages):
                    self.pages[i+j] = 1
                self.page_table[process_id] = list(range(i, i+num_pages))
                return i  # Return start index
        return -1  # No space available

    def allocate_segmentation(self, process_id, size):
        """Allocates memory for a process using segmentation"""
        for i in range(len(self.pages) - size + 1):
            if all(p == 0 for p in self.pages[i:i+size]):
                self.segment_table[process_id] = (i, size)
                for j in range(size):
                    self.pages[i+j] = 1
                return i  # Return base address
        return -1  # No space available

    def deallocate(self, process_id):
        """Frees memory allocated to a process"""
        if process_id in self.page_table:
            for page in self.page_table.pop(process_id):
                self.pages[page] = 0
        elif process_id in self.segment_table:
            base, size = self.segment_table.pop(process_id)
            for i in range(size):
                self.pages[base + i] = 0
'''
'''
class MemoryManager:
    def __init__(self, total_pages=256, page_size=4):
        self.total_pages = total_pages
        self.page_size = page_size
        self.pages = [None] * total_pages  # None = free, process ID when allocated
        self.processes = {}  # Stores process details: {process_id: (allocated_pages)}

    def allocate_memory(self, process_id, num_pages):
        """Allocates memory and assigns it to a process."""
        free_blocks = [i for i, p in enumerate(self.pages) if p is None]
        if len(free_blocks) < num_pages:
            print(f"❌ Not enough memory to allocate {num_pages} pages to Process {process_id}!")
            return "Error: Not enough memory!"

        allocated_pages = free_blocks[:num_pages]
        for page in allocated_pages:
            self.pages[page] = process_id
        self.processes[process_id] = allocated_pages

        print(f"✅ Allocated {num_pages} pages to Process {process_id}. Pages: {allocated_pages}")
        return allocated_pages

    def deallocate_memory(self, process_id):
        """Frees memory used by a process."""
        if process_id in self.processes:
            for page in self.processes.pop(process_id):
                self.pages[page] = None
            print(f"🔄 Deallocated memory for Process {process_id}.")
        else:
            print(f"⚠ Error: Process {process_id} not found!")

    def compact_memory(self):
        """Rearranges memory to reduce fragmentation."""
        allocated = [p for p in self.pages if p is not None]
        self.pages = allocated + [None] * (self.total_pages - len(allocated))
        print(f"🛠 Memory Compaction Completed!")
'''
class MemoryManager:
    def __init__(self, total_pages=256):
        self.total_pages = total_pages
        self.pages = [None] * total_pages  # None = free, otherwise process ID
        self.processes = {}

    def allocate_memory(self, process_id, num_pages):
        """Allocates memory and returns a success message."""
        free_blocks = [i for i, p in enumerate(self.pages) if p is None]
        if len(free_blocks) < num_pages:
            return f"❌ Not enough memory for {num_pages} pages!"

        allocated_pages = free_blocks[:num_pages]
        for page in allocated_pages:
            self.pages[page] = process_id
        self.processes[process_id] = allocated_pages

        return f"✅ Process {process_id} allocated {num_pages} pages!"

    def deallocate_memory(self, process_id):
        """Frees memory and returns a success message."""
        if process_id in self.processes:
            for page in self.processes.pop(process_id):
                self.pages[page] = None
            return f"🔄 Process {process_id} memory deallocated!"
        return f"⚠ Error: Process {process_id} not found!"

    def get_memory_state(self):
        """Returns a user-friendly view of memory state."""
        return [p if p is not None else "Free" for p in self.pages]
