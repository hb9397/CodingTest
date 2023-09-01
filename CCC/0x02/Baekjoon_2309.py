# https://www.acmicpc.net/problem/2309

# 해당 문제는 9명의 난쟁이 중 가짜 난쟁이 두명을 제외한 진짜 난쟁이 7명의 키의 합이 100
# 으로 9명의 난쟁이 중 7명의 조합의 합이 100인 경우를 찾는 문제이다.
# 하지만 조합의 성질로 인해 이 경우의 수는 9명의 난쟁이 중 가짜 난쟁이 2명을 찾아 어떤값 X를 찾는 것과 같으며
# 이 X는 9명의 조합 중 2명의 키 조합이 [난쟁이 키의 전체 합 - 100] 에 해당되는 문제로 생각하는 것이 코드로 풀어내는데 더 적합하다.

arrHeights = [int(input()) for _ in range(9)]

finish = False
fake1, fake2 = 0, 0

for i in range(8):
    for j in range(i+1, 9):
        if sum(arrHeights) - (arrHeights[i] + arrHeights[j]) == 100:
            fake1 = arrHeights[i]
            fake2 = arrHeights[j]

            finish = True
            break

    if finish:
        break

arrHeights = sorted(arrHeights)
arrHeights.remove(fake1)
arrHeights.remove(fake2)

for i in range(7):
    print(arrHeights[i])