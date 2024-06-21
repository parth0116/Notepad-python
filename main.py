import pandas as pd
import numpy as np
def slicer(names):
    if len(names)%2==0:
        return 'Even'
    else:
        return names[0]
name=['Andy','Eve','Jose','Sally']