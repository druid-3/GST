#!/usr/bin/python3
# -*- coding: utf-8 -*-

from numpy import *

#-------------------------------------------------------------------------------
def proj(normVector, constVector):
    Vn = array(normVector)
    Vc = array(constVector)
    return ((sum(Vc*Vn)/sum(Vn**2))*Vn)
#-------------------------------------------------------------------------------
def gs(vL):
    Out = []
    for i in range(len(vL)):
        nowVec = array(vL[i])

        for v in Out :
            nowVec -= proj(v, nowVec)

        Out.append(nowVec)
    return Out
#-------------------------------------------------------------------------------
def gsn(vL):
    Out = []
    for i in range(len(vL)):
        nowVec = array(vL[i])

        for v in Out :
            nowVec -= proj(v, nowVec)
        nowVec /= sqrt(sum(nowVec*nowVec))

        Out.append(nowVec)
    return Out
#-------------------------------------------------------------------------------

# http://www.scs.ryerson.ca/~danziger/mth141/Handouts/gram.pdf
test_0 = array([[0., 1.], [1., 1.]])
# http://www.personal.psu.edu/tam44/Math2025/Lecture7.pdf
test_1 = array([[1., 1.], [2., -1.]])

test0 = array([[1., 1., 0.], [1., 3., 1.], [2.,-1., 1.]])
# http://www.personal.psu.edu/tam44/Math2025/Lecture7.pdf
test1 = array([[0., 1., 2.], [1., 1., 2.], [1., 0., 1.]])
# http://www.math.ucla.edu/~yanovsky/Teaching/Math151B/handouts/GramSchmidt.pdf
test2 = array([[1., 1., 0.], [1., 0., 1.], [0., 1., 1.]])
# http://www.scs.ryerson.ca/~danziger/mth141/Handouts/gram.pdf
test3 = array([[1., 2., 1.],[1., 1., 3.],[2., 1., 1.]])
# https://www.math.hmc.edu/calculus/tutorials/gramschmidt/gramschmidt.pdf
test4 = array([[1., -1., 1.],[1., 0., 1.],[1., 1., 2.]])
# http://perso.ens-lyon.fr/marco.mazzucchelli/teaching/2011/math220/notes/sec6_4.pdf
test5 = array([[1., 1., 0.], [2., 2., 3.]])

print ("----------------------------------------------------------------------")
print array(gs(test_0))
print ("----------------------------------------------------------------------")
print array(gs(test_1))
print ("----------------------------------------------------------------------")
print array(gs(test0))
print array(gsn(test0))
print ("----------------------------------------------------------------------")
print array(gs(test1))
print ("----------------------------------------------------------------------")
print array(gs(test2))
print ("----------------------------------------------------------------------")
print array(gs(test3))
print ("----------------------------------------------------------------------")
print array(gs(test4))
print ("----------------------------------------------------------------------")
print array(gs(test5))
print ("----------------------------------------------------------------------")
