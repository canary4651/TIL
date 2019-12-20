from glob import glob

for filename in glob('data/*'):
    with open(filename) as f:
        text = f.read()
        if text[:1] != '{':
            print(filename)
            print(text)
            print()
