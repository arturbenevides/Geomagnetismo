# Function Juliandate from MatLab

juliandate Calculate Julian date.
    JD = juliandate( V ) converts one or more date vectors V into Julian date JD.
    Input V can be an M-by-6 or M-by-3 matrix containing M full or partial date vectors, respectively.
    juliandate returns a column vector
    of M Julian dates which are the number of days and fractions since noon
    Universal Time on January 1, 4713 BCE.
    
    A date vector contains six elements, specifying year, month, day, hour,
    minute, and second. A partial date vector has three elements, specifying
    year, month, and day.  Each element of V must be a positive double
    precision number.
    
    JD = juliandate(S,F) converts one or more date strings S to Julian date
    JD using format string F. S can be a character array where each
    row corresponds to one date string, or one dimensional cell array of
    strings.  juliandate returns a column vector of M Julian dates, where M is
    the number of strings in S.
    
    All of the date strings in S must have the same format F, which must be
    composed of date format symbols according to DATESTR help. Formats with
    'Q' are not accepted by juliandate. 
    
    Certain formats may not contain enough information to compute a date
    number.  In those cases, hours, minutes, and seconds default to 0, days
    default to 1, months default to January, and years default to the
    current year. Date strings with two character years are interpreted to
    be within the 100 years centered around the current year.
       
    JD = juliandate(Y,MO,D) and JD = juliandate([Y,MO,D]) return the Julian
    date for Y,MO,D (year,month,day). Y, MO, and D must be either one 
    dimensional arrays of the same length or scalar values. 
    
    JD = juliandate(Y,MO,D,H,MI,S) and JD = juliandate([Y,MO,D,H,MI,S])
    return the Julian dates for Y,MO,D,H,MI,S (year,month,day,hour,minute,second). 
    Y, MO, D, H, MI, S must be either one dimensional arrays of the same 
    length or scalar values. 
    
    Limitations: 
    This function is valid for all common era (CE) dates in the Gregorian calendar.
 
    The calculation of Julian date does not take into account leap seconds.
 
    Examples:
 
    Calculate Julian date for May 24, 2005:
 	   jd = juliandate('24-May-2005','dd-mm-yyyy')
    
    Calculate Julian date for December 19, 2006:
 	   jd = juliandate(2006,12,19)
    
    Calculate Julian date for October 10, 2004 at 12:21:00 pm:
 	   jd = juliandate(2004,10,10,12,21,0)
     
     
# Function mjuliandate from Matlab

   mjuliandate Calculate modified Julian date.
    MJD = mjuliandate( V ) converts one or more date vectors V into
    modified Julian date MJD.  Input V can be an M-by-6 or M-by-3 matrix
    containing M full or partial date vectors, respectively.  mjuliandate
    returns a column vector of M modified Julian dates.  Modified Julian
    dates begin at midnight rather than noon and have the first two digits of 
    the corresponding Julian date removed.
 
    A date vector contains six elements, specifying year, month, day, hour, 
    minute, and second. A partial date vector has three elements, specifying 
    year, month, and day.  Each element of V must be a positive double 
    precision number.  
    
    MJD = mjuliandate(S,F) converts one or more date strings S to modified
    Julian date MJD using format string F. S can be a character array where
    each row corresponds to one date string, or one dimensional cell array
    of strings.  mjuliandate returns a column vector of M Julian dates,
    where M is the number of strings in S. 
    
    All of the date strings in S must have the same format F, which must be
    composed of date format symbols according to DATESTR help. Formats with
    'Q' are not accepted by mjuliandate. 
 
    Certain formats may not contain enough information to compute a date
    number.  In those cases, hours, minutes, and seconds default to 0, days
    default to 1, months default to January, and years default to the
    current year. Date strings with two character years are interpreted to
    be within the 100 years centered around the current year.
    
    MJD = mjuliandate(Y,MO,D) and MJD = mjuliandate([Y,MO,D]) return the
    modified Julian date for corresponding elements of the Y,MO,D
    (year,month,day) arrays. Y, MO, and D must be either one dimensional 
    arrays of the same length or scalar values. 
    
    MJD = mjuliandate(Y,MO,D,H,MI,S) and MJD = mjuliandate([Y,MO,D,H,MI,S])
    return the modified Julian dates for corresponding elements of the
    Y,MO,D,H,MI,S (year,month,day,hour,minute,second) arrays.  The six
    arguments must be either one dimensional arrays of the same length or 
    scalar values. 
    
    Limitations: 
    This function is valid for all common era (CE) dates in the Gregorian
    calendar.
 
    The calculation of Julian date does not take into account leap seconds.
    
    Examples:
    
    Calculate modified Julian date for May 24, 2005:
 	   mjd = mjuliandate('24-May-2005','dd-mm-yyyy')
 
    Calculate modified Julian date for December 19, 2006:
 	   mjd = mjuliandate(2006,12,19)
 
    Calculate modified Julian date for October 10, 2004 at 12:21:00 pm:
 	   mjd = mjuliandate(2004,10,10,12,21,0) 
     
     
# Function Decyear from Matlab

   decyear Calculate decimal year.
    DY = decyear( V ) converts one or more date vectors V into decimal year
    DY.  Input V can be an M-by-6 or M-by-3 matrix containing M full or
    partial date vectors respectively.  decyear returns a column vector of
    M decimal years.
 
 	A date vector contains six elements, specifying year, month, day, hour, 
 	minute, and second. A partial date vector has three elements, specifying 
 	year, month, and day.  Each element of V must be a positive double 
 	precision number.  
 
 	DY = decyear(S,F) converts one or more date strings S to decimal year
 	DY using format string F. S can be a character array where each
 	row corresponds to one date string, or one dimensional cell array of 
 	strings.  decyear returns a column vector of M decimal years, where M is 
 	the number of strings in S. 
 
 	All of the date strings in S must have the same format F, which must be
 	composed of date format symbols according to Table 2 in DATESTR help.
 	Formats with 'Q' are not accepted by decyear.  
 
 	Certain formats may not contain enough information to compute a date
 	number.  In those cases, hours, minutes, and seconds default to 0, days
 	default to 1, months default to January, and years default to the
 	current year. Date strings with two character years are interpreted to
 	be within the 100 years centered around the current year.
 
 	DY = decyear(Y,MO,D) and DY = decyear([Y,MO,D]) return the decimal
 	year for corresponding elements of the Y,MO,D (year,month,day)
 	arrays. Y, MO, and D must be either one dimensional arrays of the same 
    length or scalar values. 
 
        DY = decyear(Y,MO,D,H,MI,S) and DY = decyear([Y,MO,D,H,MI,S]) return the
 	decimal years for corresponding elements of the Y,MO,D,H,MI,S
 	(year,month,day,hour,minute,second) arrays.  The six arguments must be
    either one dimensional arrays of the same length or scalar values.
    Limitation: 
 
    The calculation of decimal year does not take into account leap seconds.
 
    Examples:
 
    Calculate decimal year for May 24, 2005:
 	   dy = decyear('24-May-2005','dd-mm-yyyy')
 
    Calculate decimal year for December 19, 2005:
 	   dy = decyear(2006,12,19)
 
    Calculate decimal year for October 10, 2004 at 12:21:00 pm:
 	   dy = decyear(2004,10,10,12,21,0)  
