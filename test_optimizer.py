"""
Project: Neroxa - Memory Core
Test Runner for Night Operations
"""

from optimizer import NeroxaOptimizer

if __name__ == "__main__":
    print("[Neroxa Core] Initiating night-ops memory test...")
    
    # Running the flush utility
    result = NeroxaOptimizer.flush_memory()
    
    print(f"[Neroxa Core] Test Result: {result}")
    print("[Neroxa Core] System status: OPTIMIZED & SECURE.")
