### Prompting and Passing

from sys import argv

script, user_name = argv
prompt = '>'

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to askyou a few quiestions.")
print("Do yu like me %s?" % user_name)
likes = input(prompt)

print("Wher do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure wher that is.
And you have a %r computer, Nice.
""" % (likes, lives, computer))

