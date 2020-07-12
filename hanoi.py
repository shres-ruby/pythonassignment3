def hanoi(n, source, destination, transit):
    '''Tower of Hanoi algorithm'''

    if n == 1:
        print(f'Move disk 1 from {source} to {destination}')

    elif n < 1:
        raise Exception("Please enter a positive integer")

    else:
        hanoi(n-1,source, transit, destination)
        print(f'Move disk {n} from {source} to {destination}')
        hanoi(n-1, transit, destination, source)

hanoi(4, "A", "B", "C")
