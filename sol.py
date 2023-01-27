# Written by Asmus Tørsleff
import itertools
import time
start_time = time.time()
smalls = sorted([ (i%10)+1 for i in range(20) ])
print("smalls:", smalls)

def build_n_big_number_comps(smalls, bigs, n):
    number_comps = set()
    if (n != 0):
        bigs_comps = list(itertools.combinations(bigs, n))
    else:
        bigs_comps = [()]

    for number_comp_smalls in itertools.combinations(smalls, 5-n):
        for number_comp_bigs in bigs_comps:
            number_comps.add(encode(number_comp_smalls,number_comp_bigs))
    return number_comps

def encode(smalls, bigs):
    return smalls + bigs

def op(a,b,k):
    if k==0:
        return a+b
    elif k==1:
        return a-b
    elif k==2:
        return a*b
    elif k==3:
        return a/b

mem = dict()
def reachable_targets(number_comp):
    targets = set()    
    if number_comp in mem:
        return mem[number_comp]
    if len(number_comp) < 2:
        mem[number_comp] = targets
        return targets
    if len(number_comp) == 5:
        for x in number_comp:
            if 99<x<1000:
                targets.add(x)
    for (a,b) in itertools.combinations(number_comp, 2):
        new_number_comp = list(number_comp)
        new_number_comp.remove(a)
        new_number_comp.remove(b)
        for k in range(4):
            x = op(a,b,k)
            if x <= 0 or x != int(x):
                continue
            if 99<x<1000:
                targets.add(x)
            new_number_comp.append(x)
            targets = targets.union(reachable_targets(tuple(sorted(new_number_comp))))
            new_number_comp.remove(x)
    mem[number_comp] = targets
    return targets

def count_t(number_comps):
    solved_total = 0
    for comp in sorted(number_comps):
        solved = len(reachable_targets(comp))
        solved_total += solved
    return solved_total


def main():
    #all combinations
    combinations = list(itertools.combinations([i for i in range (11,101)], 4)) 
    #combinations restrained
    combinations = [(i,i+25,i+50,i+75) for i in range(11,26)]
    print("total combinations:", len(combinations))
    for bigs in combinations:
        count_total = 0
        out_of_total = 0
        for n in range(5):
            number_comps = build_n_big_number_comps(smalls, bigs, n)
            count_n_large = count_t(number_comps)
            out_of = len(number_comps)*900
            count_total += count_n_large
            out_of_total += out_of
            percentage = round(100*count_n_large/out_of,1)
            print(bigs,"with",n,"large:",count_n_large,"out of",out_of,"(",percentage,"%",")")
        percentage = round(100*count_total/out_of_total,1)
        print(bigs,"in total:",count_total,"out of",out_of_total,"(",percentage,"%",")")            
main()

print("--- %s seconds ---" % (time.time() - start_time))

