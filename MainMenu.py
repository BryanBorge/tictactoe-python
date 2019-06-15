import tictac as tt

print('Would you like to play the console or GUI version?')

while True:
    ans = input("1. Console\n2. GUI\nEnter 1 or 2: ")
    if ans not in ('1','2'):
        continue
    if ans == '1':
        tt.main()