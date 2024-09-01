numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()

for elem in numbers:
    is_prime = True

    if elem == 1:
        continue

    for divider in range(2, elem):
        if elem % divider == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(elem)
    else:
        not_primes.append(elem)

print('Primes: {}'.format(primes))
print('Not primes: {}'.format(not_primes))
