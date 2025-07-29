# %%
from openai import OpenAI
client = OpenAI()
user_in = input("Please enter your question ")

# Generate Python code based on the user's input
user_input = (
    "Now, generate complete Python code for the following question:\n"
    + user_in
    + "\nFormulate logic to find the correct answer to the randomized parameters in the question.\n"
    + "Ensure the return and print statements are in the same format as the assistance responses given above.\n"
)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are an advanced code generator specializing in creating Multiple Choice Questions (MCQs) with dynamic content. Your task is to:\n\n1. Analyze the given sample MCQ, including its question and four options.\n2. Study the sample assistant response provided by the user to understand the preferred coding style.\n3. Generate error-free code that produces a similar question but with randomized parameters (for example, numbers or text) in the question, following the style of the sample response code.\n4. Implement logic to calculate the correct answer based on the randomized values.\n5. Generate four options, including the correct answer and three plausible distractors.\n6. Ensure that the code can be run multiple times to produce unique questions each time.\n\nYour code should:\n- Be free of syntax errors, logical errors, and runtime errors.\n- Adhere to the coding style, structure, and conventions used in the sample assistant response.\n- Use appropriate random number generation for the question parameters.\n- Randomize textual content such as names, objects, or scenarios to increase variability.\n- Implement the mathematical or logical operations required to solve the question.\n- Calculate the correct answer and three incorrect but plausible options.\n- Format the output to display the question and options clearly.\n- Include comments explaining the logic and calculations, if present in the sample response.\n\nProvide the code in the Python programming language as the sample response and ensure it closely follows the given style. Double-check your code for any potential errors before submitting it."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Now, generate complete Python code for the following question:\n        How many zeroes are there at the end of the following product?\n        1x 5x 10x 15 x20 x25 x 30x 35x 40x45 x 50x 55x 60\n        (a) 10 (b) 12\n        (c) 14 (d) 15"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "        import random\n        import math\n        import numpy as np\n        import datetime\n        from fractions import Fraction\n        from datetime import timedelta\n        from itertools import combinations\n        # from nltk.corpus import words\n        from sympy import symbols, Eq, solve\n        from itertools import combinations_with_replacement\n        from itertools import product\n        from collections import defaultdict\n        def f2007():\n            arr=[]\n            x = random.randint(10,15)\n            for _ in range(x):\n                z = 1\n                while z%5!=0:\n                    z = random.randint(1, 100)\n                arr.append(z)\n            arr.sort()\n            ls = str(arr[0])\n            for i in arr:\n                ls += 'x' + str(i)\n            mul = 1\n            cnt = 0\n            for i in arr:\n                mul *= i\n            for i in str(mul):\n                if i == '0':\n                    cnt+=1\n            \n            correct_option = cnt\n            options = [correct_option]\n            i=0\n            while i < 3:\n                offset = random.randint(1, 4) * random.choice([-1, 1])\n                option = (correct_option + offset)\n                if option not in options and option >= 0:\n                    options.append(option)\n                    i+=1\n            random.shuffle(options)\n\n            return [\n                f'How many zeroes are there at the end of the following product ? {ls}',\n                options,\n                correct_option\n            ]\n            \n\n        x = f2007()\n        print(x[0])\n        print('#$5$#')\n        print(*x[1], sep=\"#$5$#\")\n        print('#$5$#')\n        print(x[2])"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Now, generate complete Python code for the following question:\nHow many five-digit prime numbers can\nbe obtained by using all the digits 1, 2,\n3, 4 and 5 without repetition of digits?\n(a) Zero (b) One\n(c) Nine (d) Ten"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "import random\nimport math\nimport numpy as np\nimport datetime\nfrom fractions import Fraction\nfrom datetime import timedelta\nfrom itertools import combinations\n# from nltk.corpus import words\nfrom sympy import symbols, Eq, solve\nfrom itertools import combinations_with_replacement\nfrom itertools import product\nfrom collections import defaultdict\nfrom itertools import permutations\ndef is_prime(n):\n    if n <= 1:\n        return False  # 1 and below are not prime\n    elif n <= 3:\n        return True  # 2 and 3 are prime\n    elif n % 2 == 0 or n % 3 == 0:\n        return False  # Numbers divisible by 2 or 3 are not prime\n    \n    i = 5\n    while i * i <= n:\n        if n % i == 0 or n % (i + 2) == 0:\n            return False  # Numbers divisible by i or i + 2 are not prime\n        i += 6\n    return True  # If no divisor is found, the number is prime\n\ndef f2010():\n    num = random.randint(3, 6)\n    digits = random.sample([1,2,3,4,5,6,7,8,9], num)\n    digits.sort()\n    # print(num, digits)\n    all_comb = list(permutations(digits, num))\n    perms = [int(''.join(map(str, perm))) for perm in all_comb]\n    # print(perms)\n    cnt=0\n    for i in perms:\n        if is_prime(i):\n            cnt+=1\n    correct_option = cnt\n    options = [correct_option]\n    i = 0\n    while i < 3:\n        offset = random.randint(1, 6) * random.choice([-1, 1]) \n        option = correct_option + offset\n        if option not in options and option >= 0: \n            options.append(option)\n            i+=1\n    options.sort()\n\n    return[\n        f'How many {num}-digit prime numbers can be obtained by using all the digits ' + \", \".join(map(str, digits)) +' without repetition of digits ?',\n        options,\n        correct_option\n\n    ]\n\nx = f2010()\nprint(x[0])\nprint('#$5$#')\nprint(*x[1], sep=\"#$5$#\")\nprint('#$5$#')\nprint(x[2])"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Now, generate complete Python code for the following ,question: \nIf you have two straight sticks of length 7.5 feet and 3.25 feet, what is the minimum length you can measure?\n (a) 0.08 foot (b) 0.25 foot (c) 1 foot (d) 3.25 feet"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "import random\nimport math\nimport numpy as np\nimport datetime\nfrom fractions import Fraction\nfrom datetime import timedelta\nfrom itertools import combinations\n# from nltk.corpus import words\nfrom sympy import symbols, Eq, solve\nfrom itertools import combinations_with_replacement\nfrom itertools import product\nfrom collections import defaultdict\nimport math\ndef f2012():\n    # needs work\n    canbe = [(1,2), (1,4), (1,5), (1,10), (1,20), (1,25), (2,5), (2, 100), (1, 50)]\n    x, y = random.choice(canbe)\n\n    options = [a/b for a,b in random.sample(canbe, k=4)]\n    options[random.randint(0,3)] = x/y\n\n    # Calculate GCD/HCF\n    num1 = random.randint(1, 100)\n    num2 = random.randint(1, 100)\n    while math.gcd(num1, num2) != x:\n        num2 = random.randint(1, 100)\n\n    #print(num1, num2)\n\n    den1 = random.randint(1, 100)\n    den2 = random.randint(1, 100)\n\n    while (den1 * den2) // math.gcd(den1, den2) != y:\n        den1 = random.randint(1, 100)\n        den2 = random.randint(1, 100)\n\n    #print(den1, den2)\n\n    correct_question = [num1/den1, num2/den2]\n    #print(correct_question)\n\n    return[\n        f'If you have two straight sticks of length {correct_question[0]} feet and {correct_question[1]} feet, what is the minimum length you can measure?',\n        options,\n        x/y\n    ]\n\nx = f2012()\nprint(x[0])\nprint('#$5$#')\nprint(*x[1], sep=\"#$5$#\")\nprint('#$5$#')\nprint(x[2])"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Now, generate complete Python code for the following ,question: \nOne page is torn from a booklet whose pages are numbered in the usual manner starting from the first page as 1. The sum of the numbers on the remaining pages is 195. The torn page contains which of the following numbers?\nOptions: (a) 5, 6 (b) 7, 8 (c) 9, 10 (d) 11, 12"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "import random\nimport math\nimport numpy as np\nimport datetime\nfrom fractions import Fraction\nfrom datetime import timedelta\nfrom itertools import combinations\n# from nltk.corpus import words\nfrom sympy import symbols, Eq, solve\nfrom itertools import combinations_with_replacement\nfrom itertools import product\nfrom collections import defaultdict\ndef f2014():\n    x = random.randint(15, 30)\n    y = random.randint(2, x-1)\n\n    Sum = (x*(x+1))//2\n    # print(Sum)\n    Sum = Sum - y - (y + 1)\n    # print(Sum)\n\n    correct_option = y\n    options = [(y,y+1)]\n    i=0\n    while i < 3:\n        offset = random.randint(1, 4) * random.choice([-1, 1])\n        option = (correct_option + offset)\n        if (option, option+1) not in options and option >= 2 and option < x:\n            options.append((option, option+1))\n            i+=1\n    random.shuffle(options)\n\n    return[\n        f'One page is torn from a booklet whose pages are numbered, starting from 1. The sum of the numbers on the remaining pages is {Sum}. The torn page contains which of the following numbers?',\n        options, \n        [y, y+1]\n    ]\n\nx = f2014()\nprint(x[0])\nprint('#$5$#')\nprint(*x[1], sep=\"#$5$#\")\nprint('#$5$#')\nprint(x[2])"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Now, generate complete Python code for the following ,question: \nLet A3BC and DE2F be four-digit numbers where each letter represents a different digit greater than 3. If the sum of the numbers is 15,902, then what is the difference between the values of AAA and DDD?\nOptions: (a) 1 (b) 2 (c) 3 (d) 4\n"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "import random\nimport math\nimport numpy as np\nimport datetime\nfrom fractions import Fraction\nfrom datetime import timedelta\nfrom itertools import combinations\n# from nltk.corpus import words\nfrom sympy import symbols, Eq, solve\nfrom itertools import combinations_with_replacement\nfrom itertools import product\nfrom collections import defaultdict\ndef f2016():\n    arr=[0,1,2,3,4,5,6,7,8,9]\n\n    # x1 = random.randint(1000, 9999)\n    # x2 = random.randint(1000, 9999)\n    trea = random.sample(arr[4:], k=6)\n    rew = random.sample(arr[1:], k=2)\n\n    y1, y2 = random.sample(arr[:4], k=2)\n\n    op1 = []\n    op2 = []\n    for i in arr[:4]:\n        if i!=y1:\n            op1.append(i)\n        if i!=y2:\n            op2.append(i)\n\n\n    l1 = ''\n    l2 = ''\n    for i in range(4):\n        if i == y1:\n            l1+=str(rew[0])\n        else:\n            l1+=str(trea.pop())\n\n    for i in range(4):\n        if i == y2:\n            l2+=str(rew[1])\n        else:\n            l2+=str(trea.pop())\n\n    x1=int(l1)\n    x2=int(l2)\n    # print(l1, l2)\n    X1=''\n    X2=''\n    for i in range(4):\n        if i == y1:\n            X1+=l1[i]\n        else:\n            X1+=chr(ord('A')+i)\n\n    for i in range(4):\n        if i == y2:\n            X2+=l2[i]\n        else:\n            X2+=chr(ord('A')+i+4)\n\n    Sum = x1+x2\n    #print(x1, x2, Sum)\n    #print(y1, y2, X1, X2)\n\n    t1 = random.choice(op1)\n    t2 = random.choice(op2)\n\n    correct_option = abs(int(str(x1)[t1])-int(str(x2)[t2]))\n    options = [correct_option]\n    i=0\n    while i < 3:\n        offset = random.randint(1, 4) * random.choice([-1, 1])\n        option = (correct_option + offset)\n        if option not in options and option >=0:\n            options.append(option)\n            i+=1\n    random.shuffle(options)\n\n    return[\n        f'Let {X1} and {X2} be four-digit numbers where each letter represents different digit greater than 3. If the sum of the numbers is {Sum}, then absolute difference between the values of {X1[t1]} and {X2[t2]} ?',\n        options,\n        correct_option\n    ]\n\nx = f2016()\nprint(x[0])\nprint('#$5$#')\nprint(*x[1], sep=\"#$5$#\")\nprint('#$5$#')\nprint(x[2])"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Now, generate complete Python code for the following question: \nThe average marks in English and Hindi are given as follows:\nGirls: Average marks in English = 9, Average marks in Hindi = 8\nBoys: Average marks in English = 8, Average marks in Hindi = T\nOverall average marks: Average marks in English = 8.8, Average marks in Hindi = xxx\nWhat is the value of xxx in the above information?\nOptions: (a) 7.8 (b) 7.6 (c) 7.4 (d) 7.2"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "import random\nimport math\nimport numpy as np\nimport datetime\nfrom fractions import Fraction\nfrom datetime import timedelta\nfrom itertools import combinations\n# from nltk.corpus import words\nfrom sympy import symbols, Eq, solve\nfrom itertools import combinations_with_replacement\nfrom itertools import product\nfrom collections import defaultdict\ndef f2018():\n    arr = [5,6,7,8,9,10,11,12,13,14,15]\n    x = random.sample(arr, k=2)\n    y = random.randint(1,4)\n\n    new_x = []\n    if random.randint(0,1):\n        new_x.append(x[0]+y)\n        new_x.append(x[1]+y)\n    else:\n        new_x.append(x[0]-y)\n        new_x.append(x[1]-y)\n    r = round(random.uniform(1.0, 10.0), 1)\n\n    correct_option = round(r + new_x[0]-x[0],1)\n    options = [correct_option]\n    i=0\n    while i < 3:\n        offset = round(random.uniform(0.0, 0.4), 1) * random.choice([-1, 1])\n        option = round((correct_option + offset),1)\n        if option not in options and option >=0:\n            options.append(option)\n            i+=1\n    random.shuffle(options)\n\n    return[\n        f'Consider the following data,\\n Average marks of Girls in English = {x[0]},\\n Average marks of Girls in Hindi = {new_x[0]},\\n Average marks of Boys in English = {x[1]},\\n Average marks of Boys in Hindi = {new_x[0]},\\n Overall average marks in English ={r},\\n Overall average marks in Hindi = X.\\nWhat is the value of X in the above table ?',\n        options,\n        correct_option\n\n    ]\n\nx = f2018()\nprint(x[0])\nprint('#$5$#')\nprint(*x[1], sep=\"#$5$#\")\nprint('#$5$#')\nprint(x[2])\n"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Now, generate complete Python code for the following question: \nIf in a particular year 12th January is a Sunday, then which one of the following is correct?\nOptions: (a) 15th July is a Sunday if the year is a leap year. (b) 15th July is a Sunday if the year is not a leap year. (c) 12th July is a Sunday if the year is a leap year. (d) 12th July is not a Sunday if the year is a leap year.\n"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "import random\nimport math\nimport numpy as np\nimport datetime\nfrom fractions import Fraction\nfrom datetime import timedelta\nfrom itertools import combinations\n# from nltk.corpus import words\nfrom sympy import symbols, Eq, solve\nfrom itertools import combinations_with_replacement\nfrom itertools import product\nfrom collections import defaultdict\ndef is_leap_year(year):\n    # Leap years are divisible by 4\n    if year % 4 == 0:\n        # Except for years divisible by 100, unless they are also divisible by 400\n        if year % 100 == 0:\n            return year % 400 == 0\n        return True\n    return False\ndef ordinal_suffix(number):\n    if 10 <= number % 100 <= 20:\n        suffix = 'th'\n    else:\n        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')\n    return str(number) + suffix\ndef is_date_and_day_present(year, month, day, day_of_week):\n    # print(year, month, day, day_of_week)\n    try:\n        input_date = datetime.date(year, month, day)\n        input_day_of_week = input_date.strftime(\"%A\")\n        # print(input_day_of_week)\n        return input_day_of_week == day_of_week\n    except ValueError:\n        return False\n    \ndef f2020():\n    month_map = {\n    1: \"January\",\n    2: \"February\",\n    3: \"March\",\n    4: \"April\",\n    5: \"May\",\n    6: \"June\",\n    7: \"July\",\n    8: \"August\",\n    9: \"September\",\n    10: \"October\",\n    11: \"November\",\n    12: \"December\"\n}\n    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']\n    leap_year = ['', 'not ']\n    Y = random.randint(1900, 2050)\n    M = random.randint(1, 12)\n    D = random.randint(1, 28)\n    da = datetime.date(Y, M, D)\n    day = da.strftime(\"%A\")\n    ques = f'If in a particular year {ordinal_suffix(D)} {month_map[M]} is a {day}, then which one of the following is correct ?'\n    options = []\n    \n    while True:\n        M = random.randint(1, 12)\n        D = random.randint(1, 28)\n        day = days_of_week[random.randint(0, 6)]\n        if is_date_and_day_present(Y, M, D, day):\n            if is_leap_year(Y):\n                thing = 0\n                correct_option = f'{ordinal_suffix(D)} {month_map[M]} is a {day} if the year is {leap_year[thing]}a leap year'\n            else:\n                thing = 1\n                correct_option = f'{ordinal_suffix(D)} {month_map[M]} is a {day} if the year is {leap_year[thing]}a leap year'\n            options.append(f'{ordinal_suffix(D)} {month_map[M]} is a {day} if the year is {leap_year[thing]}a leap year')\n            options.append(f'{ordinal_suffix(D)} {month_map[M]} is a {day} if the year is {leap_year[thing^1]}a leap year')\n            break\n\n    while True:\n        M = random.randint(1, 12)\n        D = random.randint(1, 28)\n        day = days_of_week[random.randint(0, 6)]\n        if not is_date_and_day_present(Y, M, D, day):\n            if is_leap_year(Y):\n                thing = 0\n            else:\n                thing = 1\n            options.append(f'{ordinal_suffix(D)} {month_map[M]} is a {day} if the year is {leap_year[thing]}a leap year')\n            options.append(f'{ordinal_suffix(D)} {month_map[M]} is a {day} if the year is {leap_year[thing^1]}a leap year')\n            break     \n    random.shuffle(options)       \n    return[\n        ques,\n        options,\n        correct_option\n    ]\n\nx = f2020()\nprint(x[0])\nprint('#$5$#')\nprint(*x[1], sep=\"#$5$#\")\nprint('#$5$#')\nprint(x[2])"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Now, generate complete Python code for the following question: \nA man walks down the backside of his house straight for 25 meters, then turns to the right and walks 50 meters; then he turns to the left and walks 25 meters again. If his house faces East, what is his direction from the starting point?\nOptions: (a) South-East (b) South-West (c) North-East (d) North-West\n"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "import random\nimport math\nimport numpy as np\nimport datetime\nfrom fractions import Fraction\nfrom datetime import timedelta\nfrom itertools import combinations\n# from nltk.corpus import words\nfrom sympy import symbols, Eq, solve\nfrom itertools import combinations_with_replacement\nfrom itertools import product\nfrom collections import defaultdict\ndef f2031():\n    #directions\n    origin = [0,0]\n    original_origin = origin[:]\n    dist = random.randint(1, 10)*5\n    dist2 = random.randint(1, 10)*5\n    dir = ['North', 'East', 'South', 'West']\n    all_dir = ['South-West', 'West', 'North-West', 'North', \n               'North-East', 'East', 'South-East', 'South']\n    moves=[]\n    # dir of house\n    dir_house = random.choice(dir)\n\n    for dist in [dist, dist2, dist]:\n        x = random.choice(dir)\n        # Can't turn North from North\n        while moves and x == moves[-1]:\n            x = random.choice(dir)\n        moves.append(x)\n\n        if x == 'East':\n            origin[0]+=dist\n        elif x == 'West':\n            origin[0]-=dist\n        elif x == 'North':\n            origin[1]+=dist\n        elif x == 'South':\n            origin[1]-=dist   \n        \n    # print(origin)\n    if original_origin == origin:\n        correct_option = 'Origin'\n    elif original_origin[0]==origin[0]:\n        if original_origin[1] < origin[1]:\n            correct_option = 'North'\n        else:\n            correct_option = 'South'\n    elif original_origin[1]==origin[1]:\n        if original_origin[0] < origin[0]:\n            correct_option = 'East'\n        else:\n            correct_option = 'West'\n    elif original_origin[1] < origin[1]:\n        if original_origin[0] < origin[0]:\n            correct_option = 'North-East'\n        else:\n            correct_option = 'North-West'\n    elif original_origin[1] > origin[1]:\n        if original_origin[0] > origin[0]:\n            correct_option = 'South-West'\n        else:\n            correct_option = 'South-East'\n    else:\n        return 'Error'\n\n    # Rotate as per direction of house\n    for i in range(1, 4):\n        if correct_option != 'Origin' and dir_house == dir[i]:\n            correct_option = all_dir[(all_dir.index(correct_option)+2*i)%8]\n\n    options = random.sample([num for num in all_dir if num != correct_option], k=3) + [correct_option]\n    random.shuffle(options)   \n\n\n    return [\n        f'A man starts his walk from {moves[0]} of his house of {dist} meters, then turns to the {moves[1]} and walks {dist2} meters again; then he turns towards {moves[2]} and again walks {dist} meters. If his house faces to the {dir_house}, what is the direction from the starting point?',\n        options,\n        correct_option\n    ]\n\n\nx = f2031()\nprint(x[0])\nprint('#$5$#')\nprint(*x[1], sep=\"#$5$#\")\nprint('#$5$#')\nprint(x[2])"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": user_input
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=5000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)

# Print the assistant's response
print(response.choices[0].message.content)
