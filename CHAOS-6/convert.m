tic;
close all;
clear all;
clc;

load('datas_abs_X2014F.dat');
x=datas_abs_X2014F(:,:);
d = juliandate (x);
mjd = mjuliandate(x);
dy = decyear(x);



