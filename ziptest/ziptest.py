import pandas as pd
import zipline
from zipline.api import order, record, symbol

def initialize(context):
    pass

def handle_data(context,data):
    order(symbol('AAPL'),10)
    record(APPL=data.current(symbol('AAPL'),"price"))


