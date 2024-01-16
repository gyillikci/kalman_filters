def staicDynamicModel(x_cur, p_cur=0, q=0):
    """
    This is a generic function.
    This function performs the next state prediction.
    For the static dynamic model, the predicted state equals to the current
    state and the predicted uncertainty equals to the current estimation uncertainty


    Inputs
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Variable      Variable Type       Description
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    x_cur         scalar              The current state estimated value
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    p_cur         scalar              The current state estimation variance (optional input)
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------


    Outputs
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Variable      Variable Type       Description
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    x_pred        scalar              The next state estimated value (prediction)
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    p_pred        scalar              The predicted value estimation variance
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    x_pred = x_cur
    p_pred = p_cur + q

    return x_pred, p_pred