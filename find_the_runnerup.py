############################################FIND THE RUNNER UP SCORE#######################################################
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?i
'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.

Input Format
    The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints
    2 <= n <= 10
     -100 <= A[i] <= 100
Output Format
    Print the runner-up score.
'''
###################################################################################################


if __name__ == '__main__':
    n = int(input())
    if not (2 <= n <= 10):
        print('"n" is Out of bounds')
    else:
        arr = list(map(int, input().split()))
        
        arr = [item for item in arr if -100 <= item <= 100]
        
        no_dupes = []
        for item in arr:
            if item not in no_dupes:
                no_dupes.append(item)

        if len(no_dupes) < 2:
            print("Few Elements")
        else:
            arr_sorted = sorted(no_dupes)
            
            menor = arr_sorted[0]
            maior = arr_sorted[-1]
            
            segundo_maior = arr_sorted[-2]
            print(segundo_maior)
            '''
            print("Maior:", maior)
            print("Segundo maior:", segundo_maior)
            print("Menor:", menor)
            '''
