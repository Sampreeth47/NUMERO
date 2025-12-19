print('\t\t\t\033[94mNUMERO\033[0m')
n = input('\033[97mName : ')
print(f'\nನಮಸ್ಕಾರ {n}!! Welcome to NUMERO.....')
print("\033[91mಎಚ್ಚರಿಕೆ: ಬುದ್ಧಿವಂತರಿಗೆ ಮಾತ್ರ!!\n")


def select_level(fu):
    def wrapper():
        print('Select The Level: \nE.\033[32mEasy\033[0m \nM.\033[33mMedium\033[0m \nH.\033[31mHard\033[0m')
        f = False
        while f == False:
            c = input().lower()
            match c:
                case 'e' | 'easy':
                    fu('e')
                    f = True
                case 'm' | 'medium':
                    fu('m')
                    f = True
                case 'h' | 'hard':
                    fu('h')
                    f = True
                case _:
                    print('Invalid input please try again!!')

    return wrapper


def topic():
    f = False
    while f == False:
        print(
            '\033[97mList of Topics : \n1. Algebra \n2. Limits & Derivatives \n3. Integrals \n4. Vectors \n5. Permutation and combination \n6. Complex numbers \n7. Trigonometry \n8. Exit')
        i = input('Choose a topic(number) : ')
        print()
        match i:
            case '1':
                Algebra()
                f = True
            case '2':
                Limits_Derivatives()
                f = True
            case '3':
                Integrals()
                f = True
            case '4':
                Vectors()
                f = True
            case '5':
                Permutation_Combination()
                f = True
            case '6':
                Complex_Numbers()
                f = True
            case '7':
                Trigonometry()
                f = True
            case '8':
                print("                 \033[33mಧನ್ಯವಾದಗಳು\033[0m")
                print(f'        Thank you for playing {n}!!')
                print("                 \U0001F64F\033[31mಶುಭಂ\033[0m\U0001F64F")
                f = True
                return
            case _:
                print('Invalid input please try again')


def question_structure(t, a, b, a1, a2, l, h1, h2):
    f = False
    while f == False:
        print(f'Question 1:\n{a}')
        ans = input('Answer : ')
        if ans == a1.strip():
            print('\u2705 \033[32mCorrect\033[0m\n')
            z = False
            while z == False:
                print('Do you want to attend the next question(yes/no)?')
                i = input().lower()
                print()
                if i == 'yes':
                    x = False
                    while x == False:
                        print(f'Question 2 : \n{b}')
                        an = input('Answer : ')
                        print()
                        if an == a2.strip():
                            print('\u2705 \033[32mCorrect\033[0m')
                            print(f'Excellent you have cleared all the questions of {t} in {l} level!!\n')
                            print()
                            topic()
                            x = True
                        else:
                            print('\u274C \033[31mIncorrect\033[0m\n')
                            y = False
                            while y == False:
                                print('Do you want to:\n1. Try again\n2. See Hint\n3. See Solution\n4. Change Topic')
                                inp = input()
                                print()
                                match inp:
                                    case '1':
                                        y = True
                                    case '2':
                                        print(f'Hint: {h2}\n')
                                        y = True
                                    case '3':
                                        print(f'Solution: {a2}\n')
                                        y = True
                                        f = True
                                        topic()
                                    case '4':
                                        f = True
                                        y = True
                                        topic()
                                    case _:
                                        print('Invalid input please try again\n')
                    z = True
                elif i == 'no':
                    topic()
                    z = True
                else:
                    print('Invalid input please try again\n')
            f = True
        else:
            print('\u274C \033[31mIncorrect\033[0m\n')
            y = False
            while y == False:
                print('Do you want to:\n1. Try again\n2. See Hint\n3. See Solution\n4. Change Topic')
                inp = input()
                print()
                match inp:
                    case '1':
                        y = True
                    case '2':
                        print(f'Hint: {h1}\n')
                        y = True
                    case '3':
                        print(f'Solution: {a1}\n')
                        y = True
                        f = True
                        topic()
                    case '4':
                        f = True
                        y = True
                        topic()
                    case _:
                        print('Invalid input please try again\n')


@select_level
def Algebra(level):
    t = 'Algebra'
    if level == 'e':
        a = 'Evaluate : x\u00b2+1 for 𝑥=2.'
        a1 = '5'
        b = 'If 2y-8=0, then find y.'
        a2 = '4'
        l = 'easy'
        h1 = 'Substitute the given value into the expression and simplify.'
        h2 = 'Rearrange the equation to isolate y and solve.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'm':
        a = 'Solve for x: 7(x+2)−5=3x+21'
        a1 = '3'
        b = 'y⁴ - 2y³ - 13y² + 14y + 24 = 0. Find the sum of solutions of y.'
        a2 = '2'
        l = 'medium'
        h1 = 'Expand and simplify the equation to isolate x.'
        h2 = 'Use factorization or the Rational Root Theorem to find the roots and sum them.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'h':
        a = 'If x² + px + q = 0 has roots α and β, find the sum of p and q when α³ + β³ = 407 and α² + β² = 65.'
        a1 = '17'
        b = 'if a+b+c=5, ab+bc+ca=7, and abc=3 find the value of a³ + b³ + c³.'
        a2 = '29'
        l = 'hard'
        h1 = 'Use the relationships between the coefficients and the roots of the quadratic equation to express α³ + β³ in terms of p and q.'
        h2 = 'Use the identity a³ + b³ + c³ - 3abc = (a + b + c)( (a + b + c)² - 3(ab + bc + ca) ) to find a³ + b³ + c³.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    pass


