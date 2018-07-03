print("Oh hi Mark")

print("The square of two is %(sq)s, and the type of 2 and 4.5 are %(t)s and %(f)s respectively." % {'sq': 2**2, 't': type(2), 'f': type(4.5)})

print("What you didn't expect is that the type may depend on how you write a fraction, look at this: 4/2 is %(f)s and 4//2 is %(i)s" % {'f': type(4/2), 'i': type(4//2)})

print("It also happens if the module of the division is not 0, like 8//3. This is of type %(i)s" % {'i': type(8//3)})

print("This is also funny, look at the type of 2, %(i)s, and 2., %(f)s" % {'i': type(2), 'f': type(2.)})

sentence = "Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to them"

print("The lenght of '%(s)s' is %(l)s characters, and the first 9 characters are %(c)s" % {'s': sentence, 'l': len(sentence), 'c': sentence[:8]})

print(2+float("3.5"))

print("Let's see how boolean operations work: not(2) is %(b1)s, not(None) is %(b2)s, 2 and '' is '%(b3)s', 'hello' and 2 is %(b4)s, '' and '2' is '%(b5)s'" % {'b1': not(2), 'b2': not(None), 'b3': 2 and "", 'b4': ("hello" and 2), 'b5': ("" and 2)})

print("Let's check now the or operations: '' or 2 is %(b1)s, 2 or '' is %(b2)s, 2 or 3 is %(b3)s, 3 or 2 is %(b4)s" % {'b1': "" or 2, 'b2': 2 or "", 'b3': 2 or 3, 'b4': 3 or 2 })

print("Sí") if True else print("No")

