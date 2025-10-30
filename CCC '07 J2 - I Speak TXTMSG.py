yes = {
    "CU": "see you",
    ":-)" : "I'm happy",
    ":-(" : "I'm unhappy",
    ";-)" : "wink",
    ":-P" : "stick out my tongue",
    "(~.~)": "sleepy",
    "TA" : "totally awesome",
    "CCC" : "Canadian Computing Competition",
    "CUZ" : "because",
    "TY": "thank-you",
    "YW" : "you're welcome",
    "TTYL" : "talk to you later"
}
done = False
while done is False:
    a = input()
    if a in yes.keys():
        print(yes[a])
        if a == "TTYL":
            done = True
    else:
        print(a)