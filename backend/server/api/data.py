import pandas as pd
import os
import numpy as np
from fuzzywuzzy import fuzz
from functools import partial
import traceback
import datetime

# Set the data path
data_path = os.path.join(os.getcwd(), 'backend/server/data')

class Data:
    def __init__(self, hotel_params, offers_params):
        self.hotels_params = hotel_params
        self.offers_params = offers_params
        self.hotels = self.load_hotels()
        self.offers = None

    def load_offers(self):
        offers = pd.DataFrame()
        counter = 0

        # Load offers data in chunks from CSV file
        for chunk in pd.read_csv(data_path + '/offers.csv', dtype={'hotelid': str, 'countadults': str, 'countchildren': str, 'price': int, 'inbounddepartureairport': str, 'outboundarrivalairport': str, 'inboundarrivaldatetime': str, 'outbounddepartureairport': str, 'inboundarrivalairport': str, 'outboundarrivaldatetime': str, 'mealtype': str, 'oceanview': str, 'roomtype': str}, sep=',', chunksize=100000):
            if counter == 1:
                break
            self.offers = chunk

            # Convert date columns to datetime objects
            self.offers['outbounddeparturedatetime'] = pd.to_datetime(self.offers['outbounddeparturedatetime'], utc=True)
            self.offers['inbounddeparturedatetime'] = pd.to_datetime(self.offers['inbounddeparturedatetime'], utc=True)
            self.offers = self.remove_duplicates(self.offers)
            df = self.run()
            offers = pd.concat([offers, df])
            counter += 1

        return offers


    # Load hotels data from CSV file
    def load_hotels(self):
        return pd.read_csv(data_path + '/hotels.csv', sep=';', dtype={ 'hotelid': 'str' })



    # Process the loaded offers
    def run(self):
        if not self.offers_params and not self.hotels_params:
            return self.merge()
        
        # Apply hotel filters
        if self.hotels_params:
            self.filter_hotels()
        
        # Apply offers filters
        if self.offers_params:
            self.filter_offers()
        
        return self.merge()

    def fuzzy_match(self, query, choices, threshold):
        return choices.apply(partial(fuzz.token_set_ratio, s2=query)) >= threshold

    
    
    # Filter hotels based on given parameters
    def filter_hotels(self):
        try:
            self.hotels = self.hotels[self.fuzzy_match(self.hotels_params["hotelname"], self.hotels["hotelname"], threshold=80)]
        except Exception as e:
            print("=== ERROR IN FILTER_HOTELS ===")
            print(e)
            pass
        
        try:
            self.hotels = self.hotels[self.hotels['hotelstars'] >= float(self.hotels_params['hotelstars'])]
        except:
            pass

        return self.hotels


    # Filter offers based on parameters
    def filter_offers(self):
        try:
            if "countadults" in self.offers_params and "countchildren" in self.offers_params:
                pass
            elif "countadults" in self.offers_params:
                self.offers_params["countchildren"] = '0'
            elif "countchildren" in self.offers_params:
                self.offers_params["countadults"] = '0'

            query_conditions = []

            for key, value in self.offers_params.items():
                if key == 'outbounddeparturedatetime':
                    date_object = datetime.datetime.strptime(value, "%Y-%m-%d")
                    date_object = date_object.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=datetime.timezone.utc)
                    formatted_date = date_object.isoformat()
                    query_conditions.append(f"outbounddeparturedatetime >= '{formatted_date}'")
                elif key == 'inbounddeparturedatetime':
                    date_object = datetime.datetime.strptime(value, "%Y-%m-%d")
                    date_object = date_object.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=datetime.timezone.utc)
                    formatted_date = date_object.isoformat()
                    query_conditions.append(f"inbounddeparturedatetime <= '{formatted_date}'")
                elif key == 'minprice':
                    query_conditions.append(f"price >= {int(value)}")
                elif key == 'maxprice':
                    query_conditions.append(f"price <= {int(value)}")
                elif key == 'duration':
                    query_conditions.append(f"(inbounddeparturedatetime - outbounddeparturedatetime).dt.total_seconds() / (24*60*60) >= {int(value)}")
                else:
                    query_conditions.append(f"{key} == '{value}'")

            query_condition = " and ".join(query_conditions)

            self.offers = self.offers.query(query_condition)

            return self.offers
        except Exception as e:
            print("=== ERROR IN FILTER_OFFERS ===")
            traceback.print_tb(e.__traceback__)
            pass

    # second query
    def get_all_hotel_offers(self, hotelid):
        df = pd.DataFrame()
        # Load offers data for a specific hotel in chunks
        for chunk in pd.read_csv(data_path + '/offers.csv', dtype={'hotelid': str, 'countadults': str, 'countchildren': str, 'price': int, 'inbounddepartureairport': str, 'outboundarrivalairport': str, 'inboundarrivaldatetime': str, 'outbounddepartureairport': str, 'inboundarrivalairport': str, 'outboundarrivaldatetime': str, 'mealtype': str, 'oceanview': str, 'roomtype': str}, sep=',', chunksize=100000, nrows=100000):
            chunk['outbounddeparturedatetime'] = pd.to_datetime(chunk['outbounddeparturedatetime'], utc=True)
            chunk['inbounddeparturedatetime'] = pd.to_datetime(chunk['inbounddeparturedatetime'], utc=True)
            filtered_chunk = chunk[chunk['hotelid'] == hotelid]
            df = pd.concat([df, filtered_chunk])

        self.offers = df
        self.hotels = self.hotels[self.hotels['hotelid'] == hotelid]
        return self.merge() 

    def merge(self):
        merged_data = self.hotels.merge(self.offers, on='hotelid', how='inner')
        return merged_data

    # Remove duplicates based on hotelid
    def remove_duplicates(self, df):
        cols_to_compare = ['hotelid']
        df_unique = df.sort_values('price').drop_duplicates(subset=cols_to_compare, keep='first')
        return df_unique
