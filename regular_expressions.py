import re

numeric=r'[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'

if __name__=='__main__':
  re.findall(numeric,"1.2 1.2e-3 text 1.2e3 100e3 -1e3")
