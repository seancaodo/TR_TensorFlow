import random
import matplotlib.pyplot as plt


h = 250
sim = 5000
n_arms = 5
counts = [0]*5
values = [0]*5
rewards = [0.1, 0.1, 0.1, 0.1, 0.2]
epsilon = 0.1
acc_track = [0]*h
cum_acc_track = [0]*h
chosen_arms = [0]*h

for j in range(sim)
    for i in range(h):
      if random.random() > epsilon:
        max_arm = values.index(max(values))
        chosen_arms[i] = max_arm
        if max_arm == 4:
          acc_track[i] = 1
        counts[max_arm] = counts[max_arm]+1
        if random.random() <= rewards[max_arm]:
          draw = 1
        else:
          draw = 0
        values[max_arm] = (values[max_arm]*(counts[max_arm]-1) + draw)/counts[max_arm]
      else:
        choose_arm = random.randrange(n_arms)
        chosen_arms[i] = choose_arm
        if choose_arm == 4:
          acc_track[i] = 1
        counts[choose_arm] = counts[choose_arm]+1
        if random.random() <= rewards[choose_arm]:
          draw = 1
        else:
          draw = 0
        values[choose_arm] = (values[choose_arm]*(counts[choose_arm]-1) + draw)/counts[choose_arm]
    
for i in range(h):
  cum_acc_track[i] = sum(acc_track[0:i])/(i+1)
