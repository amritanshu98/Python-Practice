# Check if string starts with specific prefix 
from annotated_types import T


text = "Python programming is fun" 
prefix = "Python"

# index = text.find(prefix)

# if index ==0:
#     print(True)

# else:
#     print(False)


if text.lower().startswith(prefix.lower()):
    print(True)

else:
    print(False)