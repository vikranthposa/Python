open_br = ['(' , '{', '[']
close_br = [')', '}', ']']

def print_err_str(que, cur_ch, cur_idx):
    if cur_ch:
        if len(que):
            err_tup = que[0]
            if((cur_ch == '}') and (err_tup[0]=='{')):
                err_tup = que[1]
            elif((cur_ch == ']') and (err_tup[0]=='[')):
                err_tup = que[1]
            elif((cur_ch == ')') and (err_tup[0]=='(')):
                err_tup = que[1]
        else:
            err_tup = (cur_ch, cur_idx)
    else:
        err_tup = que[0]

    print("Invalid Expression with character " + str(err_tup[0]) + ' at position ' + str(err_tup[1]+1))


def validate_exp(exp):
    cur_idx = 0
    queue = []
    for cur_idx in range(len(exp)):
        cur_ch = exp[cur_idx]
        if cur_ch in open_br:
            queue.append((cur_ch,cur_idx))
        elif cur_ch in close_br:
            if len(queue):
                last_ch = queue[-1]
                if(cur_ch == '}'):
                    if (last_ch[0] != '{'):
                        return(print_err_str(queue,cur_ch, cur_idx))
                elif (cur_ch == ')'):
                    if (last_ch[0] != '('):
                        return(print_err_str(queue,cur_ch, cur_idx))
                elif (cur_ch == ']'):
                    if (last_ch[0] != '['):
                        return(print_err_str(queue,cur_ch, cur_idx))
                queue.pop()
            else:
                return(print_err_str(queue,cur_ch, cur_idx))

    if len(queue):
        return(print_err_str(queue, None, None))
    else:
        print("Valid expression")

ip_exp = '{{{)}}}([ds'
validate_exp(ip_exp)


