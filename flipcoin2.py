import random

def flipCoin():
    heads = 0
    tails = 0
    hper = 0 
    tper = 0 

    for i in range(1000): 
      coin=random.randint(1,2) 
      if coin==1: 
          heads+=1
      else:
          tails+=1

    hper = heads / 10.0 
    tper = 100.0 - hper

    print("Heads percent: " + str(hper))
    print("Tails percent: " + str(tper))

flipCoin() 
