# Insecure password locker
import sys, pyperclip

PASSWORDS = {'email': 'F7min1BDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python passwordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first arg is account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard')
else:
    print(f"There's no account named {account}")