import os

print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(__file__))
print(__file__)