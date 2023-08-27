#!/bin/python3
# This program is for generating hash from hash from input data. It uses sha3 512 bit algoritm.
# User is giving input string and number of algoritm iterations.
# One iteration is 1 000 000 hash function.

import time
import hashlib

def do_iterations(data = 'Give me data!', number = 0, verbose = True):
    for i in range(number):
        for _ in range(int(1e6)):
            data = hashlib.sha3_512(data.encode()).hexdigest()
        if verbose: print(data, ' (iteracja: ', i+1,') (pozostało: ', number-(i+1), ')', sep='')

def speed_test(test_loops = 1):   # output is in MH/h
    start = time.time()
    do_iterations('speed_test', test_loops, False)
    return int((test_loops / (time.time() - start))*3600)

def main():
    string1 = input('String wejściowy: ')
    time1 = float(input('Czas generowania [h]: '))
    speed1 = speed_test()
    print('Wydajność:', str(speed1), 'iteracji/h'); time.sleep(1)
    print('Potrzebujesz', str(int(speed1*time1)), 'iteracji'); time.sleep(1)
    number1 = int(input('Ilość iteracji: '))
    do_iterations(string1, number1)

if __name__ == "__main__":
        try: main()
        except ValueError:
             print('Niepoprawna wartość!')
        except KeyboardInterrupt:
             pass
