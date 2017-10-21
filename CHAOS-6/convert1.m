tic;
close all;
clear all;
clc;

load('datas_abs_D.dat');
x=datas_abs_D(:,:);
d = juliandate (x);
mjd = mjuliandate(x);
dy = decyear(x);



