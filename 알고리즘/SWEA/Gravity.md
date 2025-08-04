가로 N 세로 100 크기의 방에 상자들이 쌓여있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 가장 큰 낙차를 구하여라

[제약 사항]
중력은 회전이 완료된 후 적용된다.
상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
방의 세로 길이는 항상 100이다. 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 줄에는 방의 가로길이가 주어지고 그 다음 줄부터는 쌓여있는 상자의 수가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

[그림설명]
총 26개의 상자가 회전 후, 오른쪽 방 그림의 상태가 된다. A 상자의 낙차가 7로 가장크므로 7을리턴하면 된다.
회전 결과, B상자의 낙차는6, C상자의 낙차는 1이다.
```
T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    box = list(map(int, input().split()))
    max_result = 0
    for count in range(length):         # length 길이 만큼 순회
        cnt = 0
        for rotation in box[count:length]:      # 순회하는 길이만큼 슬라이싱 후 순회
            if box[count] <= rotation:          # 순회한 값이 box[인덱스]보다 클경우 cnt 1씩추가
                cnt += 1
        max_cnt = length - (count + cnt)        # 순회한 값의 최댓값 = 길이 - (인덱스 + 카운트)
        max_result = max(max_cnt, max_result)   # 순회한 값의 최댓값 비교

    print(f'#{test_case} {max_result}')
```
