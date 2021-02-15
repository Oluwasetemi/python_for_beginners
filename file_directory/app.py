from pathlib import Path

# mkdir, exist, rmdir,
p = Path()
x = p.glob('*')
for file in x:
    print(file)
# [x for x in p.iterdir() if x.is_dir()]

# p1 = Path('../')
# y = list(p1.glob('**/*.py'))
# print(len(y))
