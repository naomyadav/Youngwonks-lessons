# define seive(n):
#     l =range(n+1)
#     l2=list(l)
#     curent value = l[2]
#     while curent value is in l:
#         if curent value in l2:
#             l2.remove(mulltiples of curent value)
#         else:
#             continue loop
#         curent value+=1
#     return l2
#     end seive


def seive(n):
    n = n+1
    nums =range(n)
    prime_list=list(nums)
    current_value = nums[2]
    while current_value in nums:
        #print(f'current value={current_value}')
        if current_value in prime_list:
            # remove all multiples of current_value from prime_list not including current_value
            for k in range(2*current_value,n,current_value):
                if k in prime_list:
                    #print(f'   k={k}')
                    #print(f'   prime list={prime_list}')
                    prime_list.remove(k)
        current_value+=1
    prime_count = len(prime_list)
    print(f'prime count = {prime_count}')
    print(f'prime list = {prime_list}')
    return prime_list, prime_count

if __name__=="__main__":
    seive(200)

