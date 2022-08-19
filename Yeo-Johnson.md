(defun yj-power (y p &key included (normalize t))
"Function args: (data power &key included (normalize t))
This function returns the normalized Yeo-Johnson transformation,
suggested by In-Kwon Yeo and Richard A. Johnson (2000). A new family
of power transformations to improve normality or symmetry, Biometrika,
87, 954-959."
(let* ((lam (if (< (abs p) 1.e-6) 0 p))
(obs (find-obs y))
(gm (geometric-mean (ˆ (+ 1 (abs (select y obs)))
(if-else (< (select y obs) 0) -1 1))
(if included (which (select included obs)))))
(transform (mapcar #’(lambda (x)
(cond ((and (>= x 0) (/= lam 0))
(/ (- (ˆ (+ x 1) lam) 1) lam))
((and (>= x 0) (= lam 0))
(log (+ 1 x)))
((and (< x 0) (/= lam 2))
(- (/ (- (ˆ (+ (- x) 1) (- 2 lam)) 1) (- 2 lam))))
(t (- (log (+ (- x) 1)))))) (select y obs)))
(z y))
(setf (select z obs) transform)
(if normalize (/ z (ˆ gm (- lam 1))) z)))
