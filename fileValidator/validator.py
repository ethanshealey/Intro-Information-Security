import hashlib
import os

if not os.path.exists('integrity'):
    print('File \'integrity\' not found, creating new integrity file')
    with open('integrity', 'w+') as file:
        with open('target.txt', 'r') as target_file:
            target = hashlib.sha256(target_file.read().encode()).hexdigest()
        file.write(target)

else:
    with open('integrity', 'r') as file:
        content = file.read()
        
    with open('target.txt', 'r') as file:
        target = hashlib.sha256(file.read().encode()).hexdigest()

    
    if content == target:
        print('File integrity matches')
    else:
        print('File integrity does not match')