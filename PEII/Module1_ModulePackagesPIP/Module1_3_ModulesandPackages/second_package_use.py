from sys import path

# path.append("ex_package\\packages\\")

# getting to bottom layers of file tree
#import extra.good.best.sigma
#from extra.good.best.tau import FunT

##print(extra.good.best.sigma.FunS())
#print(FunT())

# using aliasing to make things easier
#import extra.good.best.sigma as sig
#import extra.good.alpha as alp

#print(sig.FunS())
#print(alp.FunA())

# using a zip
# path.append("ex_package\\ex.zip")

#import ex.good.best.sigma as siggy

#print(siggy.FunS())

# can also do this instead of changing path (bit clunky maybe)
import ex_package.packages.extra.good.alpha
