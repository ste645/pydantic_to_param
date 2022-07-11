"""AUTO GENERATED DATACLASS for Trade."""

import param


class Period(param.Parameterized):
    """Period Object"""

    strike= param.Integer(default=None)
    trade_date= param.Integer(default=None)


class Leg(param.Parameterized):
    """Leg Object"""

    strike= param.Integer(default=None)
    period= param.List(default=None)



class Trade(param.Parameterized):
    """Trade Object."""

    strike= param.Number(default=2.0)
    name= param.String(default=None)
    number= param.Integer(default=None)
    trade_date= param.Date(default=None)
    legs= param.List(default=None)
    periods= param.List(default=None)
