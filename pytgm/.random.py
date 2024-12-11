class num:
  @staticmethod
  def integer(min_value, max_value, seed=None):
    if seed == None:
      try: seed = int(time() * 1000)
      except: from time import time; seed = int(time() * 1000)
                
      number = (seed % (max_value - min_value + 1)) + min_value
      return number
    
   @staticmethod
   def binary(): return random.num.integer(0,1)
    
class seq:
  @staticmethod
  def choose(lst, amnt=1): return [random.seq.choose.choice(lst) for _ in range(amnt)]

  class modify:
    @staticmethod
      def shuffle(lst, times=1):
        shuffled_list = lst[:]
        for i in range(times):
          for i in range(len(shuffled_list)):
            rand_index = random.num.integer(0, len(shuffled_list) - 1)
             shuffled_list[i], shuffled_list[rand_index] = shuffled_list[rand_index], shuffled_list[i]
          return shuffled_list
                
     @staticmethod
     def duplicate(lst, times=1):
       shuffled_list = lst
       for i in range(times):
         for i in range(len(shuffled_list)):
           shuffled_list[i], shuffled_list[random.num.integer(0, len(shuffled_list) - 1)] = shuffled_list[random.num.integer(0, len(shuffled_list) - 1)], shuffled_list[i]
       return shuffled_list
                
     @staticmethod
     def remove(lst, amnt): return [lst.remove(random.seq.choose.choice(lst)) for _ in range(amnt)]