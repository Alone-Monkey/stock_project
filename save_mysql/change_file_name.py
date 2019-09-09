with open('code.txt','w') as file:
    with open('all.txt','rt') as f:
        data = f.readlines()
        for i in data:
            i = i.replace('\n','')
            if i[0:2] == '60':
                i = 'SH' + i
            else:
                i = 'SZ' + i
            print(i)
            file.writelines(i+'\n')