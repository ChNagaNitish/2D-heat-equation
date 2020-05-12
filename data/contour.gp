set terminal pngcairo enhanced font "Times New Roman,30.0" size 1000,800
set output filename . '.png'
set size 1,1
#####################################
set encoding utf8
set title 'time step = ' . filename
set xrange [0:1]
set yrange [0:1]
set zrange [cbmin:cbmax]
unset key
set cbrange [cbmin:cbmax]
set palette rgbformulae 33,13,10
plot 'time_step_' . filename . '.dat' with image