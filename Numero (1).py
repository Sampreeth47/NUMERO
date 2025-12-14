print('\t\t\t\033[94mNUMERA\033[0m')
n=input('\033[97mName : ')
print(f'ನಮಸ್ಕಾರ {n}!! Welcome to NUMERA.....')
print("\033[91mಎಚ್ಚರಿಕೆ: ಬುದ್ಧಿವಂತರಿಗೆ ಮಾತ್ರ!!")

print('\n7 Topics!! \033[93m#ThalaForAReason')

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
        i=input('Choose a topic(number) : ')
        print()
        match i:
            case '1':
                Algebra()
                f=True
            case '2':
                Limits_Derivatives()
                f=True
            case '3':
                Integrals()
                f=True
            case '4':
                Vectors()
                f=True
            case '5':
                Permutation_Combination()
                f=True
            case '6':
                Complex_Numbers()
                f=True
            case '7':
                Trigonometry()
                f=True
            case '8':
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
        ans=input('Answer : ')
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
                        an=input('Answer : ')
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
        a1='5'
        b='If 2y-8=0, then find y.'
        a2='4'
        l='easy'
        question_structure(t,a,b,a1,a2,l)
    elif level=='m':
        a='Solve for x: 7(x+2)−5=3x+21'
        a1='3'
        b='y⁴ - 2y³ - 13y² + 14y + 24 = 0. Find the sum of solutions of y.'
        a2='2'
        l='medium'
        question_structure(t,a,b,a1,a2,l)
    elif level=='h':
        a='If x² + px + q = 0 has roots α and β, find the sum of p and q when α³ + β³ = 407 and α² + β² = 65.'
        a1='17'
        b='if a+b+c=5, ab+bc+ca=7, and abc=3 find the value of a³ + b³ + c³.'
        a2='29'
        l='hard'
        question_structure(t,a,b,a1,a2,l)
    pass

@select_level

def Limits_Derivatives(level):
    t='Limits_Derivatives'
    if level=='e':
        a="Find the Limit: lim(x→2) (3x + 4)"
        a1='10'
        b= "Find f′(25) for f(x) = x²"
        a2='625'
        l='easy'
        question_structure(t,a,b,a1,a2,l)       
    elif level=='m':
        a="Find the Limit: lim(x→0) (sin(x) / x)"
        a1='1'
        b= "Find f′(7) if f(x) = 3x³ − 5x + 7"
        a2='436'
        l='medium'
        question_structure(t,a,b,a1,a2,l)
    elif level=='h':
        a="If l=lim(x→0) (sin(5x) − 5x) / x³. Find l"
        a1='-21'
        b="Find f′(1) for f(x) = x⁵·e³x·sin(2x)"
        a2='111'
        l='hard'
        question_structure(t,a,b,a1,a2,l)
    pass

def Integrals(level):
    t='Integration'
    if level=='e':
        a="f(x)=∫(3x²−4x+5)dx with limits x=0 to x=2"
        a1='10'
        b="f(x)=∫(sin(x)+ cos(x))dx with lmits x=0 to x=π"
        a2='2'
        l='easy'
        question_structure(t,a,b,a1,a2,l)
    elif level=='m':
        a="f(x)=∫eᶜᵒˢˣsinx for x=0 to x=2π"
        a1='0'
        b= "f(x)=∫2x/x²+1 for x=1 to x=3(Write in terms ln)"
        a2='ln(5)'
        l='medium'
        question_structure(t,a,b,a1,a2,l)
    elif level=='h':
        a="f(x)=∫sin³x/cos⁵x for x=0 to x=π/4(Enter the decimal value)"
        a1='0.25'
        b="f(x)=∫(xˣ+(1-x)¹⁻ˣ)/x"
        a2='2'
        l='hard'
        question_structure(t,a,b,a1,a2,l)
    pass
    pass
@select_level

def Vectors(level):
    t='vectors'
    if level=='e':
        a="Find the magnitude of vector (3,4)?"
        a1='5'
        b="Find the dot product of (2,3) and (3,4)?"
        a2='11'
        l='easy'
        question_structure(t,a,b,a1,a2,l)
    elif level=='m':
        a="Find the resultant of two vectors having magnitude of 9 and 5 but act in opposite direction?"
        a1='4'
        b= "Find the resultant of two vectors having magnitude of 9 and 5 and act in same direction?"
        a2='14'
        l='medium'
        question_structure(t,a,b,a1,a2,l)
    elif level=='h':
        a="A vector (12,16) is inclined at an angle 60(degree) to the horizontal direction find the horizontal  components?"
        a1='10'
        b="If vector has magnitude 25 and makes one component is 7, find the other component?"
        a2='24'
        l='hard'
        question_structure(t,a,b,a1,a2,l)
    pass

@select_level

def Permutation_Combination(level):
    t='vectors'
    if level=='e':
        a="How many ways can you arrange the letters of the word 'DOG'?"
        a1='6'
        b="How many ways can you choose 2 objects from 4?"
        a2='6'
        l='easy'
        question_structure(t,a,b,a1,a2,l)
    elif level=='m':
        a="How many 3-digit numbers can be formed using digits 1,2,3,4 without repetition?"
        a1='24'
        b= "In how many ways can 5 people sit in a row?"
        a2='120'
        l='medium'
        question_structure(t,a,b,a1,a2,l)
    elif level=='h':
        a= "In how many ways can 5 boys and 5 girls be seated alternately in a row?"
        a1='28800'
        b="How many ways can you distribute 5 identical balls into 3 distinct boxes?"
        a2='21'
        l='hard'
        question_structure(t,a,b,a1,a2,l)      
    pass

@select_level

def Complex_Numbers(level):
    t="Complex_Numbers"
    if level=='e':
        a= "Find the modulus of (3 + 4i)"
        a1='5'
        b="What is the real part of (6 + 9i)?"
        a2='6'
        l='easy'
        question_structure(t,a,b,a1,a2,l)
    elif level=='m':
        a="Find the modulus of (6 - 8i)"
        a1='10'
        b='Find the real part of ( (3 + 4i)(5 − 2i)).'
        a2='23'
        l='medium'
        question_structure(t,a,b,a1,a2,l)
    elif level=='h':
        a="Simplify: ((2 + 5i)(3 - i)) / (1 + 2i) and find the sum of real and imaginary part"
        a1='5'
        b='Find the imaginary part of (4 + 3i)(2 - 7i)(1 + i).'
        a2='-170'
        l='hard'
        question_structure(t,a,b,a1,a2,l)
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










