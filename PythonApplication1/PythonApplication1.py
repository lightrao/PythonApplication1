import sys
from math import sin, cos, radians

# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    rad = radians(x)                             # cos works with radians
    numspaces = int(20 * cos(radians(x)) + 20)   # scale to 0-40 spaces
    str = ' ' * numspaces + 'o'                  # place 'o' after the spaces
    return str

def main():
    for i in range(0, 1800, 12):
        s = make_dot_string(i)
        print(s)

#main()

if __name__ == "__main__":
    sys.exit(int(main() or 0))

#change for github test.

