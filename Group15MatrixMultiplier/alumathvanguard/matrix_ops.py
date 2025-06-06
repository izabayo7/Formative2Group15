"""
Matrix Operations Module
Handles matrix multiplication with personality and humor!
"""

import random
from typing import List, Union


class Matrix:
    """A matrix class that stores 2D arrays and provides basic operations."""
    
    def __init__(self, data: List[List[Union[int, float]]]):
        """
        Initialize a matrix with 2D list data.
        
        Args:
            data: 2D list representing the matrix
        """
        if not data or not data[0]:
            raise ValueError("Matrix cannot be empty!")
        
        # Check if all rows have the same length
        row_length = len(data[0])
        for i, row in enumerate(data):
            if len(row) != row_length:
                raise ValueError(f"All rows must have the same length! Row {i} has length {len(row)}, expected {row_length}")
        
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
    
    def __str__(self):
        """String representation of the matrix."""
        result = []
        for row in self.data:
            result.append("[" + " ".join(f"{x:8.2f}" for x in row) + "]")
        return "\n".join(result)
    
    def __repr__(self):
        return f"Matrix({self.rows}x{self.cols})"
    
    def get_dimensions(self):
        """Return matrix dimensions as (rows, cols)."""
        return (self.rows, self.cols)

def create_matrix(data):
    """Convenience function to create a Matrix object."""
    return Matrix(data)
