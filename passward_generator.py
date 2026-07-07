#Random passward generator
# list comprehension

import random 
import string

pass_len = 8
charvalue = string.ascii_letters + string.digits + string.punctuation

res = "".join([random.choice(charvalue) for i in range(pass_len)])
#.join is used to convert list into a single string
print("Random passward is ", res)

