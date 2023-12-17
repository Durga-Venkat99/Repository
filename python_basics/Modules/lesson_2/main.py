import mod1,mod2

mod1.test()
mod2.test()

print(50*"-")

from mod1 import test
from mod2 import test
test()                            # it take's mod2 as a presidence