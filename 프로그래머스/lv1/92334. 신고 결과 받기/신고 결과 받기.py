def solution(id_list, report, k):
    answer = [0] * len(id_list)
    repcount = {x : 0 for x in id_list}
    
    for rep in set(report):
        target = rep.split()[1]
        repcount[target] += 1
    
    for rep in set(report):
        user,target = rep.split()
        if repcount[target] >= k:
            answer[id_list.index(user)] += 1
    
    return answer