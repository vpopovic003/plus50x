import os


# List to hold all source files per lecture
source = {}

# Which lecture
lecture = "src1"
path = (f"static/files/source/{lecture}")
# Open folder, add files to the list
for f in os.listdir(path):
    with open(os.path.join(path, f)) as f:
        source[os.path.basename(f.name)] = f.read()

for item in source:
    # Prints value
    print(source[item])
