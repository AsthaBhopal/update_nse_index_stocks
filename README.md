# update_nse_index_stocks
update NSE index stocks


https://www1.nseindia.com/homepage/Indices1.json


"""
    ? Don't have token & market_segment_id in NSE data 
        - can't map it properly cause it requires uniqueness for ForeignKey
    * Insert into IndexDeatils Table
        - Get all NSE stocks where series is EQ | token & market_segment_id
        - Put Index ID and Stocks token & market_segment_id to Mapper Table
    * Add 4 new columns for indices stock to check stock exist in that specific index | True/False
        - ADDING 4 NEW COLUMNS TO NSE_DATA -> NIFTY BANK | NIFTY 50 | NIFTY NEXT 50 | NIFTY MIDCAP 50
    * ManyToManyField.symmetrical
        - instrument_name = EQIDX | Index
        - `stocks = models.ManyToManyField("self", symmetrical=False)`
        - link `https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.symmetrical`
"""
