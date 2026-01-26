"""
PyTorch Workflows - Main Entry Point
"""
import torch
import torch.nn as nn


def main():
    """Main function to demonstrate PyTorch basics."""
    print("PyTorch Workflows")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    # Create a simple tensor
    x = torch.randn(3, 3)
    print(f"\nSample tensor:\n{x}")


if __name__ == "__main__":
    main()