@select_level
def Limits_Derivatives(level):
    t = 'Limits and Derivatives'
    if level == 'e':
        a = "Find the Limit: lim(x→2) (3x + 4)"
        a1 = '10'
        b = "Find f′(25) for f(x) = x²"
        a2 = '50'
        l = 'easy'
        h1 = 'Substitute the value of x into the expression and simplify.'
        h2 = 'Differentiate the function and then substitute x=25 to find f′(25).'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'm':
        a = "Find the Limit: lim(x→0) (sin(x) / x)"
        a1 = '1'
        b = "Find f′(7) if f(x) = 3x³ − 5x + 7"
        a2 = '436'
        l = 'medium'
        h1 = 'Use the standard limit result that lim(x→0) (sin(x) / x) = 1.'
        h2 = 'Differentiate the function using the power rule and then substitute x=7 to find f′(7).'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'h':
        a = "If l=lim(x→0) (sin(5x) − 5x) / x³. Find l"
        a1 = '-21'
        b = "Find f′(1) for f(x) = x⁵·e³x·sin(2x)"
        a2 = '111'
        l = 'hard'
        h1 = 'Use L’Hôpital’s Rule to evaluate the limit by differentiating the numerator and denominator until a determinate form is obtained.'
        h2 = 'Differentiate the function using the product rule and chain rule as necessary, then substitute x=1 to find f′(1).'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    pass


@select_level
def Integrals(level):
    t = 'Integration'
    if level == 'e':
        a = "f(x)=∫(3x²−4x+5)dx with limits x=0 to x=2"
        a1 = '10'
        b = "f(x)=∫(sin(x)+ cos(x))dx with lmits x=0 to x=π"
        a2 = '2'
        l = 'easy'
        h1 = 'Integrate the polynomial function and then evaluate it at the given limits.'
        h2 = 'Integrate the trigonometric functions separately and then evaluate at the given limits.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'm':
        a = "f(x)=∫eᶜᵒˢˣsinx for x=0 to x=2π"
        a1 = '0'
        b = "If I=∫2x/x²+1 for x=1 to x=3, find the value of eᴵ."
        a2 = '5'
        l = 'medium'
        h1 = 'Use substitution method to solve the integral and then evaluate it at the given limits.'
        h2 = 'Use substitution method to solve the integral and then evaluate it at the given limits.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'h':
        a = "f(x)=∫sin³x/cos⁵x for x=0 to x=π/4(Enter the decimal value)."
        a1 = '0.5'
        b = "f(x)=∫(xˣ+(1-x)¹⁻ˣ)/x"
        a2 = '2'
        l = 'hard'
        h1 = 'Use trigonometric identities to simplify the integrand before integrating and evaluating at the limits.'
        h2 = 'Split the integral into two parts and evaluate each separately before combining the results.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    pass


@select_level
def Vectors(level):
    t = 'Vectors'
    if level == 'e':
        a = "Find the magnitude of vector (3,4)?"
        a1 = '5'
        b = "Find the dot product of (2,3) and (3,4)?"
        a2 = '11'
        l = 'easy'
        h1 = 'Use the Pythagorean theorem to calculate the magnitude of the vector.'
        h2 = 'Use the formula for dot product: a·b = ax * bx + ay * by.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'm':
        a = "Find the resultant of two vectors having magnitude of 9 and 5 but act in opposite direction?"
        a1 = '4'
        b = "Find the resultant of two vectors having magnitude of 9 and 5 and act in same direction?"
        a2 = '14'
        l = 'medium'
        h1 = 'Subtract the smaller magnitude from the larger magnitude to find the resultant vector.'
        h2 = 'Add the magnitudes of the two vectors to find the resultant vector.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'h':
        a = "A vector (12,16) is inclined at an angle 60(degree) to the horizontal direction find the horizontal  components?"
        a1 = '10'
        b = "If vector has magnitude 25 and makes one component is 7, find the other component?"
        a2 = '24'
        l = 'hard'
        h1 = 'Use the cosine of the angle to find the horizontal component: horizontal component = magnitude * cos(angle).'
        h2 = 'Use the Pythagorean theorem to find the other component: other component = √(magnitude² - given component²).'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    pass


