y <- seq(-4, 4, len = (nn <- 200))
ltry <- c(0, 0.5, 1, 1.5, 2)  # Try these values of lambda
lltry <- length(ltry)
psi <- matrix(as.numeric(NA), nn, lltry)
for (ii in 1:lltry)
  psi[, ii] <- yeo.johnson(y, lambda = ltry[ii])
## Not run: 
matplot(y, psi, type = "l", ylim = c(-4, 4), lwd = 2,
        lty = 1:lltry, col = 1:lltry, las = 1,
        ylab = "Yeo-Johnson transformation", 
        main = "Yeo-Johnson transformation with some lambda values")
abline(v = 0, h = 0)
legend(x = 1, y = -0.5, lty = 1:lltry, legend = as.character(ltry), lwd = 2, col = 1:lltry) 
## End(Not run)
