# Import necessary libraries
#%matplotlib inline
import numpy as np
#import matplotlib.pyplot as plt
#from tqdm import tqdm
import time

#from rlglue.rl_glue import RLGlue
#import main_agent
#import ten_arm_env
#import test_env

#import grader

def argmax(q_values):
    """
    Takes in a list of q_values and returns the index of the item 
    with the highest value. Breaks ties randomly.
    returns: int - the index of the highest value in q_values
    """
    top_value = float("-inf")
    ties = []
    
    for i in range(len(q_values)):
    	if q_values[i]>top_value:
    		top_value = q_values[i]
    		ties=[i]
    	elif q_values[i] == top_value:
    		ties.append(i)
    	print(ties)
        print("/////////////") 	  	
        # if a value in q_values is greater than the highest value update top and reset ties to zero
        # if a value is equal to top value add the index to ties
        # return a random selection from ties.
        ### BEGIN SOLUTION (~5-7 lines)
        ### END SOLUTION
    
    return np.random.choice(ties)
    
    
q_values = [0.14, 0.43, 0.67, 0.11, 0.03, 6.67]
counts = [0, 0, 0, 0, 0, 0]  #Counts the number of times a particular q_value has been chosen as maximum.
for _ in range(1):
    a = argmax(q_values)
    counts[a] += 1
print(counts)