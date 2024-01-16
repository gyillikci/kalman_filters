def F_matrix_12(x, Fargs):
    """
    Description
    This function creates F matrix (State Transition Matrix) for example 12.

    Inputs
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Variable              Variable Type       Units       Description
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    x                     matrix                          pendulum angle and angular velocity
                                                          (first row is the pendulum angle, second row is the pendulum angular velocity)
    -------------------------------------------------------------------------------------------------------------------------------------------------------
    Fargs[0] - g          scalar              m/s^2       Gravitational acceleration constant
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Fargs[1] - L          scalar              meters      Pendulum string length
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Fargs[2] - dt         scalar              seconds     time between samples
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------


    Outputs
    -------------------------------------------------------------------------------------------------------------------------------------------------------
    Variable      Variable Type                Units       Description
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    F             matrix                                   State Transition Matrix
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    dF            matrix                                   Derivative of F
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    import numpy as np

    g = Fargs[0]
    L = Fargs[1]
    dt = Fargs[2]

    Fx = np.array([x[0] + x[1]*dt, x[1] - g/L*np.sin(x[0])*dt])  # create F matrix (State Transition Matrix)
    dFx = np.array([[1, dt],[-g/L*np.cos(x[0])*dt, 1]], dtype='float64')          # derivative of Fx

    return Fx, dFx