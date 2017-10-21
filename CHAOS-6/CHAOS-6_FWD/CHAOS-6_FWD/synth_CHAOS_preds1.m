%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Matlab script to calculate predictions of CHAOS field model
% Both internal and external parts
% Given list of input locations and times
% CF 03.09.2014
% Updated for CHAOS-6 12.05.2016
% Following NIO's model_synth_values.m
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear all;
close all;
a = 6371.2; % Earth's radius
rad = pi/180; % Conversion degrees to radians

tmp=load('./input.dat');   % Read in list of Input 

theta = tmp(:,1);   %  Gecentric co-lat (deg)
phi = tmp(:,2);     % Geocentric longitude (deg)
r=a+tmp(:,3);  % Geocentric radius from Altitude (km)
t=tmp(:,4) ;     % time (MJD2000)

% load CHAOS model
load('./CHAOS-6.mat')

% load RC-index
filename_Dst  = './RC_1997-2016_May_v1.dat';
[t_Dst, Dst_all, Dst_e_all, Dst_i_all]  = textread(filename_Dst, '%f %f %f %f %*s', 'commentstyle', 'shell');

% low degree field, spline representation up to N
disp('core field model values ...')
N = 20;   % Take all of core field
pp_N = pp;
pp_N.dim = N*(N+2);
coefs_tmp = reshape(pp.coefs, [], pp.pieces, pp.order);
pp_N.coefs = reshape(coefs_tmp(1:N*(N+2),:,:), [], pp.order);
B_core = synth_values(r, theta, phi, pp, t);

% high degree field
disp('custal field model values ...')
B_crust = synth_values(r, theta, phi, g(1:110*112));  % Take crustal field up to degree 110
B_int_mod = B_core + B_crust;

disp('external field model values ...')
RC_ei = interp1(t_Dst, [Dst_e_all Dst_i_all], t, 'linear');

B_ext_mod = synth_values_CHAOS_ext(t, r, theta, phi, RC_ei, model_ext);

B_chaos= B_int_mod + B_ext_mod;

% save the output predictions to asii file
filename_out = './CHAOS_preds.dat'
fid_out = fopen(filename_out, 'w');
fprintf(fid_out, '%s\n', '%    t [md2000]    r [km] theta [deg]   phi [deg]       B_r   B_theta     B_phi       B_r   B_theta     B_phi       B_r   B_theta     B_phi');
fprintf(fid_out, '%s\n', '%                                                            model total                  model internal                model external');

fprintf(fid_out,'%15.8f %9.3f %11.5f %11.5f %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n',...
    [t r theta phi B_chaos B_int_mod B_ext_mod]');
fclose(fid_out);

