"""
    *rough* Algorithmic logic to solving Sudoku
    
    Step 1.
        Pick and empty square    
    Step 2.
        Try all numbers
    Step 3.
        Find one that works
    Step4.
        Repeat until dead end
    Step 5.
        Backtrack 
        (go back to last sucessful location and try to advance
        with a different number, if no numbers advance to end
        go back further)
        
"""