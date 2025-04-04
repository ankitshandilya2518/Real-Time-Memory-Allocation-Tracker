'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visualize_paging(memory_manager):
    """Visualizes paging memory allocation."""
    pages = memory_manager.pages
    plt.bar(range(len(pages)), pages, color=['green' if p == 0 else 'red' for p in pages])
    plt.xlabel("Page Number")
    plt.ylabel("Allocation Status")
    plt.title("Memory Paging Visualization")
    plt.show()

def visualize_segmentation(memory_manager):
    """Visualizes segmentation memory allocation."""
    segments = memory_manager.segment_table
    data = np.zeros((1, len(memory_manager.pages)))  # 1 row, multiple columns
    for _, (base, size) in segments.items():
        data[0, base:base+size] = 1  # Mark allocated segments

    sns.heatmap(data, cmap="coolwarm", cbar=False, xticklabels=False, yticklabels=False)
    plt.title("Memory Segmentation")
    plt.show()
'''
'''
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

def visualize_memory(manager):
    """Visualizes memory allocation dynamically with process IDs."""
    fig, ax = plt.subplots(figsize=(10, 2))

    def update(_):
        ax.clear()
        data = [p if p is not None else -1 for p in manager.pages]  # -1 for free memory
        print(f"🔍 Memory State: {data}")  # Debugging
        sns.heatmap([data], cmap="coolwarm", cbar=False, xticklabels=False, yticklabels=False, ax=ax)
        ax.set_title("Memory Allocation")
        plt.draw()

    ani = animation.FuncAnimation(fig, update, interval=1000)
    plt.show()
'''
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visualize_memory(manager):
    """Displays memory allocation in a separate window."""
    memory_state = manager.get_memory_state()

    # Convert memory state: "None" -> 0, process IDs -> unique numbers
    unique_ids = list(set(p for p in memory_state if p != "Free"))
    id_mapping = {pid: i + 1 for i, pid in enumerate(unique_ids)}

    numeric_memory = [id_mapping.get(p, 0) for p in memory_state]

    plt.figure(figsize=(12, 3))
    data = np.array(numeric_memory).reshape(1, len(numeric_memory))
    ax = sns.heatmap(data, annot=True, fmt="d", cmap="coolwarm", cbar=False, linewidths=0.5)

    ax.set_title("📊 Memory Allocation")
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
'''
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visualize_memory(manager):
    """Displays memory allocation in a separate window with captions."""
    memory_state = manager.get_memory_state()

    # Convert memory state: "Free" -> 0, process IDs -> unique numbers
    unique_ids = list(set(p for p in memory_state if p != "Free"))
    id_mapping = {pid: i + 1 for i, pid in enumerate(unique_ids)}

    numeric_memory = [id_mapping.get(p, 0) for p in memory_state]

    plt.figure(figsize=(12, 3))
    data = np.array(numeric_memory).reshape(1, len(numeric_memory))
    ax = sns.heatmap(data, annot=True, fmt="d", cmap="coolwarm", cbar=False, linewidths=0.5)

    ax.set_title("📊 Memory Allocation Visualization", fontsize=14, fontweight="bold")
    ax.set_xlabel("Memory Blocks", fontsize=12)
    ax.set_ylabel("Allocation Status", fontsize=12)

    # Add labels for Free & Allocated memory
    plt.figtext(0.1, -0.2, "🔵 Free Memory (0)   🔴 Allocated Memory (Process IDs)", fontsize=10, ha="left")

    plt.xticks([])
    plt.yticks([])

    plt.show()

'''
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visualize_memory(manager):
    """Displays memory allocation in a separate window with detailed captions."""
    memory_state = manager.get_memory_state()

    # Unique process IDs mapped to numbers for visualization
    unique_ids = list(set(p for p in memory_state if p != "Free"))
    id_mapping = {pid: i + 1 for i, pid in enumerate(unique_ids)}

    # Convert memory state to numbers (Free -> 0, Processes -> Unique IDs)
    numeric_memory = [id_mapping.get(p, 0) for p in memory_state]

    # Creating labels for blocks
    block_labels = [p if p != "Free" else "🟩 Free" for p in memory_state]

    plt.figure(figsize=(12, 3))
    data = np.array(numeric_memory).reshape(1, len(numeric_memory))
    
    ax = sns.heatmap(data, annot=True, fmt="d", cmap="coolwarm", cbar=False, linewidths=0.5)

    ax.set_title("📊 Memory Allocation & Segmentation", fontsize=14, fontweight="bold")
    ax.set_xlabel("Memory Blocks", fontsize=12)
    ax.set_ylabel("Allocation Status", fontsize=12)

    # Adding labels directly on the heatmap
    for i, label in enumerate(block_labels):
        ax.text(i + 0.5, 0.5, label, ha="center", va="center", fontsize=8, color="white", fontweight="bold")

    # Custom legend for memory status
    plt.figtext(0.1, -0.2, "🟥 Allocated Memory   🟩 Free Memory", fontsize=10, ha="left")

    plt.xticks([])
    plt.yticks([])

    plt.show()
'''
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.patches as mpatches

