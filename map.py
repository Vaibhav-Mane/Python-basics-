# txt = ['lambda functions are anonymous functions.',
#  'anonymous functions dont have a name.',
#  'functions are objects in Python.']
# mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
# print(list(mark))
## Data
letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''
## One-Liner
find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1
## Result
print(find(letters_amazon, 'SQL'))