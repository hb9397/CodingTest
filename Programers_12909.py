# https://school.programmers.co.kr/learn/courses/30/lessons/12909
'''
해당 문제는 ())()() 또는 ((())()) 와 같은 문자열이 주어질 때, 전자의 경우는 ()와 같은 올바르게 괄호가
묶여져있지 않은경우로, 후자는 ()의 괄호 쌍이 올바르게 묶인 경우로 취급하는 문제이다.
1. Stack을 이용해서 현재 문자열이 ( 인 경우에 Stack temp 에 삽입한다.
2. 만약 현재 문자열이 ) 인 경우에 현재 스택의 길이가 0 보다 클때를 분류하는데 이유는 temp라는 스택에는 ( 만 삽입
    되기 때문이다, 그래서 len(temp) > 0 이면 현재 stack 에 ( 가 있으므로 올바른 괄호 쌍 ()을 분류 할 수 있어서
    ( 를 하나 Pop 한다.
3. 만약 현재 문자열이 ) 인 경우인데 Stack temp 의 길이가 0이라면, 아직 ( 가 한 번도 문자열에서 탐색 되지 않았거나
    이미 올바른 괄호 쌍으로 취급되어 pop 된 경우인데, 이 때 ) 가 오게 되면 시작 괄호가 )로 취급 되기 때문에 무조건 틀린
    경우로 취급해야 한다.

4. 만약 위 경우를 전부 True로 통과했는데 stack 에 값이 남아있는 경우에는 (가 )보다 문자열에 많은 경우로 이 또한
    len(temp) > 0 으로 분류해 잘못된 괄호 쌍으로 취급하면 주어진 문자열이 올바른 괄호쌍으로 이뤄졌는지ㅣ, 그렇지 않은지
    알 수 있다.
'''
def solution(s):
    answer = True
    temp = []
    for item in s:
        if item == '(':
            temp.append(item)

        if item == ')':
            if len(temp) > 0:
                temp.pop()
            # temp 에 ( 가 존재하지 않는 상태에서 )가 들어가버리면 이미 잘못된
            # 괄호 문자열에 해당된다.
            else:
                answer = False

    if len(temp) != 0:
        answer = False

    return answer