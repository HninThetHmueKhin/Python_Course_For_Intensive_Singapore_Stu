import os

os.chdir('/Users/khine/Desktop/')
#os.makedirs('OS-Demo-1/Sub-Dir-1')
print(os.listdir())

dest = '/Users/khine/Desktop/OS-Demo-1/Sub-Dir-1/test.txt'

print(os.stat(dest).st_mode)


