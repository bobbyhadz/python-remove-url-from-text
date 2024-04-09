# Remove URLs from Text in Python 

import re

my_string = """
First https://bobbyhadz.com
https://google.com Second
Third https://bobbyhadz.com
"""

result = re.sub(r'http\S+', '', my_string, flags=re.MULTILINE)

# First
#  Second
# Third
print(result)