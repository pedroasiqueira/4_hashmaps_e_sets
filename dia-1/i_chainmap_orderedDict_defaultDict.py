from collections import ChainMap
from collections import OrderedDict
from collections import defaultdict


time = ChainMap({'nome': 'Felps'}, {'idade': '28'}, {'cargo': 'Instrutor'})

# print(time)
# print(time['nome'])
# print(time['idade'])
# print(time['cargo'])


ordered = OrderedDict()
ordered['nome'] = 'Felps'
ordered['idade'] = 28
ordered['cargo'] = 'instrutor'
# print(ordered.keys())


default = defaultdict(list)
default['time'].append('Flávio')
default['time'].append('Felps')
default['time'].append('Carlos')
default['time'].append('Roni')
print(default['time'], default['instrutor'])