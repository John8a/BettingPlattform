import json
from datetime import datetime

airports = {'FRA': 'Frankfurt, Frankfurt am Main', 'MUC': 'München, Franz Josef Strauß', 'DUS': 'Düsseldorf, Düsseldorf', 'BER': 'Berlin, Brandenburg', 'PMI': 'Palma de Mallorca, Son Sant Joan', 'TXL': 'Berlin, Tegel', 'HAM': 'Hamburg, Hamburg', 'STR': 'Stuttgart, Stuttgart', 'CGN': 'Köln, Köln Bonn', 'SXF': 'Berlin, Schönefeld', 'HAJ': 'Hannover, Hannover', 'BRE': 'Bremen, Neuenland', 'NUE': 'Nürnberg, Nürnberg', 'HHN': 'Hahn, Frankfurt Hahn', 'LEJ': 'Leipzig, Leipzig Halle', 'NRN': 'Weeze, Niederrhein', 'DTM': 'Dortmund, Dortmund', 'FMM': 'Memmingen, Allgäu', 'DRS': 'Dresden, Dresden', 'FKB': 'Karlsruhe/Baden-Baden, Baden Airpark', 'FDH': 'Friedrichshafen, Friedrichshafen', 'PAD': 'Paderborn, Paderborn Lippstadt', 'FMO': 'Münster, Münster Osnabrück', 'SCN': 'Saarbrücken, Saarbrücken', 'GWT': 'Westerland, Westerland Sylt', 'ERF': 'Erfurt, Erfurt', 'ZQW': 'Zweibrücken, Zweibrücken', 'RLG': 'Laage, Laage', 'HDF': 'Heringsdorf, Heringsdorf', 'LBC': 'Lübeck, Lübeck Blankensee', 'KSF': 'Kassel, Kassel Calden', 'OAL': 'Marktoberdorf, Marktoberdorf', 'AGB': 'Augsburg, Augsburg', 'XFW': 'Hamburg, Hamburg Finkenwerder', 'MHG': 'Mannheim, Mannheim City', 'BSL': 'Basel, EuroAirport Basel-Mulhouse-Freiburg', 'VIE': 'Wien, Flughafen Wien-Schwechat', 'GRZ': 'Graz, Flughafen Graz', 'INN': 'Innsbruck, Flughafen Innsbruck', 'SZG': 'Salzburg, Flughafen Salzburg', 'LNZ': 'Linz, Flughafen Linz', 'ZRH': 'Zürich, Flughafen Zürich', 'LUX': 'Luxemburg, Flughafen Luxemburg', 'AMS': 'Amsterdam, Flughafen Amsterdam-Schiphol', 'RTM': 'Rotterdam, Flughafen Rotterdam Den Haag', 'BRU': 'Brüssel, Flughafen Brüssel-Zaventem', 'CRL': 'Brüssel, Flughafen Brüssel-Charleroi', 'ANR': 'Antwerpen, Flughafen Antwerpen', 'LGG': 'Lüttich, Flughafen Lüttich', 'OST': 'Ostende, Flughafen Ostende-Brügge', 'LUX': 'Luxemburg, Flughafen Luxemburg', 'WAW': 'Warschau, Flughafen Warschau-Chopin', 'KRK': 'Krakau, Flughafen Johannes Paul II. Krakau-Balice', 'WRO': 'Breslau, Flughafen Breslau-Nikolaus-Kopernikus', 'GDN': 'Danzig, Flughafen Danzig-Lech-Wałęsa', 'PRG': 'Prag, Flughafen Václav Havel', 'BRQ': 'Brünn, Flughafen Brno-Tuřany', 'PED': 'Pardubice, Flughafen Pardubice', 'OSR': 'Ostrava, Flughafen Ostrava-Leoš Janáček', 'EIN': 'Eindhoven Flughafen', 'GVA': 'Genf, Flughafen Genf', 'SXB': 'Straßburg, Flughafen Straßburg'}
mealtype = {'NONE': 'ohne Verpflegung', 'BREAKFAST': 'Frühstück', 'HALFBOARD': 'Halbpension', 'FULLBOARD': 'Vollpension', 'ALLINCLUSIVE': 'All Inclusive', 'ALLINCLUSIVEPLUS': 'All Inclusive+', 'HALFBOARDPLUS': 'Halbpension+', 'FULLBOARDPLUS': 'Vollpension+', 'ACCORDINGDESCRIPTION': 'Andere'}
roomtype = {'NOT': 'No Selection', 'SINGLE': 'Einzelzimmer', 'DOUBLE': 'Doppelzimmer', 'TRIPLE': 'Dreierzimmer', 'FAMILY': 'Familienzimmer', 'ECONOMY': 'Economy', 'STUDIO': 'Studio', 'SUITE': 'Suite', 'APARTMENT': 'Apartment', 'DELUXE': 'Deluxe', 'ACCORDINGDESCRIPTION': 'Andere', 'SUPERIOR': 'Superior', 'BUNGALOW': 'Bungalow', 'TWINROOM': 'Zwillingsraum', 'MULTISHARE': 'Mehrbettzimmer', 'VILLA': 'Villa', 'FOURBEDROOM': 'Vierbettzimmer', 'HOLIDAYHOUSE': 'Ferienhaus', 'JUNIORSUITE': 'Junior Suite'}
oceanview = {True: 'Meerblick', False: 'kein Meerblick'}


