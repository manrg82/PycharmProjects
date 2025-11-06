def encontrar_primos(limite):
  for num in range(2, limite + 1):
    is_prime = True
    for i in range(2, num):
      if num % i == 0:
        is_prime = False
        break
    if is_prime:
        print(num)
encontrar_primos(777)