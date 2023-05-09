#disassembler for python bytecode
def add(x,y):
    return x+y
import dis
# print(dis.dis(add))


def do_sth(delta_seconds):
    if delta_seconds<11*24*3600:
        return

print(dis.dis(do_sth))


def sort_user_inf(users):
    def key_func(username):
        age=users[username]
        return age if age is not None else float('inf')
    return sorted(users.keys(),key=key_func)
users={"tom":19,"jenny":13,"jack":None,"andrew":43}
print(sort_user_inf(users))