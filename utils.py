# Defining a model for the first order system
def BasicModel(yk, uk, Ts):
    # Model parameters
    K = 3
    T = 5
    a = -1/T
    b = K/T

    # Mathematical model
    yk1 = (1 + a*Ts)*yk + b*Ts*uk

    return yk1

def Controller(r, y, u_prev, e_prev, Ts):

    # PI Controller Initial Parameters
    Kp = 0.5
    Ti = 5
    Ki = Kp/Ti

    # error
    e = r - y # r is the reference and y is the output
    u = u_prev + Kp*(e - e_prev) + Ki*Ts*e

    return u, e
