import os
from api.data import Data
from api.hotel import Hotel
from flask import Flask, request, Response, render_template, redirect
import traceback
import urllib.parse


template_dir = os.path.abspath("frontend/templates")
static_dir = os.path.abspath("frontend/static")
hotels_per_page = 10
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)



# Route for displaying hotel details
@app.route('/<hotelid>', methods=['GET'])
def hotel(hotelid):
    page = request.args.get('page', default=1, type=int)
    hotels = []
    data = Data({}, {})
    try:
        hotels = data.get_all_hotel_offers(hotelid)  # Get all offers for the specific hotel
        hotels = hotels.apply(lambda row: Hotel(row).get_hotel(), axis=1).tolist()  # Convert DataFrame rows to hotel dictionaries
        hotels.sort(key=lambda x: x['score'], reverse=True)  # Sort hotels by score in descending order
    except Exception as e:
        print("=== ERROR IN HOTEL-GET ===")
        print(e)
        traceback.print_exc()
        error_msg = True
        hotels = []
        pass

    total_pages = (len(hotels) - 1) // hotels_per_page + 1
    start_index = (page - 1) * hotels_per_page
    end_index = start_index + hotels_per_page
    pagination = hotels[start_index:end_index]
    error_msg = (len(pagination) == 0)

    return render_template('hotel.html', hotelid=hotelid, hotels=pagination, error_msg=error_msg, page=page, total_pages=total_pages)



# Main route for displaying the index page with all hotels
@app.route('/', methods=['GET'])
def index():
    page = request.args.get('page', default=1, type=int)
    hotel_params = {}
    offer_params = {}
    filter_param = request.args.get('filter', default='score', type=str)
    for key, value in request.args.items():
        if key == 'page':
            continue
        if value != '' and value != '0' and not key.startswith('hotel') and value != 'NOT':
            offer_params[key] = value
        elif value != '' and value != '0.0' and key.startswith('hotel') and value != 'NOT':
            hotel_params[key] = value

    data = Data(hotel_params, offer_params)

    try:
        hotels = data.load_offers()  # Load offers data based on the given parameters
        hotels = hotels.apply(lambda row: Hotel(row).get_hotel(), axis=1).tolist()  # Convert DataFrame rows to hotel dictionaries
        hotels.sort(key=lambda x: x['score'], reverse=True)  # Sort hotels by score in descending order
        
        # Pagination for website
        total_pages = (len(hotels) - 1) // hotels_per_page + 1
        start_index = (page - 1) * hotels_per_page
        end_index = start_index + hotels_per_page
        pagination = hotels[start_index:end_index]
        error_msg = (len(pagination) == 0)

        # Get current request parameters and add them to the next page URL
        next_page_url = "/?page=" + str(page + 1) + "&" + urllib.parse.urlencode(request.args) + "#results"
        return render_template('index.html', hotels=pagination, hotel_params=hotel_params, offer_params=offer_params, show_filter=True, error_msg=error_msg, page=page, total_pages=total_pages, next_page_url=next_page_url)

    except Exception as e:
        print("=== ERROR IN INDEX-POST ===")
        print(e)
        
        # Print traceback
        traceback.print_exc()
        return render_template('index.html', hotels=[], hotel_params=hotel_params, offer_params=offer_params,
                               show_filter=True, error_msg=True, page=page, total_pages=0, next_page_url="")

    return render_template('index.html', hotels=[], hotel_params=hotel_params, offer_params=offer_params, show_filter=True, error_msg=True, page=page, total_pages=0, next_page_url="")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
