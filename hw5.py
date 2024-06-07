x = "hello my name is john"
y = {i:len(i) for i in x.split() if len(i) > 3}
print(y)