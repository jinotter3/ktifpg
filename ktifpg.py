# Korean Text Input for Pygame
import hgtk

def jaummoum(a):
    if ord(a)>=12593 and ord(a) <=12622:
        if ord(a) == 12600 or ord(a) == 12611 or ord(a) == 12617:
            return 2
        return 1

    elif ord(a) >=12623 and ord(a) <=12643:
        return 3
    else:
        return 4


def ssangjaum(a,b):
    if ord(a) == 12593 and ord(b) == 12613:
        return 'ㄳ'
    elif ord(a) == 12596 and ord(b) == 12616:
        return 'ㄵ'
    elif ord(a) == 12596 and ord(b) == 12622:
        return 'ㄶ'
    elif ord(a) == 12601 and ord(b) == 12593:
        return 'ㄺ'
    elif ord(a) == 12601 and ord(b) == 12609:
        return 'ㄻ'
    elif ord(a) == 12601 and ord(b) == 12610:
        return 'ㄼ'
    elif ord(a) == 12601 and ord(b) == 12613:
        return 'ㄽ'
    elif ord(a) == 12601 and ord(b) == 12620:
        return 'ㄾ'
    elif ord(a) == 12601 and ord(b) == 12621:
        return 'ㄿ'
    elif ord(a) == 12601 and ord(b) == 12622:
        return 'ㅀ'
    elif ord(a) == 12610 and ord(b) == 12613:
        return 'ㅄ'
    else:
        return '0'

def ssangmoum(a,b):
    if ord(a) == 12631 and ord(b) == 12623:
        return 'ㅘ'
    elif ord(a) == 12631 and ord(b) == 12624:
        return 'ㅙ'
    elif ord(a) == 12631 and ord(b) == 12643:
        return 'ㅚ'
    elif ord(a) == 12636 and ord(b) == 12627:
        return 'ㅝ'
    elif ord(a) == 12636 and ord(b) == 12628:
        return 'ㅞ'
    elif ord(a) == 12636 and ord(b) == 12643:
        return 'ㅟ'
    elif ord(a) == 12641 and ord(b) == 12643:
        return 'ㅢ'
    else:
        return '0'
def changeName(b):
    finalName = ''
    a = []
    a += b
    lenOfNoname = len(a)
    print(lenOfNoname)
    j=-1
    while (1):          # '<3' : 자음이면, ==3 : 모음이면 ==2 : 된소리 ㄸㅉㅃ이면
        j+=1
        print(j)
        print(a)
        temp = []
        if j>=len(a):
            break
        if jaummoum(a[j])<3:
            if j+1 >= len(a):
                break
            elif jaummoum(a[j+1])<3:
                if j+2 >= len(a):
                    temp += ssangjaum(a[j], a[j + 1])
                    if temp[0] != '0' and j!=0:
                        a[j] = temp[0]
                        del a[j + 1]
                    break
                elif jaummoum(a[j+2]) <3:
                    temp += ssangjaum(a[j],a[j+1])
                    if temp[0] != '0':
                        a[j] = temp[0]
                        del a[j+1]

            elif jaummoum(a[j+1])==3:
                if j+2 >= len(a):
                    a[j] = hgtk.letter.compose(a[j],a[j+1])
                    del a[j+1]
                    break
                elif jaummoum(a[j + 2]) == 2:
                    a[j] = hgtk.letter.compose(a[j], a[j + 1])
                    del a[j + 1]

                elif jaummoum(a[j+2])<3:
                    if j+3>= len(a):
                        a[j] = hgtk.letter.compose(a[j],a[j+1],a[j+2])
                        del a[j+1]
                        del a[j+1]
                        break

                    elif jaummoum(a[j+3])<3:
                        if j+4 >= len(a):
                            temp += ssangjaum(a[j+2], a[j+3])
                            if temp[0] != '0':
                                a[j+2] = temp[0]
                                del a[j+3]
                            a[j] = hgtk.letter.compose(a[j], a[j + 1], a[j + 2])
                            del a[j + 1]
                            del a[j + 1]
                            break
                        elif jaummoum(a[j+4]) <3:
                            temp += ssangjaum(a[j + 2], a[j + 3])
                            if temp[0] != '0':
                                a[j+2] = temp[0]
                                del a[j+3]
                        print('A'+str(j))
                        a[j] = hgtk.letter.compose(a[j],a[j+1],a[j+2])
                        del a[j+1]
                        del a[j+1]
                    elif jaummoum(a[j+3])==3:
                        a[j]=hgtk.letter.compose(a[j],a[j+1])
                        del a[j+1]
                elif jaummoum(a[j+2])==3:
                    temp += ssangmoum(a[j+1], a[j + 2])
                    if temp[0] != '0':
                        a[j+1] = temp[0]
                        del a[j + 2]
                        lenOfNoname -= 1
                        j -= 1
                    else:
                        a[j] = hgtk.letter.compose(a[j],a[j+1])
                        del a[j+1]
    finalName = a
    return finalName