def visualize_memory(manager):
    """Displays memory allocation in a separate window with process details & legend."""
    memory_state = manager.get_memory_state()

    # Unique process IDs mapped to numbers for visualization
    unique_ids = sorted(set(p for p in memory_state if p != "Free"))
    id_mapping = {pid: i + 1 for i, pid in enumerate(unique_ids)}

    # Convert memory state to numbers (Free -> 0, Processes -> Unique IDs)
    numeric_memory = [id_mapping.get(p, 0) for p in memory_state]

    plt.figure(figsize=(12, 3))
    data = np.array(numeric_memory).reshape(1, len(numeric_memory))
    
    ax = sns.heatmap(data, annot=False, fmt="d", cmap="coolwarm", cbar=False, linewidths=0.5)

    ax.set_title("📊 Memory Allocation & Segmentation", fontsize=14, fontweight="bold")
    ax.set_xlabel("Memory Blocks", fontsize=12)
    ax.set_ylabel("Allocation Status", fontsize=12)

    # Adding labels inside the heatmap for each process
    for i, p in enumerate(memory_state):
        if p != "Free":
            ax.text(i + 0.5, 0.5, p, ha="center", va="center", fontsize=8, color="white", fontweight="bold")

    # Creating a legend for processes
    legend_patches = [mpatches.Patch(color=sns.color_palette("coolwarm", len(unique_ids))[i], label=f"Process {pid}") for i, pid in enumerate(unique_ids)]
    plt.legend(handles=legend_patches, title="Process Legend", loc="upper right", bbox_to_anchor=(1.15, 1))

    # Custom legend for memory status
    plt.figtext(0.1, -0.2, "🟥 Allocated Memory   🟩 Free Memory", fontsize=10, ha="left")

    plt.xticks([])
    plt.yticks([])

    plt.show()
'''
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.patches as mpatches

def visualize_memory(manager):
    """Displays memory allocation with process labels & a properly positioned legend."""
    memory_state = manager.get_memory_state()

    # Unique process IDs mapped to numbers
    unique_ids = sorted(set(p for p in memory_state if p != "Free"))
    id_mapping = {pid: i + 1 for i, pid in enumerate(unique_ids)}

    # Convert memory state to numbers (Free -> 0, Processes -> Unique IDs)
    numeric_memory = [id_mapping.get(p, 0) for p in memory_state]

    plt.figure(figsize=(12, 4))  # Adjusted size for better fit
    data = np.array(numeric_memory).reshape(1, len(numeric_memory))
    
    ax = sns.heatmap(data, annot=False, fmt="d", cmap="coolwarm", cbar=False, linewidths=0.5)

    ax.set_title("📊 Memory Allocation & Segmentation", fontsize=14, fontweight="bold")
    ax.set_xlabel("Memory Blocks", fontsize=12)
    ax.set_ylabel("Allocation Status", fontsize=12)

    # Adding process labels inside heatmap
    for i, p in enumerate(memory_state):
        if p != "Free":
            ax.text(i + 0.5, 0.5, p, ha="center", va="center", fontsize=8, color="white", fontweight="bold")

    # Creating a dynamic legend
    legend_patches = [
        mpatches.Patch(color=sns.color_palette("coolwarm", len(unique_ids))[i], label=f"Process {pid}") 
        for i, pid in enumerate(unique_ids)
    ]

    # Set legend outside the plot
    plt.legend(handles=legend_patches, title="Process Legend", loc="upper center",
               bbox_to_anchor=(0.5, -0.15), ncol=len(unique_ids), fontsize=10, frameon=False)

    plt.xticks([])
    plt.yticks([])

    plt.show()
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.patches as mpatches

def visualize_memory(manager):
    """Displays memory allocation with process labels & a properly positioned legend."""
    memory_state = manager.get_memory_state()

    # Unique process IDs mapped to colors
    unique_ids = sorted(set(p for p in memory_state if p != "Free"))
    id_mapping = {pid: i + 1 for i, pid in enumerate(unique_ids)}

    # Convert memory state to numbers (Free -> 0, Processes -> Unique IDs)
    numeric_memory = [id_mapping.get(p, 0) for p in memory_state]

    plt.figure(figsize=(12, 5))  # Adjusted size for better fit
    data = np.array(numeric_memory).reshape(1, len(numeric_memory))
    
    ax = sns.heatmap(data, annot=False, fmt="d", cmap="coolwarm", cbar=False, linewidths=0.5)

    ax.set_title("📊 Memory Allocation & Segmentation", fontsize=14, fontweight="bold")
    ax.set_xlabel("Memory Blocks", fontsize=12)
    ax.set_ylabel("Allocation Status", fontsize=12)

    # Adding process labels inside heatmap
    for i, p in enumerate(memory_state):
        if p != "Free":
            ax.text(i + 0.5, 0.5, p, ha="center", va="center", fontsize=8, color="white", fontweight="bold")

    # Creating a dynamic legend
    legend_patches = [
        mpatches.Patch(color=sns.color_palette("coolwarm", len(unique_ids))[i], label=f"Process {pid}") 
        for i, pid in enumerate(unique_ids)
    ]

    # Fix: Explicitly adding legend to the figure
    legend = plt.legend(handles=legend_patches, title="Process Legend", loc="upper right",
                        bbox_to_anchor=(1, 1), fontsize=10, frameon=True)
    
    plt.gca().add_artist(legend)  # Ensure legend is drawn

    plt.xticks([])
    plt.yticks([])

    plt.show()
 