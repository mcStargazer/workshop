import time

def f2c(f):  # Fahrenheit to Celsius
    c = 5.0*( f-32.0 )/9.0
    return c

def c2f(c):  # Celsius to Fahrenheit
    f = 9.0*c/5.0 + 32.0
    return f

def mkISOdate(dd,month,yy):  # Return ISO 8601 Datetime
    """
    INPUTS: dd (int) - Integer day of month
            month (int) - Integer month of year
            yy (int) - Two digit integer year
    OUTPUT: ISO 8601 Standard date string
    """

    # define look up table using dictionary structure
    LUT={"JAN":1,"FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6,\
         "JUL":7,"AUG":8,"SEP":9,"OCT":10,"NOV":11,"DEC":12}

    # create date from field tech descriptions
    if yy > 80: yyyy = yy + 1900
    else: yyyy = yy + 2000
    date = "%s-%02i-%02i" % (yyyy, LUT[month.upper()], dd)

    # create current date
    (now_yr, now_mon, now_day) = (time.localtime().tm_year,
                                  time.localtime().tm_mon,
                                  time.localtime().tm_mday)
    now_str = "%s-%02i-%02i" % (now_yr, now_mon, now_day)

    # compare with current, error if afterwards
    if date > now_str:
        date = "9999-99-99"

    return date


if __name__ == "__main__":

    print("mkISOdate(24, 'Jan', 16): {}".format(mkISOdate(24, "Jan", 16)))
    print("mkISOdate(25, 'Jan', 16): {}".format(mkISOdate(25, "Jan", 16)))
    print("mkISOdate(26, 'Jan', 16): {}".format(mkISOdate(26, "Jan", 16)))
    print("mkISOdate(24, 'jan', 11): {}".format(mkISOdate(24, "jan", 11)))
