

with open('KakaoTalk_friend.txt', 'r', encoding='utf-8') as input_file:
    out=open('kakaotalk.txt','w')
    while(1):
        s=input_file.readline()
        if not s:
            break
        s=s.split(']')
        if(len(s)<3):
            continue
        out.write(s[2])
    out.close()

