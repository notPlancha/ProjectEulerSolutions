#set page(height: auto, width: auto)

$
  &A := "Taking 2 Red" \
  &B := "Taking 2 Black" \
  &C := "Taking 1 of each"
  \ \ 
  &R := "Number of Red balls" \
  
  &B := "Number of Black balls"
  \ \ 
  &P(a,b) := P(R=a, B=b)
$
#pagebreak()

$
  P(A) &= cases(binom(R, 2) / binom(R+B, 2) "if" R >= 2, 0 "otherwise")
  \
  P(B) &= cases(binom(B, 2) / binom(R+B, 2) "if" B >= 2, 0 "otherwise")
  \
  P(C) &= cases((binom(R, 1) dot binom(B, 1)) / binom(R+B, 2) "if" R >= 1 and B >= 1, 0 "otherwise")
  \ 
  P(a,b) &= cases(1 "if" a == 0, 0 "if" b == 0, f(a,b) "otherwise")
  \
  f(a,b) =& P(A; a,b) dot P(a-2, b) + \
  +& P(B; a,b) dot P(a,b) \
  +& P(C; a,b) dot P(a,b-1)
$

$ binom(n, 1) = n $

#pagebreak()

$
  P(2,2)   =&P(A; 2,2) dot P(0,2) + \ 
           +& P(B; 2,2) dot P(2,2) \
           +& P(C; 2,2) dot P(2,1)
  \ \ \ \ \
  P(0,2) &= 1
  \ \ \ \ \
  P(2,1)   = & P(A; 2,1) dot P(0,1) + \
           + & P(B; 2,1) dot P(2,1) \
           + & P(C; 2,1) dot P(2,0)
  \ \ \ \ \
  P(0,1)    &= 1 \
  P(2,0)    &= 0 \
  P(B; 2,1) &= 0 \
  \ \ \ \ \
  therefore P(2,1)  =& P(A; 2,1) dot 1 + \
                    +& 0 dot P(2,1) \
                    +& P(C; 2,1) dot 0 \
      P(2,1)     &= P(A; 2,1) \
      &=binom(2, 2) / binom(3, 2) \
      &=1/3
  \ \ \ \ \
  P(B; 2,2) &= binom(2, 2) / binom(4, 2) \
  &=1/6
  \
  P(A; 2,2) &= binom(2, 2) / binom(4, 2) \
  &=1/6
  \
  P(C; 2,2) &= (2 dot 2) / binom(4, 2) \
  &=4/6 \
  \ \ \ \ \

  therefore P(2,2) &= 1/6 dot 1 + \ 
          & + 1/6 dot P(2,2) \
          & + 4/6 dot 1/3 \
  equiv P(2,2) &= 7/15 = 0.4(6) \ && qed
$