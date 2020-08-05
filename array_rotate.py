
def solution(A, K):
	return A[K:] + A[:K]


# Test
print(solution([2,3,5,6,7],3))