class table:
  table_ = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890?!@#$%^&*()_+-=[]{}\\|/,.<>~`;:'" '''
  
  @staticmethod
  def tableGen(self, chars, times):
      table = encryption.b64.table.table_
      self.table = random.seq.modify.shuffle(self.table, times)
      return table
      
  @staticmethod
  def tableSet(self, chars): 
      if type(chars) == str: self.table = chars
          
def encode(self, text):
  bins = str()
  for c in text:
      bins += '{:0>8}'.format(str(bin(ord(c)))[2:])
  while len(bins) % 3:
      bins += '00000000'
  d = 1
  for i in range(6, len(bins) + int(len(bins) / 6), 7):
      bins = bins[:i] + ' ' + bins[i:]
  bins = bins.split(' ')
  if '' in bins:
      bins.remove('')
  base64 = str()
  for b in bins:
      if b == '000000':
          base64 += '='
      else:
          base64 += self.table_[int(b, 2)]
  return base64

def decode(self, text):
  bins = str()
  for c in text:
      if c == '=':
          bins += '000000'
      else:
          bins += '{:0>6}'.format(str(bin(encryption.b64.table.table_.index(c)))[2:])
  for i in range(8, len(bins) + int(len(bins) / 8), 9):
      bins = bins[:i] + ' ' + bins[i:]
  bins = bins.split(' ')
  if '' in bins:
      bins.remove('')
  text = str()
  for b in bins:
      if not b == '00000000':
          text += chr(int(b, 2))
  return text
