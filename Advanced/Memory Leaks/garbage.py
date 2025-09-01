import gc

gc.enable()

gcO = gc.collect()

print(gcO)
allOb = gc.get_objects()
print(len(allOb))