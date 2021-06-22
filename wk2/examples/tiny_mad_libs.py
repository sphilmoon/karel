# adjective noun verb
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

def main():
    adj = input("Please type an adjective and press ENTER. ")
    noun = input("Please type an noun and press ENTER. ")
    verb = input("Please type an verb and press ENTER. ")
    print(SENTENCE_START, adj, noun, verb, "!")

if __name__ == "__main__":
    main()
