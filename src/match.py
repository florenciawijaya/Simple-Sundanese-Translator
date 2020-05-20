def fail(pattern):
    fail = [0]*len(pattern)
    fail[0] = 0
    i = 1
    j = 0
    while(i<len(pattern)):
        if(pattern[j]==pattern[i]):
            fail[i] = j+1
            i+=1
            j+=1
        elif(j!=0):
            j = fail[j-1]
        else:
            fail[i] = 0
            i+=1
    return fail

def kmpMatch(pattern, text):
    border = fail(pattern)
    i = 0
    j = 0
    while(i<len(text)):
        if(pattern[j]==text[i]):
            if(j==len(pattern)-1):
                return i-len(pattern)+1,i
            i+=1
            j+=1
        elif(j!=0):
            j = border[j-1]
        else:
            i+=1
    return -1,-1

def lastOccurrence(pattern):
    last = [-1]*128
    for i in range(len(pattern)):
        last[ord(pattern[i])] = i
    return last

def bmMatch(pattern, text):
    last = lastOccurrence(pattern)
    i = len(pattern)-1
    j = len(pattern)-1
    if(i>len(text)-1):
        return -1
    else:
        j = len(pattern)-1
        while(i<=len(text)-1):
            if(pattern[j]==text[i]):
                if(j==0):
                    return i
                else:
                    i-=1
                    j-=1
            else:
                lastOc = last[ord(text[i])]
                i = i + len(pattern) - min(j, 1+lastOc)
                j = len(pattern)-1
        return -1

def regexMatch(pattern, text):
    hasil = re.findall(pattern, text)
    hasilIter = re.finditer(pattern, text)
    if(len(hasil)!=0):
        for i in hasilIter:
            return i.start(),i.end()-1
    else:
        return -1,-1