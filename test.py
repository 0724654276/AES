from string import ascii_uppercase as l

class CypherTable:
   def __init__(self):
      self.final_table = [l[i:]+l[:i] for i in range(len(l))]

for i in CypherTable().final_table:
    print(i)