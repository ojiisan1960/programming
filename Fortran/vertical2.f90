!
! http://www.mrao.cam.ac.uk/~rachael/compphys/SelfStudyF95.pdf
!
program vertical

!
! Vertical motion under gravity
!
implicit none           ! all variables must be defined before use

real, parameter :: g = 9.8  !defines g to be a constant

! define variables
real :: s               ! displacement
real :: t               ! time
real :: u               ! initial speed ( m/s )

! set values the the variables
t =6.0
u = 60

! Calculate displacement
s = u * t -g * (t**2) /2

! output results ( print or write? )

!write(*,*) 'Time = ',t,' Displacement = ',s
print *,'Time = ',t,' Displacement = ',s

end program vertical
