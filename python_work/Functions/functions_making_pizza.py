# Importing an Entire Module
import functions_pizza 


# Importing an Entire Module and using alias
import functions_pizza as fp

# Importing Specific Functions
from functions_pizza import make_pizza

# Importing Specific Functions
from functions_pizza import make_pizza as mp

# Importing All functions in a Module
from functions_pizza import *

# Entire Module

fp.make_pizza(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')

# Specific Functions

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')