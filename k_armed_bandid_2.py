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
        # if a value in q_values is greater than the highest value update top and reset ties to zero
        # if a value is equal to top value add the index to ties
        # return a random selection from ties.
        ### BEGIN SOLUTION (~5-7 lines)
    	if q_values[i]>top_value:
    		top_value = q_values[i]
    		ties=[i]
    	elif q_values[i] == top_value:
    		ties.append(i)
    	
        
        ### END SOLUTION
    
    return np.random.choice(ties)
    
class GreedyAgent():
    def agent_step(self, reward, observation):
        """
        Takes one step for the agent. It takes in a reward and observation and 
        returns the action the agent chooses at that time step.
        
        Arguments:
        reward -- float, the reward the agent recieved from the environment after taking the last action.
        observation -- float, the observed state the agent is in. Do not worry about this as you will not use it
                              until future lessons
        Returns:
        current_action -- int, the action chosen by the agent at the current time step.
        """
        ### Useful Class Variables ###
        # self.q_values : An array with what the agent believes each of the values of the arm are.
        # self.arm_count : An array with a count of the number of times each arm has been pulled.
        # self.last_action : The action that the agent took on the previous time step
        #######################
        
        # Update Q values Hint: Look at the algorithm in section 2.4 of the textbook.
        # increment the counter in self.arm_count for the action from the previous time step
        # update the step size using self.arm_count
        # update self.q_values for the action from the previous time step
        
        ### BEGIN SOLUTION (~3-5 lines)
        self.arm_count[self.last_action] += 1
        #?????????????
        self.q_values[self.last_action] += (reward-self.q_values[self.last_action])/self.arm_count[self.last_action]
        ### END SOLUTION
        
        # current action = ? # Use the argmax function you created above
        ### BEGIN SOLUTION (~2 lines)
        current_action = argmax(self.q_values)
        ### END SOLUTION
    
        self.last_action = current_action
        
        return current_action
        
        
    

np.random.seed(1)
# build a fake agent for testing and set some initial conditions
greedy_agent = GreedyAgent()
greedy_agent.q_values = [0, 0, 0.5, 0, 0]
greedy_agent.arm_count = [0, 1, 0, 0, 0]
greedy_agent.last_action = 1
# take a fake agent step
action = greedy_agent.agent_step(reward=1, observation=0)
print(greedy_agent.q_values)



# build a fake agent for testing and set some initial conditions
greedy_agent = GreedyAgent()
greedy_agent.q_values = [0, 0, 1.0, 0, 0]
greedy_agent.arm_count = [0, 1, 0, 0, 0]
greedy_agent.last_action = 1
# take a fake agent step
action = greedy_agent.agent_step(reward=1, observation=0)
print(greedy_agent.q_values)