import random


def main():
    total = 0
    for i in range(100):
        a = random.randint(1, 100)
            
        if a % 2:
            total = total + 1
    print('Четных чисел: ',total)
                
    
    

main()

 