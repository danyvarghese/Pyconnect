class Clause(object):    def __init__(self,mode):        mode = mode.replace("[[", "$[", 100)        mode = mode.replace("]]", "], *", 100)        self.predicate,_,body=mode.replace(" ", "").partition('(')        self.body=body.strip().split(')')    def args(name):        args=[]        if "[" in name.body[0]:            for i in name.body[0].split("["):                if "]" in i:                    ans=split_into_args(i)                    for j in ans:                        if j:                            args.append(j)                else:                    for j in  i.split(","):                        if j:                            args.append(j)        else:            for arg_str in name.body[0].split(','):                if arg_str:                    if arg_str:                        args.append(arg_str)        if "$" in name.body[0]:            return(convert_set_list(args))        else:            return args        def D_1(predicate,args):    head=predicate    start="("    for i in args:        start=start+str(i)+","    body=start[0:-1]+")"    clause=head+body    return clausedef extract_actions(plan_1):    x = plan_1.split("),")    rules = []    for id, i in enumerate(x):                if 'actionType' in i:            string_1 = i+')'        if 'actionParams' in i:            String_2 = i+','+x[id+1]            cord = Clause(String_2).args()            string_4 = []            for j in cord:                string_3= j+')'                string_4.append(Clause(string_3).args()[0])            inst = D_1(Clause(string_1).args()[0],string_4)            rules.append(inst)    rules.reverse()    return rules