#!/usr/bin/env python3

def main():
    nums = [int(n) for n in input().strip().split()]
    full_rooms = nums[1:]
    rooms = nums[0] * [0]
    for n in full_rooms:
        rooms[n - 1] = 1
    if sum(rooms) != len(rooms):
        print(rooms.index(0) + 1)
    else:
        print("no room")


if __name__ == "__main__":
    main()
