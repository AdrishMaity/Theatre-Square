import math

def main():

    n,m,a = map(int,input().split(' '))

    # along n number of a is
    x = math.ceil(n/a)

    # along n number of a is
    y = math.ceil(m/a)

    print(x*y)

if __name__ == "__main__":
    main()
