import sys
from lib.dispatcher import Dummy
from custom_logging import my_logger

@my_logger(["username"])
def login(username, password):
	pass

@my_logger()
def foo(x):
	pass

@my_logger()
def bar(collection, items):
	pass

if __name__ == "__main__":
	username = "gabriel"
	password = "secret"
	x = 15
	dummy = Dummy()
	login(username=username, password=password)
	foo(x)
	bar({"a":1, "b":2}, [0,1,2])
	dummy.do_this(y=2, x=x)
	dummy.do_that()