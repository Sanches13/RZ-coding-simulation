#!/usr/bin/env python3
import rz

def main():
    data = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0]
    print(rz.get_decoded_sequence(data))

if __name__ == "__main__":
    main()
