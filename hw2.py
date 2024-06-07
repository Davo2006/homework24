sent = "hello human hello"
x = {i:sent.count(i) for i in sent.split()}
print(x)