import heapq

# 오른차순 힙 정렬(heap sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내여 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 내림차순은 heap라이브러리 원소에 - 추가
def heapsort_reverse(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내여 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result = heapsort_reverse([1,3,5,7,9,2,4,6,8,0])
print(result)