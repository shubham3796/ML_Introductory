//implementing the epsilon greedy strategy
import numpy as np
import time


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
    
class EpsilonGreedyAgent():
    def agent_step(self, reward, observation):
        
        
        # Update Q values - this should be the same update as your greedy agent 
        ### BEGIN SOLUTION (~3-5 lines)
        self.arm_count[self.last_action] += 1
        #?????????????
        self.q_values[self.last_action] += (reward-self.q_values[self.last_action])/self.arm_count[self.last_action]
        ### END SOLUTION
        
        # Choose action using epsilon greedy
        # Randomly choose a number between 0 and 1 and see if it's less than self.epsilon
        # (hint: look at np.random.random()). If it is, set current_action to a random action.
        random_num = np.random.random()
        if random_num < self.epsilon:
            current_action = np.random.randint(0,len(self.arm_count))
        else:
        # otherwise choose current_action greedily as you did above.
        ### BEGIN SOLUTION (~4 lines)
            current_action = argmax(self.q_values)
        ### END SOLUTION
        
        self.last_action = current_action
        
        return current_action
        

np.random.seed(0)
e_greedy_agent = EpsilonGreedyAgent()
e_greedy_agent.q_values = [0, 0.0, 0.5, 0, 0]
e_greedy_agent.arm_count = [0, 1, 0, 0, 0]
e_greedy_agent.num_actions = 5
e_greedy_agent.last_action = 1
e_greedy_agent.epsilon = 0.5
# given this random seed, we should see a greedy action (action 2) here
action = e_greedy_agent.agent_step(reward=1, observation=0)
print(e_greedy_agent.q_values)
print(e_greedy_agent.arm_count)
print(action)


# let's see what happens for another action
np.random.seed(1)
e_greedy_agent = EpsilonGreedyAgent()
e_greedy_agent.q_values = [0, 0.5, 0.5, 0, 0]
e_greedy_agent.arm_count = [0, 1, 0, 0, 0]
e_greedy_agent.num_actions = 5
e_greedy_agent.last_action = 1
e_greedy_agent.epsilon = 0.5
# given this random seed, we should see a random action (action 4) here
action = e_greedy_agent.agent_step(reward=1, observation=0)
print(e_greedy_agent.q_values)
print(e_greedy_agent.arm_count)
print(action)
