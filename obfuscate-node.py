import sys
import time
import subprocess

def main():
    a = time.perf_counter()
    subprocess.run(["node", "./test.js", sys.argv[1]])
    b = time.perf_counter()
    print(f"Python node syscall:  {b - a:0.3f}s")

if __name__ == '__main__':
    main()
