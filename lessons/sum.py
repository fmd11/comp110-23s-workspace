"""LS16 Unit Tests"""
def sum(xs: list[float]) -> float:
    """return sum of elements in xs"""
    
    for idx in range(0, len(xs), 1):
        sum_total: float = 0.0
        sum_total += xs[idx]  
    return sum_total
    
    # for item in xs:
        # sum_total: float = 0.0 
       # sum_total += item 
    # return sum_total

    # while idx <= len(xs) - 1:
       # sum_total += xs[idx]
      #  idx += 1 
   # return sum_total