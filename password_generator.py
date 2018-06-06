import json
import random
from itertools import product
import string

# while True:
password = []

chars = list(string.ascii_letters) + list('1234567890')
# for n in range(2):
cross = list(product(chars, repeat=3))
list_iteration = []
with open('passwords.json', 'w') as f_obj:
    for each_cross in cross:
        list_iteration.append(''.join(each_cross))
        for each in list_iteration:
            json.dump(each, f_obj)
print(list_iteration)
