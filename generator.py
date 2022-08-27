import numpy
import json
import random

def matrix_multiplication(A, B): #行列AとBの掛け算
    a = len(A)
    b = len(A[0])
    c = len(B[0])
    M = []
    for i in range(a):
        M.append([])
    for i in range(a):
        for k in range(c):
            M[i].append(0)
    for i in range(a):
        for k in range(c):
            s = 0
            for j in range(b):
                s += A[i][j] * B[j][k]
            M[i][k] = s
    return M

def main():
  test_cases = []

  for _ in range(40):

    p = random.randint(1, 30)

    IN = str(p) + ' ' + str(p) + '\n'

    A = []
    for i in range(p):
      line = [random.randint(0, 30) for j in range(p)]
      A.append(line)
      line = [str(el) for el in line]
      IN += ' '.join(line) + '\n'


    ans = matrix_multiplication(matrix_multiplication(A, A), A)

    OUT = ''
    for line in ans:
      line = [str(el) for el in line]
      OUT += ' '.join(line) + '\n'


    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}"
    })

  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()