def avgStateUpdate(x_prev, x_meas, iNumOfMeas):

    """
    This is a generic function.
    This function performs the current state estimation based on the
    previous state prediction for the averaging filter



    Inputs
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Variable      Variable Type       Description
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    x_prev        scalar              The previous state estimation
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    x_meas        scalar              Measured value
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    iNumOfMeas    scalar              Number of measurements
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------



    Outputs
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Variable      Variable Type       Description
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    x_cur         scalar              The current state estimation
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """

    alpha = 1/iNumOfMeas
    x_cur = x_prev + alpha*(x_meas - x_prev)

    return x_cur