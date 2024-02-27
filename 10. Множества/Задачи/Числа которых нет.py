nums = {'0','1','2','3','4','5','6','7','8','9'}
res = nums.difference(set(input()).intersection(nums))
print(''.join(sorted(res, reverse=True)) if len(res) != 0 else 'NO')