# hotelid;hotelname;hotelstarsoutbounddeparturedatetime;inbounddeparturedatetime;countadults;countchildren;price;inbounddepartureairport;inboundarrivalairport;inboundarrivaldatetime;outbounddepartureairport;outboundarrivalairport;outboundarrivaldatetime;mealtype;oceanview;roomtype
class Hotel:
    def __init__(self, data):
        self.hotelid = data['hotelid']
        self.hotelname = data['hotelname']
        self.hotelstars = data['hotelstars']
        self.outbounddeparturedatetime = self.format_time(str(data['outbounddeparturedatetime']))
        self.inbounddeparturedatetime = self.format_time(str(data['inbounddeparturedatetime']))
        self.countadults = data['countadults']
        self.countchildren = data['countchildren']
        self.price = data['price']
        self.inbounddepartureairport = airports.get(data['inbounddepartureairport'], 'Unbekannt')
        self.inboundarrivalairport = airports.get(data['inboundarrivalairport'], 'Unbekannt')
        self.inboundarrivaldatetime = self.format_time(str(data['inboundarrivaldatetime']))
        self.outbounddepartureairport = airports.get(data['outbounddepartureairport'], 'Unbekannt')
        self.outboundarrivalairport = airports.get(data['outboundarrivalairport'], 'Unbekannt')
        self.outboundarrivaldatetime = self.format_time(str(data['outboundarrivaldatetime']))
        self.mealtype = mealtype[data['mealtype']] if data['mealtype'] else 'keine Verpflegung'
        self.oceanview = oceanview[bool(data['oceanview'])] if data['oceanview'] else 'kein Meerblick'
        self.roomtype = roomtype[data['roomtype']] if data['roomtype'] else 'Überraschungszimmer'
        self.score = self.calc_score()

    def get_hotel(self):
        return self.__dict__

    def format_time(self, time):
        date_object = datetime.fromisoformat(time)

        formatted_date = date_object.strftime("%d.%m.%Y um %I:%M %p")

        return formatted_date

    def calc_score(self):
        score = 0

        score += self.hotelstars * 10

        if self.mealtype == 'All Inclusive':
            score += 10
        elif self.mealtype == 'Vollpension':
            score += 7
        elif self.mealtype == 'Halbpension':
            score += 5
        elif self.mealtype == 'Frühstück':
            score += 2

        if self.oceanview == 'Meerblick':
            score += 5

        if self.roomtype == 'Suite':
            score += 10
        elif self.roomtype == 'Juniorsuite':
            score += 7
        elif self.roomtype == 'Familienzimmer':
            score += 5
        elif self.roomtype == 'Doppelzimmer':
            score += 2

        return score
