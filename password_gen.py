#Author: Paras Kumar
#Title: Password Generator (Week-1)

import random
import string
import argparse 

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
specials = string.punctuation   #Adding all possible characters for password in separate lists

parser = argparse.ArgumentParser()

def pass_gen(length, use_upper, use_lower, use_digits, use_specials):
    
    sample_pass = []    #Making a empty list for the result password
    if use_upper:
        sample_pass.extend(list(upper))
    if use_lower:
        sample_pass.extend(list(lower))
    if use_digits:
        sample_pass.extend(list(digits))
    if use_specials:
        sample_pass.extend(list(specials))
    
    result_pass = "".join(random.sample(sample_pass, length))   #Generating password from sample_pass and joining it
    
    return result_pass


def main():
    parser.add_argument("-l", "--length", type = int, default = 16, help= "This refers to the length of the password.")
    parser.add_argument("-u", "--upper", action="store_true", help="This gives the option to include the uppercase alphabets in the password.")
    parser.add_argument("-w", "--lower", action="store_true", help="This gives the option to include the lowercase alphabets in the password.")
    parser.add_argument("-d", "--digit", action="store_true", help="This gives the option to include the digits in the password.")
    parser.add_argument("-s", "--special", action="store_true", help="This gives the option to include the special characters in the password.")

    args = parser.parse_args()
    
    try:
        password = pass_gen(args.length, args.upper, args.lower, args.digit, args.special)
        print(f"Generated Password: {password}")
        
        if args.length > 16 and args.length <= 32 and args.upper and args.lower and args.digit and args.special:
            print("Security: Very Strong")
        elif args.length <= 16 and args.upper and args.lower and args.digit and args.special:
            print("Security: Strong")
        elif args.length >= 8 and args.length < 16 and args.lower and args.upper or args.digit or args.special:
            print("Security: Weak\nTip: Try increasing length of password")
        else:
            print("Security: Very Weak\nTip: Try adding more complexity like digits and special symbols")
    
    except ValueError as e:     #Handling the Value Error that can be raised if no commands are entered by the user
        print("Kindly enter at least one command for generating password!")
    
if __name__ == "__main__":
    main()