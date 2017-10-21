function [S,GST] = sunGEI(md2000)

% function [S,GST] = sunGEI(yyyy,ddd,seconds)
% returns the unit vector position of the sun
% in GEI coordinates
% it also returns grenwich mean sidereal time (GST)
% in radians
% yyyy,ddd,seconds are integers in UT (GMT)
% alternate calling: S = sunGEI(decimalDOY)
% valid for yyyy = 1901-2099

rad = 57.29578;

dj = md2000+36159;
fday = mod(md2000, 1);

t = dj/36525;
vl = mod(279.696678 + 0.9856473354*dj, 360);
GST = mod(279.696678 + 0.9856473354*dj+360*fday+180, 360)/rad;
g = mod(358.475845 + 0.985600267*dj, 360.0)/rad;
slong = vl+(1.91946-0.004789*t).*sin(g) + 0.020094*sin(2*g);
obliq = (23.45229-0.0130125*t)/rad;
slp = (slong-0.005686)/rad;
sind = sin(obliq).*sin(slp);
cosd = sqrt(1-sind.^2);
SDEC = rad*atan(sind./cosd);
SRASN = 180-rad*atan2(1./tan(obliq).*sind./cosd, -cos(slp)./cosd);

X = cos(SRASN/rad).*cos(SDEC/rad);
Y = sin(SRASN/rad).*cos(SDEC/rad);
Z = sin(SDEC/rad);
S = [X Y Z];
