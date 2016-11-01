import praw

r = praw.Reddit("This That 1.1 by /u/someperson101")
r.login()

def check_condition(c):
    if c.body.startswith("This. ") or c.body == "This.":
        return True

def bot_action(c):
    try:
        c.reply("That.")
        print("A this was thatted. (Let's hope for sweet, sweet karma.)")
    except praw.errors.RateLimitExceeded:
        print("Oop, going too fast. Or maybe I'm banned.")
    except Exception:
        print("Oh, something went wrong!")
        time.sleep(60)

for c in praw.helpers.comment_stream(r, 'all'):
    if check_condition(c):
        bot_action(c)
