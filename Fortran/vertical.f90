!
! http://www.mrao.cam.ac.uk/~rachael/compphys/SelfStudyF95.pdf
!
program vertical

!
! Vertical motion under gravity
!

! define variables
real :: g               ! acceleration due to gravity
real :: s               ! displacement
real :: t               ! time
real :: u               ! initial speed ( m/s )

! set values the the variables
g = 9.8
t =6.0
u = 60

! Calculate displacement
s = u * t -g * (t**2) /2

! output results ( print or write? )

!write(*,*) 'Time = ',t,' Displacement = ',s
print *,'Time = ',t,' Displacement = ',s

end program vertical
