def falling_distance():
    for el in range(1, 11):
        print(el)
        d = 0.5 * 9.8 * el**2
        print('{0:.1f}'.format(d).rstrip('0').rstrip('.'))
        
falling_distance()
