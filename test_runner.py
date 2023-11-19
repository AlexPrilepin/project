def test_file(test):
	namespace = {"A":1}
	result = exec(compile(open(test).read(), test, 'exec'), namespace)
	print(namespace["result"])

