def change(prev_ch, new_ch):
    return min(abs(ord(prev_ch) - ord(new_ch)), 26 - abs(ord(prev_ch) - ord(new_ch)))


def get_name(cur_name, name, idx, move, min_move):
    update_name = cur_name.copy() # 시작 문자 AAAA 에서 -> 점차  update 중인 current_name 복사 => update
    if cur_name[idx] != name[idx]: # name update
        update_name[idx] = name[idx]

    if "".join(update_name) == name: # update 끝 나면 지금까지의 움직임과 최소움직임(name 길이) 중 작은게 최소 조작수  
        return min(min_move, move)

    if min_move <= move: # 최소 움직임(name 길이)가 move 보다 작으면 걍 우측으로 쭉 이동하는게 최소 조작수
        return min_move

    # right 이동 분기
    right_idx = (idx + 1) % len(name)
    right_move = get_name(update_name, name, right_idx, move + 1, min_move)

    # left 이동 분기
    left_idx = (idx - 1) % len(name)
    left_move = get_name(update_name, name, left_idx, move + 1, min_move)

    return min(right_move, left_move, min_move) # dfs를 통한 좌우 이동 분기에서 return 한 최소 값들 끼리의 비교 중 제일 작은 값 return


def solution(name):
    answer = 0

    cur_name = ["A"] * len(name)

    for i in range(len(name)):
        answer += change("A", name[i])

    min_move = len(name) - 1

    min_move = get_name(cur_name, name, idx=0, move=0, min_move=min_move)

    answer = min_move + answer

    return answer

