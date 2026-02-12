def solution(numbers, direction):
    answer = []
    return [numbers[len(numbers)-1]] + numbers[:len(numbers)-1]  if direction == "right" else numbers[1:] + [numbers[0]]