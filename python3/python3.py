#! /usr/bin/python

import sys
import copy

A = sys.argv[1]
B = sys.argv[2]
C = sys.argv[3]
D = sys.argv[4]
E = sys.argv[5]
F = sys.argv[6]
G = sys.argv[7]
count =0

a = [[' ' for x in range(5)]for x in range(5)]
b = [[' ' for x in range(5)]for x in range(5)]
c = [[' ' for x in range(5)]for x in range(5)]
d = [[' ' for x in range(5)]for x in range(5)]
e = [[' ' for x in range(5)]for x in range(5)]
ff = [[' ' for x in range(5)]for x in range(5)]
g = [[' ' for x in range(5)]for x in range(5)]

flag = a1 = a2 = b1 = b2 = c1 = c2 = d1 = d2 = e1 = e2 = f1 = f2 = g1 = g2 = 0
def intial(name):
  matrix = [[' ' for x in range(5)]for x in range(5)]
  with open(name) as f:
   m = 0
   n = 0
   for line in f:
      for ch in line:
        if ch == ' ':
           matrix[m][n] = ' '
           n = n+1

        if ch != ' ' and ch != '\n':
           matrix[m][n]= ch
           n = n+1
      if n <5:
         for ii in range(n,5):
             matrix[m][ii]= ' '
         m = m+1
         n = 0
  return (matrix);
def read_block(name,matrix):
  s = h = 0
  with open(name) as f:
   m = 0
   n = 0
   for line in f:
      for ch in line:
        if ch == ' ':
           matrix[m][n] = ' '
           n = n+1

        if ch != ' ' and ch != '\n':
           matrix[m][n]= ch
           n = n+1
           if s <=m:
              s = m
           if h <= n-1:
              h = n - 1
      if n <5:
         for ii in range(n,5):
             matrix[m][ii]= ' '
         m = m+1
         n = 0
  return (matrix,s,h);

def block(matrix,i,l):
  square = [[' ' for x in range(5)]for x in range(5)]
  for mm in range(5):
      for nn in range(5):
         if mm+i <5 and nn+l<5:
            square[mm+i][nn+l]=matrix[mm][nn]
            if mm+i==4 and nn+l ==4:
               break
  return (square);

def block_more(matrix1,matrix2,i,l):
  biu = 0
  for mm in range(5):
      if biu == 1:
         break
      for nn in range(5):
         if mm+i <5 and nn+l<5:
            if matrix2[mm+i][nn+l] != ' ' and matrix1[mm][nn] != ' ':
                flag = 0
                biu = 1
                break
            elif matrix2[mm+i][nn+l]==' ' :
               matrix2[mm+i][nn+l]=matrix1[mm][nn]
               if mm+i==4 and nn+l ==4:
                  flag = 1
                  biu = 1
                  break
            elif matrix2[mm+i][nn+l] != ' ' :
               if mm+i==4 and nn+l ==4:
                  mm = 6
                  flag = 1
                  biu = 1
                  break

  return (flag,matrix2);

a,a1,a2=read_block(A,a)
b,b1,b2=read_block(B,b)
c,c1,c2=read_block(C,c)
d,d1,d2=read_block(D,d)
e,e1,e2=read_block(E,e)
ff,f1,f2=read_block(F,ff)
g,g1,g2=read_block(G,g)
a_new = [[' ' for x in range(5)]for x in range(5)]
a_new = intial(A)
a_old = [[' ' for x in range(5)]for x in range(5)]
a_old = intial(A)
for lin in range(5-a1):
   for col in range(5-a2):
     a_old = block(a,lin,col)
     a_new = block(a,lin,col)
     for lin1 in range(5-b1):
        for col1 in range(5-b2):
          flag = block_more(b,a_new,lin1,col1)[0]
          if flag ==1:
             a_new = copy.deepcopy(a_old)
             b = block_more(b,a_new,lin1,col1)[1]
             b_old = copy.deepcopy(b)
             for lin2 in range(5-c1):
                for col2 in range(5-c2):
                  flag = block_more(c,b,lin2,col2)[0]
                  if flag ==1:
                    b = copy.deepcopy(b_old)
                    c = block_more(c,b,lin2,col2)[1]
                    c_old = copy.deepcopy(c)
                    for lin3 in range(5-d1):
                        for col3 in range(5-d2):
                          flag = block_more(d,c,lin3,col3)[0]
                          if flag == 1:
                            c = copy.deepcopy(c_old)
                            d = block_more(d,c,lin3,col3)[1]
                            d_old = copy.deepcopy(d)
                            for lin4 in range(5-e1):
                               for col4 in range(5-e2):
                                 flag = block_more(e,d,lin4,col4)[0]
                                 if flag ==1:
                                   d = copy.deepcopy(d_old)
                                   e = block_more(e,d,lin4,col4)[1]
                                   e_old = copy.deepcopy(e)
                                   for lin5 in range(5-f1):
                                     for col5 in range(5-f2):
                                        flag = block_more(ff,e,lin5,col5)[0]
                                        if flag ==1:
                                          e = copy.deepcopy(e_old)
                                          ff = block_more(ff,e,lin5,col5)[1]
                                          ff_old = copy.deepcopy(ff)
                                          for lin6 in range(5-g1):
                                             for col6 in range(5-g2):
                                                flag = block_more(g,ff,lin6,col6)[0]
                                                if flag ==1:
                                                   ff = copy.deepcopy(ff_old)
                                                   g = block_more(g,ff,lin6,col6)[1]
                                                   count = count+1
                                                   if count ==1:
                                                     for ni in range(5):
                                                       for mi in range(5):
                                                        sys.stdout.write (g[ni][mi])
                                                        if mi ==4:
                                                          sys.stdout.write('\n')
                                #                  print g
                                                   ff = copy.deepcopy(ff_old)
                                                   g = intial(G)
                                        #  print ff
                                          e = copy.deepcopy(e_old)
                                          ff = intial(F)
                                  # print e
                                   d = copy.deepcopy(d_old)
                                   e = intial(E)
                        #    print d
                            c = copy.deepcopy(c_old)
                            d = intial(D)
                #    print c
                    b = copy.deepcopy(b_old)
                    c = intial(C)
            # print b
             a_new = copy.deepcopy(a_old)
             b= intial(B)
     a_new = intial(A)
                                                

