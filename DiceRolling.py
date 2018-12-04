
# coding: utf-8

# In[2]:


# Dice Rolling Simulator : https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
import random
RollDice=input('Do you want to roll the dice:')
RollDice = RollDice.upper()
while(RollDice == 'YES'):
    print(random.randint(1,6))
    RollDice=input('Do you want to roll the dice again:')
    RollDice = RollDice.upper()

    

