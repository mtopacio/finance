import math

def BSM(option_type:str, s:float, k:float, t:float, r:float, sigma:float) -> float:

    """
    Black-Scholes Model

    Parameters:
        option_type (str): "option" or "put"
        s (float): current price
        k (float): strike price
        t (float): time to expiration in years
        r (float): risk-free interest rate
        sigma (float): annualized volatility of the underlying asset
    
    Returns:
        float: option price
    """

    d1 = (math.log(s/k) + (r + 0.5 * sigma**2) * t) / (sigma*math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)

    if option_type == "call":
        option_price = S * math.exp(-r * T) * CND(d1) - K * math.exp(-r * T) * cumulative_normal_distribution(d2)
    elif option_type == "put":
        option_price = K * math.exp(-r * T) * CND(-d2) - S * math.exp(-r * T) * cumulative_normal_distribution(-d1)
    else:
        raise ValueError("Invalid option type. Must be either 'call' or 'put'.")
    
    return option_price

def CND(x):
    """
    Cumulative standard normal distribution function.
    
    Args:
        x (float): Input value.
    
    Returns:
        float: Cumulative distribution value.
    """
    
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


# Example
option_price = black_scholes("call", 100, 110, 1, 0.05, 0.2)
print("Option price:", option_price)