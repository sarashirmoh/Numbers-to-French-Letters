
# coding: utf-8

# In[ ]:


import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0,       "Integer out of bounds"    
    return list("%03i" % integer)

def french_count():
    f = FST('french')
    '''
    f.add_state('start')
    for i in range(11):
        f.add_state('s' + str(i))
    '''
    f.add_state('start')
    f.add_state('s0')
    f.add_state('s1')
    f.add_state('s10')
    f.add_state('s710')
    f.add_state('s711')
    f.add_state('s712')
    f.add_state('s713')
    f.add_state('s714')
    f.add_state('s11')
    f.add_state('s12')
    f.add_state('s20')
    f.add_state('s21')
    f.add_state('s22')
    f.add_state('s23')
    f.add_state('s30')
    f.add_state('s40')
    f.add_state('s41')
    f.add_state('s42')
    f.add_state('s50')
    f.add_state('s100')
    f.add_state('s101')
    f.add_state('s102')
    f.add_state('s103')
    f.add_state('s200')

    f.initial_state = 'start'

    for ii in xrange(10): 
        
        f.add_arc('start', 'start', [str(0)], ())
        
        f.add_arc('start','s0',[str(0)],[kFRENCH_TRANS[0]])
        
        f.add_arc('s30', 's710', (), ())
        f.add_arc('s50', 's10', (), ())
        f.add_arc('s200', 's100', (), ())
        
        if ii in range(1,10):
            f.add_arc('start', 's1', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('s101', 's103', [str(ii)], [kFRENCH_TRANS[ii]])
            if ii != 1:
                f.add_arc('start', 's200', [str(ii)], [kFRENCH_TRANS[ii] + " " + kFRENCH_TRANS[100]])
        
        if ii == 1:
            f.add_arc('start', 's10', [str(ii)], ())
            f.add_arc('start', 's100', [str(ii)], [kFRENCH_TRANS[100]])
            f.add_arc('s100', 's10', [str(ii)], ())
            
        elif ii in range(2,7):
            f.add_arc('start', 's20', [str(ii)], [kFRENCH_TRANS[int(10*ii)]])
            f.add_arc('s100', 's20', [str(ii)], [kFRENCH_TRANS[int(10*ii)]])
        elif ii == 7:
            f.add_arc('start', 's30', [str(ii)], [kFRENCH_TRANS[60]])
            f.add_arc('s100', 's30', [str(ii)], [kFRENCH_TRANS[60]])
        elif ii == 8:
            f.add_arc('start', 's40', [str(ii)], [kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[20]])
            f.add_arc('s100', 's40', [str(ii)], [kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[20]])
        elif ii == 9:
            f.add_arc('start', 's50', [str(ii)], [kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[20]])
            f.add_arc('s100', 's50', [str(ii)], [kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[20]])
        
        
        if ii in range(0,7):
            f.add_arc('s10', 's11', [str(ii)], [kFRENCH_TRANS[int(ii+10)]])
        else:
            f.add_arc('s10', 's12', [str(ii)], [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[ii]])
        
        
        if ii == 1:
            f.add_arc('s20', 's21', [str(ii)], [kFRENCH_AND + " " + kFRENCH_TRANS[ii]])
            f.add_arc('s40', 's42', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('s710','s711',[str(ii)],[kFRENCH_AND + " " + kFRENCH_TRANS[11]])
        elif ii == 0:
            f.add_arc('s20', 's23', [str(ii)], ())
            f.add_arc('s40', 's41', [str(ii)], ())
            f.add_arc('s710','s712',[str(ii)],[kFRENCH_TRANS[10]])
            
            f.add_arc('s100', 's101', [str(ii)], ())
            f.add_arc('s101', 's102', [str(ii)], ())
            
        else:
            f.add_arc('s20', 's22', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('s40', 's42', [str(ii)], [kFRENCH_TRANS[ii]])
            if ii < 7:
                f.add_arc('s710','s713',[str(ii)],[kFRENCH_TRANS[int(ii+10)]])
            else:
                f.add_arc('s710','s714',[str(ii)], [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[ii]])
                
        
    f.set_final('s0')
    f.set_final('s1')
    f.set_final('s11')
    f.set_final('s12')
    f.set_final('s21')
    f.set_final('s711')
    f.set_final('s712')
    f.set_final('s713')
    f.set_final('s714')
    f.set_final('s22')
    f.set_final('s23')
    f.set_final('s41')
    f.set_final('s42')
    f.set_final('s102')
    f.set_final('s103')
    
    
    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))
    


