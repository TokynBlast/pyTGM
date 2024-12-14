def integer(min_value, max_value, seed=None):
    if seed == None:
      try: seed = int(time() * 1000)
      except: from time import time; seed = int(time() * 1000)
              
      number = (seed % (max_value - min_value + 1)) + min_value
      return number
