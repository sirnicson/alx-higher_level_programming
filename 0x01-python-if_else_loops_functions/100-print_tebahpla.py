#!/usr/bin/python3
print(''.join(f"{chr(122 - i).lower() if i % 2 == 0 else chr(90 - i)}" for i in range(26)), end='')
