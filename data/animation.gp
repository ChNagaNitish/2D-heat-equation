set terminal gif animate delay 15
set output "animation.gif"
######################
set pm3d map
set xrange [0:1]
set yrange [0:1]
set zrange [cbmin:cbmax]
unset key
set cbrange [cbmin:cbmax]
set palette rgbformulae 33,13,10
do for [i=0:var] { splot sprintf('time_step_%d.dat', i*t_s) with image }