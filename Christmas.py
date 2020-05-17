def the_tree(n):
    z = n - 1
    x = 1
    for i in range(n):
        print(' ' * z + '+' * x + ' ' * z)
        x += 2
        z -= 1
    print('   Merry Christmas !!')


the_tree(12)
