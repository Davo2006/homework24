x = {"h":10,"_k":55}
y = {"i":17,"l":55}
x.update(y)
t = {i:x[i] for i in x if not i.startswith("_")}
print(t)