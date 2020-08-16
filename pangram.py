sentence=str(input("enter the string")).lower()
converting_string_into_set=list(sorted(set(sentence)))
flag=0
for alpha in range(97,123):
    for string in converting_string_into_set:
        if(chr(alpha)==string):
            flag=flag+1
            break
if(flag==26):
    print("it is pangram")
else:
    print("it is not pangram")
    
