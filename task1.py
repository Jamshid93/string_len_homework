def main(s):
    if s.isalpha():
        answer=True
    elif s.index("*"):
            answer=s[0:s]+s[s+1:-1]
    return answer
print(main("12*34"))