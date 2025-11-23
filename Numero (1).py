print('\t\t\t\033[94mNUMERA\033[0m')
n=input('\033[97mName : ')
print(f'ನಮಸ್ಕಾರ {n}!! Welcome to NUMERA.....')
print("\033[91mಎಚ್ಚರಿಕೆ: ಬುದ್ಧಿವಂತರಿಗೆ ಮಾತ್ರ!!")

print('\033[97mList of Topics : \n1. Algebra \n2. Limits & Derivatives \n3. Integrals \n4. Vector algebra \n5. Permutation and combination \n6. Complex numbers \n7. Trigonometry')
print('\n7 Topics!! \033[93m#ThalaForAReason')

print('\033[97m')
c=int(input('Choose a topic(number) : '))
print()


def select_level(fu):
    def wrapper():
        print('Select The Level: \nE.\033[32mEasy\033[0m \nM.\033[33mMedium\033[0m \nH.\033[31mHard\033[0m')
        c=input().lower()
        f=False
        while f==False:
            match c:
                case 'e' | 'easy':
                    fu('e')
                    f=True
                case 'm' | 'medium':
                    fu('m')
                    f=True
                case 'h' | 'hard':
                    fu('h')
                    f=True
                case _:
                    print('Invalid input please try again!!')
        
    return wrapper

def topic():
    f=False
    while f==False:
        print('\033[97mList of Topics : \n1. Algebra \n2. Limits & Derivatives \n3. Integrals \n4. Vectors \n5. Permutation and combination \n6. Complex numbers \n7. Trigonometry \n8. Exit')
        i=int(input('Choose a topic(number) : '))
        print()
        match i:
            case 1:
                Algebra()
                f=True
            case 2:
                Limits_Derivatives()
                f=True
            case 3:
                Integrals()
                f=True
            case 4:
                Vectors()
                f=True
            case 5:
                Permutation_Combination()
                f=True
            case 6:
                Complex_Numbers()
                f=True
            case 7:
                Trigonometry()
                f=True
            case 8:
                print(f'Thank you for playing {n}!!\n')
                print('                  \U0001F64Fಶುಭಂ\U0001F64F')
                f=True
                return
            case _:
                print('Invalid input please try again')

def question_structure(t,a,b,a1,a2,l):
    f=False
    while f==False:
        print(f'Question 1:\n{a}')
        ans=int(input('Answer : '))
        if ans==a1:                
            print('\u2705 \033[32mCorrect\033[0m\n')
            z=False
            while z==False:
                print('Do you want to attend the next question(yes/no)?')
                i=input().lower()
                print()
                if i=='yes':
                    x=False
                    while x==False:
                        print(f'Question 2 : \n{b}')
                        an=int(input('Answer : '))
                        print()
                        if an== a2:
                            print('\u2705 \033[32mCorrect\033[0m')
                            print(f'Excellent you have cleared all the questions of {t} in {l} level!!\n')
                            print()
                            topic()
                            x=True 
                        else:
                            print('\u274C \033[31mIncorrect\033[0m\n')
                            y=False
                            while y==False:
                                print('Do you want to try again(yes/no)?')
                                j=input().lower()
                                print()
                                if j=='no':
                                    topic()
                                    x=True
                                    y=True
                                elif j=='yes':
                                    y=True
                                else :
                                    print('Invalid input please try again\n')
                    z=True
                elif i=='no':
                    topic()
                    z=True
                else :
                    print('Invalid input please try again\n')
            f=True
        else:
            print('\u274C \033[31mIncorrect\033[0m\n')
            y=False
            while y==False:
                print('Do you want to try again(yes/no)?')
                j=input().lower()
                print()
                if j=='no':
                    topic()
                    f=True
                    y=True
                elif j=='yes':
                        y=True
                else :
                    print('Invalid input please try again\n')

@select_level
def Algebra(level):
    t='Algebra'
    if level=='e':
        a='Evaluate : x\u00b2+1 for 𝑥=2.'
        a1=5
        b='If 2y-8=0, then find y.'
        a2=4
        l='easy'
        question_structure(t,a,b,a1,a2,l)
        
    elif level=='m':
        a='Solve for x: 7(x+2)−5=3x+21'
        a1=3
        b='y⁴ - 2y³ - 13y² + 14y + 24 = 0. Find the sum of solutions of y.'
        a2=2
        l='medium'
        question_structure(t,a,b,a1,a2,l)
    elif level=='h':
        a='If x² + px + q = 0 has roots α and β, find the sum of p and q when α³ + β³ = 407 and α² + β² = 65.'
        a1=17
        b='if a+b+c=5, ab+bc+ca=7, and abc=3 find the value of a³ + b³ + c³.'
        a2=29
        l='hard'
        question_structure(t,a,b,a1,a2,l)
    pass

def Limits_Derivatives():
    pass

def Integrals():
    pass

def Vectors():
    pass

def Permutation_Combination():
    pass

def Complex_Numbers():
    pass

def Trigonometry():
    pass

match c:
    case 1:
        Algebra()
    case 2:
        Limits_Derivatives()
    case 3:
        Integrals()
    case 4:
        Vectors()
    case 5:
        Permutation_Combination()
    case 6:
        Complex_Numbers()
    case 7:
        Trigonometry()

