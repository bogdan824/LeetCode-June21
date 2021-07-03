def valid_mountain(arr):
	X = len(arr)
	if len(arr) < 3:
		return False
	i = 0
	#walks up
	while i+1 < X and arr[i]<arr[i+1]:
		i+=1
	#peak
	if i==0 or i == X-1:
		return False
	#down
	while i+1 < X and arr[i] > arr[i+1]:
		i+=1
	return i == X-1
arr = [1,2,3,5,2,1,7]
print(valid_mountain(arr))