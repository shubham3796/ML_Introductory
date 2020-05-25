import numpy as np
import pickle
#import tools

num_spaces = 3
num_prices = 3
#env = tools.ParkingWorld(num_spaces, num_prices)
V = np.zeros(num_spaces + 1)
pi = np.ones((num_spaces + 1, num_prices)) / num_prices

for s, v in enumerate(V):
    print "State {", s , "}, has value {" , v ,"}"
   
state = 0 
pi[state] = np.array([0.75, 0.21, 0.04])
print pi

#for s, pi_s in enumerate(pi):
#    print(f''.join(f'pi(A={a}|S={s}) = {p.round(2)}' + 4 * ' ' for a, p in enumerate(pi_s)))