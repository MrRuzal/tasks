# Given a random non-negative number, you have to return the digits of this number within an
# array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

def digitize(n):
    result_list = []
    for i in str(n):
        result_list.append(int(i))
    result_list.reverse()
    return result_list

if __name__ == '__main__':
    n = 35231
    print(digitize(n)) # [1,3,2,5,3]
    n = 0
    print(digitize(n)) # [0]
    n = 23582357
    print(digitize(n)) # [7,5,3,2,8,5,3,2]
    n = 984764738
    print(digitize(n)) # [8,3,7,4,6,7,4,8,9]
    n = 45762893920
    print(digitize(n)) # [0,2,9,3,9,8,2,6,7,5,4]
    n = 548702838394
    print(digitize(n)) # [4,9,3,8,3,8,2,0,7,8,4,5]