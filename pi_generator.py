def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(stringInput):
    if stringInput == stringInput[::-1]:
        return True
    else:
        return False

def pi_generator():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    # 50000
    while True:
        if 4*q+r-t < n*t:
            yield n
            nr = 10*(r-n*t)
            n = ((10*(3*q+r))//t)-10*n
            q *= 10
            r = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr
def main():
    halt_flag = False
    checks_made = 0
    pi_digits = pi_generator()
    
    candidateStr = ""
    while not(halt_flag):
        if len(candidateStr) < 9:
            candidateStr += str(next(pi_digits))
        else:
            checks_made += 1
            if is_palindrome(candidateStr):
                # print("{} is a palindrome.".format(candidateStr))
                if is_prime(int(candidateStr)):
                    print("{} is palindromic and prime.".format(candidateStr))
                    halt_flag = True
            # else:
            #     print("{} is not a palindrome.".format(candidateStr))
            candidateStr = candidateStr[1:] + str(next(pi_digits))
            if (checks_made%100 == 0):
                print("checks_made: {}".format(checks_made))    

if __name__ == "__main__":
    main()