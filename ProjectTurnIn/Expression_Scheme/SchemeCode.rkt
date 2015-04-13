#lang racket
(define (quad a b c)
  (if (>=(- (* b b) (* 4 a c)) 0)
       (list (quad2 a b c) (quad3 a b c))
       (display '(NONREAL SOLUTIONS))
  )
)

(define (quad2 a b c)
  (/(/ (- (- b) (sqrt(- (* b b) (* 4 a c)))) 2) a)
  )


(define (quad3 a b c)
   (/(/ (+ (- b) (sqrt(- (* b b) (* 4 a c)))) 2) a)
  )

(define (deletefrm a b)
  (cond
    ((not(list? b)) b)
    ((null? b) '() )
    ((equal? a (car b)  ) (deletefrm a (cdr b) ) )  
    (else (cons (car b) (deletefrm a (cdr b) ) ) ) 
    )
  )

 (define (mergeset lsta lstb)
    (cond
      ((not(null? lstb))(mergeset (addelem lsta (car lstb) ) (cdr lstb) ) )
      (else lsta) 
    )
   )

(define (addelem lst a)
  (cond
    ((null? lst) (cons a '()))
    ( ( not(equal? (car lst) a) ) (cons (car lst) (addelem (cdr lst) a ) ) )
    (else lst)
  )
  )

(define (randexp n)
	(define x (- (random 19) 9) )
	(define y (- (random 19) 9) )
	(cond
		((> n 0) ((randop) (randexp (- n 1)) (randexp (- n 1))))
		(else ((randop) x y))
	)
)


(define (randop)
	(define x (random 3))
	(cond
		((= x 0) +)
		((= x 1) *)
		((= x 2) -)
	)
)

(define (repeat exp n lst)
  (define x (exp 2))
  (if (> n 0)
      (cond
        ((> x 25) (repeat exp (- n 1)( list (car lst) (car (cdr lst))(+ (car(cdr(cdr lst))) 1))))
        ((< x -25) (repeat exp (- n 1)( list (+ (car lst) 1) (car (cdr lst))(car(cdr(cdr lst)))))) 
        (else (repeat exp (- n 1)( list (car lst) (+ (car (cdr lst)) 1) (car(cdr(cdr lst))) )) ))
      lst)
 )

(repeat randexp 100000 '(0 0 0))

;EXTRA CREDIT!

(define (randexp1 n)
	(define x (- (random 19) 9) )
	(define y (- (random 19) 9) )
        (define a (random (+ n 1)) )
        (define b (random 2))
	(cond
                ((and (> n 0) (> a 0) (> b 0) ) ((randop) (randexpgar (- n 1)) (randexp2 (- n a))))
                ((and (> n 0) (> a 0)) ((randop) (randexp2 (- n a)) (randexpgar (- n 1))))
		((> n 0) ((randop) (randexp1 (- n 1)) (randexp1 (- n 1))))
		(else ((randop) x y))
	)
)

(define (randexpgar n)
	(define x (- (random 19) 9) )
	(define y (- (random 19) 9) )
        (define a (+ (random2 n)  1) )
	(define b (random 2))
	(cond
                ((and (> n 0) (> a 0) (> b 0) ) ((randop) (randexpgar (- n 1)) (randexp2 (- n a))))
                ((and (> n 0) (> a 0)) ((randop) (randexp2 (- n a)) (randexpgar (- n 1))))
		((> n 0) ((randop) (randexp2 (- n 1)) (randexp2 (- n 1))))
		(else ((randop) x y))
	)
)

(define (randexp2 n)
	(define x (- (random 19) 9) )
	(define y (- (random 19) 9) )
        (define a (+ (random2 n)  1) )
        (define b (+ (random2 n)  1) )
	(cond
		((> n 0) ((randop) (randexp2 (- n a)) (randexp2 (- n b))))
		(else ((randop) x y))
	)
)

(define (random2 n )
  (if (> n 0)
      (random n)
      0
  )
  )

(repeat randexp1 100000 '(0 0 0))