@select_level
def Permutation_Combination(level):
    t = 'Permutation and Combination'
    if level == 'e':
        a = "How many ways can you arrange the letters of the word 'DOG'?"
        a1 = '6'
        b = "How many ways can you choose 2 objects from 4?"
        a2 = '6'
        l = 'easy'
        h1 = 'Use the formula for permutations: n!/(n-r)! where n is total items and r is items to arrange.'
        h2 = 'Use the formula for combinations: n!/(r!(n-r)!) where n is total items and r is items to choose.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'm':
        a = "How many 3-digit numbers can be formed using digits 1,2,3,4 without repetition?"
        a1 = '24'
        b = "In how many ways can 5 people sit in a row?"
        a2 = '120'
        l = 'medium'
        h1 = 'Use the formula for permutations: n!/(n-r)! where n is total items and r is items to arrange.'
        h2 = 'Use the factorial of the number of people to find the arrangements: n!.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'h':
        a = "In how many ways can 5 boys and 5 girls be seated alternately in a row?"
        a1 = '28800'
        b = "How many ways can you distribute 5 identical balls into 3 distinct boxes?"
        a2 = '21'
        l = 'hard'
        h1 = 'Count how many ways the 5 boys can be arranged among their fixed positions.'
        h2 = 'Use the "stars and bars" combinatorial method to find the number of distributions.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    pass


@select_level
def Complex_Numbers(level):
    t = "Complex Numbers"
    if level == 'e':
        a = "Find the modulus of (3 + 4i)"
        a1 = '5'
        b = "What is the real part of (6 + 9i)?"
        a2 = '6'
        l = 'easy'
        h1 = 'Use the formula for modulus: |a + bi| = √(a² + b²).'
        h2 = 'The real part of a complex number a + bi is simply a.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'm':
        a = "Find the modulus of (6 - 8i)"
        a1 = '10'
        b = 'Find the real part of ( (3 + 4i)(5 − 2i)).'
        a2 = '23'
        l = 'medium'
        h1 = 'Use the formula for modulus: |a + bi| = √(a² + b²).'
        h2 = 'Multiply the complex numbers using distributive property and then identify the real part.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'h':
        a = "Simplify: ((2 + 5i)(3 - i)) / (1 + 2i) and find the sum of real and imaginary part"
        a1 = '5'
        b = 'Find the imaginary part of (4 + 3i)(2 - 7i)(1 + i).'
        a2 = '-170'
        l = 'hard'
        h1 = 'Multiply the complex numbers in the numerator and then divide by the complex number in the denominator using conjugates.'
        h2 = 'Multiply the complex numbers step by step and then identify the imaginary part.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    pass


@select_level
def Trigonometry(level):
    t = 'Trigonometry'
    if level == 'e':
        a = "sin(30ᵒ)+cos(0ᵒ)+√3cos(30ᵒ)"
        a1 = '3'
        b = "cos⁻¹(0)+sin⁻¹(1/2)-sin⁻¹(1)"
        a2 = '30'
        l = 'easy'
        h1 = 'Use the known values of sine and cosine for standard angles.'
        h2 = 'Use the inverse trigonometric function values for standard angles.'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'm':
        a = "If sin(x)+cos(x)=√2, then find the value of sin(x)cos(x)."
        a1 = '0.5'
        b = "[sin(20ᵒ)cos(40ᵒ)+sin(40ᵒ)cos(20ᵒ)]/sin(60ᵒ)​"
        a2 = '1'
        l = 'medium'
        h1 = 'Square the given expression and use the identity sin²x + cos²x = 1.'
        h2 = 'Use the sine addition formula: sin(A)cos(B) + cos(A)sin(B) = sin(A + B).'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    elif level == 'h':
        a = "[sin(75ᵒ)−sin(15ᵒ)]/[cos(15ᵒ)−cos(75ᵒ)]​​"
        a1 = '1'
        b = "Given sin(x)+cos(x)=1 Find sin³(x)+cos³(x)"
        a2 = '1'
        l = 'hard'
        h1 = 'Use the sine subtraction formula: sin(A) - sin(B) = 2cos((A + B)/2)sin((A - B)/2).'
        h2 = 'Use the identity a³ + b³ = (a + b)(a² - ab + b²) and substitute a = sin(x) and b = cos(x).'
        question_structure(t, a, b, a1, a2, l, h1, h2)
    pass


f = False
while f == False:
    print(
        '\033[97mList of Topics : \n1. Algebra \n2. Limits & Derivatives \n3. Integrals \n4. Vector algebra \n5. Permutation and combination \n6. Complex numbers \n7. Trigonometry')
    print('\n7 Topics!! \033[93m#ThalaForAReason')
    print()
    c = input('\033[31mChoose a topic(number) :\033[0m ')
    print()
    match c:
        case '1':
            Algebra()
            f = True
        case '2':
            Limits_Derivatives()
            f = True
        case '3':
            Integrals()
            f = True
        case '4':
            Vectors()
            f = True
        case '5':
            Permutation_Combination()
            f = True
        case '6':
            Complex_Numbers()
            f = True
        case '7':
            Trigonometry()
            f = True
        case _:
            print('Invalid input please try again!!')

