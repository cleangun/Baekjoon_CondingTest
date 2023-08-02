from string import ascii_lowercase

def solution(s, skip, index):
    alphabet_list = list(ascii_lowercase)
    skip = set(sorted(list(skip))) ; answer = []
    for ch in s:
        plus_index = index
        idx = alphabet_list.index(ch)
        while plus_index > 0:
            idx += 1
            if idx >= 26:
                idx = 0
            if alphabet_list[idx] in skip:
                continue
            plus_index -= 1
        answer.append(alphabet_list[idx])
    answer = "".join(answer)
    return answer