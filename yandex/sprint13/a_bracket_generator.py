def backtrack(current, open_count, close_count, n):
    if len(current) == 2 * n:
        print(current)
        return
    if open_count < n:
        backtrack(current + '(', open_count + 1, close_count, n)
    if close_count < open_count:
        backtrack(current + ')', open_count, close_count + 1, n)


if __name__ == '__main__':
    backtrack('', 0, 0, n=int(input()))
