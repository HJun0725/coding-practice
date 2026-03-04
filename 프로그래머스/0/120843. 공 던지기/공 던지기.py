def solution(numbers, k):
    return (1+(k-1)*2)%len(numbers) if (1+(k-1)*2)%len(numbers) != 0 else len(numbers)