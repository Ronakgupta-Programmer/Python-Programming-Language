import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests

# Sample data for countries, states, and cities
data ={
    "United States": {
        "Alabama": ["Birmingham", "Montgomery", "Huntsville", "Mobile", "Tuscaloosa", "Hoover", "Dothan", "Auburn", "Decatur", "Madison"],
        "Alaska": ["Anchorage", "Juneau", "Fairbanks", "Sitka", "Ketchikan", "Wasilla", "Kenai", "Kodiak", "Bethel", "Palmer"],
        "Arizona": ["Phoenix", "Tucson", "Mesa", "Chandler", "Glendale", "Scottsdale", "Gilbert", "Tempe", "Peoria", "Flagstaff"],
        "Arkansas": ["Little Rock", "Fayetteville", "Fort Smith", "Springdale", "Jonesboro", "North Little Rock", "Conway", "Rogers", "Pine Bluff", "Benton"],
        "California": ["Los Angeles", "San Francisco", "San Diego", "San Jose", "Fresno", "Sacramento", "Long Beach", "Santa Ana", "Anaheim", "Bakersfield"],
        "Colorado": ["Denver", "Colorado Springs", "Aurora", "Fort Collins", "Lakewood", "Thornton", "Arvada", "Westminster", "Pueblo", "Boulder"],
        "Connecticut": ["Hartford", "Bridgeport", "New Haven", "Stamford", "Waterbury", "Norwalk", "Danbury", "New Britain", "Meriden", "Bristol"],
        "Delaware": ["Wilmington", "Dover", "Newark", "Middletown", "Smyrna", "New Castle", "Georgetown", "Bear", "Brookside", "Claymont"],
        "Florida": ["Miami", "Orlando", "Tampa", "Jacksonville", "St. Petersburg", "Hialeah", "Tallahassee", "Fort Lauderdale", "Cape Coral", "Pembroke Pines"],
        "Georgia": ["Atlanta", "Savannah", "Augusta", "Columbus", "Macon", "Roswell", "Albany", "Sandy Springs", "Athens", "Warner Robins"],
        "Hawaii": ["Honolulu", "Hilo", "Kailua", "Kaneohe", "Waipahu", "Mililani Mauka", "Lahaina", "Kahului", "Aiea", "Wahiawa"],
        "Idaho": ["Boise", "Nampa", "Pocatello", "Meridian", "Idaho Falls", "Caldwell", "Coeur d'Alene", "Twin Falls", "Lewiston", "Rexburg"],
        "Illinois": ["Chicago", "Aurora", "Naperville", "Rockford", "Joliet", "Elgin", "Peoria", "Champaign", "Waukegan", "Cicero"],
        "Indiana": ["Indianapolis", "Fort Wayne", "Evansville", "South Bend", "Carmel", "Fishers", "Gary", "Muncie", "Lafayette", "Terre Haute"],
        "Iowa": ["Des Moines", "Cedar Rapids", "Davenport", "Sioux City", "Iowa City", "Waterloo", "Ames", "West Des Moines", "Council Bluffs", "Ankeny"],
        "Kansas": ["Topeka", "Wichita", "Olathe", "Overland Park", "Lawrence", "Shawnee", "Manhattan", "Lenexa", "Salina", "Hutchinson"],
        "Kentucky": ["Louisville", "Lexington", "Bowling Green", "Owensboro", "Covington", "Richmond", "Florence", "Georgetown", "Nicholasville", "Elizabethtown"],
        "Louisiana": ["New Orleans", "Baton Rouge", "Shreveport", "Lafayette", "Lake Charles", "Kenner", "Bossier City", "Monroe", "Alexandria", "Central"],
        "Maine": ["Portland", "Augusta", "Bangor", "South Portland", "Westbrook", "Scarborough", "Saco", "Biddeford", "Sanford", "Brunswick"],
        "Maryland": ["Baltimore", "Annapolis", "Frederick", "Gaithersburg", "Bowie", "Rockville", "Hagerstown", "Salisbury", "Laurel", "Bel Air"],
        "Massachusetts": ["Boston", "Worcester", "Springfield", "Cambridge", "Lowell", " Brockton", "New Bedford", "Quincy", "Lynn", "Fall River"],
        "Michigan": ["Detroit", "Grand Rapids", "Ann Arbor", "Warren", "Sterling Heights", "Lansing", "Flint", "Dearborn", "Livonia", "Troy"],
        "Minnesota": ["Minneapolis", "Saint Paul", "Rochester", "Bloomington", "Duluth", "Brooklyn Park", "Plymouth", "Woodbury", "Eagan", "Minnetonka"],
        "Mississippi": ["Jackson", "Gulfport", "Southaven", "Hattiesburg", "Biloxi", "Meridian", "Tupelo", "Olive Branch", "Pearl", "Madison"],
        "Missouri": ["Kansas City", "Saint Louis", "Springfield", "Columbia", "Lee's Summit", "St. Joseph", "O'Fallon", "Independence", "Florissant", "Jefferson City"],
        "Montana": ["Billings", "Missoula", "Great Falls", "Bozeman", "Butte", "Helena", "Kalispell", "Havre", "Anaconda", "Miles City"],
        "Nebraska": ["Lincoln", "Omaha", "Bellevue", "Grand Island", "Kearney", "Fremont", "Hastings", "North Platte", "Papillion", "Columbus"],
        "Nevada": ["Las Vegas", "Reno", "Carson City", "Henderson", "North Las Vegas", "Sparks", "Elko", "Mesquite", "Fallon", "Boulder City"],
        "New Hampshire": ["Concord", "Manchester", "Nashua", "Derry", "Rochester", "Salem", "Keene", "Laconia", "Hudson", "Portsmouth"],
        "New Jersey": ["Trenton", "Newark", "Jersey City", "Paterson", "Elizabeth", "Edison", "Woodbridge", "Lakewood", "Toms River", "Hamilton"],
        "New Mexico": ["Albuquerque", "Santa Fe", "Las Cruces", "Rio Rancho", "Roswell", "Farmington", "Clovis", "Carlsbad", "Hobbs", "Alamogordo"],
        "New York": ["New York City", "Buffalo", "Rochester", "Yonkers", "Syracuse", "Albany", "New Rochelle", "Mount Vernon", "Schenectady", "Utica"],
        "North Carolina": ["Charlotte", "Raleigh", "Greensboro", "Durham", "Winston-Salem", "Fayetteville", "Cary", "High Point", "Concord", "Gastonia"],
        "North Dakota": ["Bismarck", "Fargo", "Grand Forks", "Minot", "West Fargo", "Dickinson", "Williston", "Jamestown", "Mandan", "Lakewood"],
        "Ohio": ["Columbus", "Cleveland", "Cincinnati", "Toledo", "Akron", "Dayton", "Parma", "Canton", "Youngstown", "Lorain"],
        "Oklahoma": ["Oklahoma City", "Tulsa", "Norman", "Broken Arrow", "Edmond", "Lawton", "Moore", "Midwest City", "Enid", "Stillwater"],
        "Oregon": ["Portland", "Salem", "Eugene", "Gresham", "Hillsboro", "Beaverton", "Bend", "Medford", "Springfield", "Corvallis"],
        "Pennsylvania": ["Philadelphia", "Pittsburgh", "Allentown", "Erie", "Reading", "Scranton", "Bethlehem", "Lancaster", "Harrisburg", "York"],
        "Rhode Island": ["Providence", "Warwick", "Cranston", "Pawtucket", "East Providence", "North Providence", "South Kingstown", "Coventry", "Woonsocket", "Narragansett"],
        "South Carolina": ["Columbia", "Charleston", "Greenville", "Mount Pleasant", "Rock Hill", "Summerville", "Goose Creek", "Myrtle Beach", "Florence", "Anderson"],
        "South Dakota": ["Pierre", "Sioux Falls", "Rapid City", "Aberdeen", "Brookings", "Mitchell", "Huron", "Yankton", "Watertown", "Spearfish"],
        "Tennessee": ["Nashville", "Memphis", "Knoxville", "Chattanooga", "Clarksville", "Murfreesboro", "Jackson", "Johnson City", "Smyrna", "Hendersonville"],
        "Texas": ["Houston", "Dallas", "Austin", "San Antonio", "Fort Worth", "El Paso", "Arlington", "Corpus Christi", "Plano", "Laredo"],
        "Utah": ["Salt Lake City", "Provo", "West Valley City", "West Jordan", "Orem", "Sandy", "Layton", "South Jordan", "Logan", "Lehi"],
        "Vermont": ["Montpelier", "Burlington", "South Burlington", "Rutland", "Barre", "Winooski", "Stowe", "Montpelier", "Essex", "Brattleboro"],
        "Virginia": ["Virginia Beach", "Norfolk", "Chesapeake", "Richmond", "Newport News", "Alexandria", "Hampton", "Roanoke", "Lynchburg", "Suffolk"],
        "Washington": ["Seattle", "Spokane", "Tacoma", "Vancouver", "Bellevue", "Kent", "Everett", "Renton", "Richland", "Bellingham"],
        "West Virginia": ["Charleston", "Huntington", "Morgantown", "Parkersburg", "Weirton", "Wheeling", "Fairmont", "South Charleston", "Clarksburg", "Lewisburg"],
        "Wisconsin": ["Milwaukee", "Madison", "Green Bay", "Kenosha", "Racine", "Appleton", "Waukesha", "Sheboygan", "Eau Claire", "Oshkosh"],
        "Wyoming": ["Cheyenne", "Casper", "Laramie", "Gillette", "Rock Springs", "Sheridan", "Jackson", "Evanston", "Green River", "Riverton"],
    },
    "India": {
        "Andaman and Nicobar Islands": ["Port Blair", "Havelock", "Neil Island", "Diglipur", "Baratang"],
        "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Nellore", "Tirupati", "Kakinada", "Kadapa", "Rajahmundry", "Anantapur", "Chittoor"],
        "Arunachal Pradesh": ["Itanagar", "Naharlagun", "Pasighat", "Tezpur", "Bomdila"],
        "Assam": ["Guwahati", "Silchar", "Dibrugarh", "Nagaon", "Tezpur"],
        "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga"],
        "Chandigarh": ["Chandigarh"],
        "Chhattisgarh": ["Raipur", "Bhilai", "Durg", "Korba", "Bilaspur"],
        "Dadra and Nagar Haveli": ["Silvassa"],
        "Daman and Diu": ["Daman", "Diu"],
        "Delhi": ["New Delhi", "North Delhi", "South Delhi", "East Delhi", "West Delhi"],
        "Goa": ["Panaji", "Margao", "Mapusa", "Pernem", "Ponda"],
        "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Junagadh", "Anand", "Nadiad", "Gandhinagar"],
        "Haryana": ["Chandigarh", "Gurugram", "Faridabad", "Panipat", "Ambala"],
        "Himachal Pradesh": ["Shimla", "Dharamshala", "Kullu", "Manali", "Solan"],
        "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Deoghar"],
        "Karnataka": ["Bangalore", "Mysore", "Mangalore", "Belgaum", "Hubli", "Dharwad", "Davangere", "Ballari", "Tumkur", "Udupi"],
        "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Kottayam", "Malappuram"],
        "Lakshadweep": ["Kavaratti"],
        "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Thane", "Solapur", "Kalyan", "Dombivli", "Bhiwandi"],
        "Manipur": ["Imphal", "Thoubal", "Kakching", "Churachandpur", "Tamenglong"],
        "Meghalaya": ["Shillong", "Tura", "Jowai", "Nongpoh", "Baghmara"],
        "Mizoram": ["Aizawl", "Lunglei", "Siaha", "Khawzawl", "Champhai"],
        "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Wokha", "Tuensang"],
        "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Berhampur", "Sambalpur"],
        "Punjab": ["Chandigarh", "Amritsar", "Ludhiana", "Jalandhar", "Patiala", "Bathinda", "Mohali", "Rupnagar", "Hoshiarpur", "Fatehgarh Sahib"],
        "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Ajmer", "Bikaner", "Bhilwara", "Sikar", "Tonk", "Kota", "Chittorgarh"],
        "Sikkim": ["Gangtok", "Namchi", "Mangan", "Gyalshing", "Pelling"],
        "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli", "Erode", "Vellore", "Thanjavur", "Kanyakumari"],
        "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam", "Mahbubnagar", "Ranga Reddy", "Nalgonda", "Adilabad", "Medak"],
        "Tripura": ["Agartala", "Udaipur", "Dharmanagar", "Ambassa", "Kailashahar"],
        "Uttar Pradesh": ["Lucknow", "Kanpur", "Ghaziabad", "Agra", "Varanasi", "Allahabad", "Meerut", "Noida", "Aligarh", "Merrut"],
        "Uttarakhand": ["Dehradun", "Haridwar", "Nainital", "Rudrapur", "Roorkee"],
        "West Bengal": ["Kolkata", "Siliguri", "Durgapur", "Asansol", "Bardhaman", "Berhampore", "Malda", "Kalyani", "Howrah", "Haldia"],
        "Haryana": ["Gurgaon", "Faridabad", "Ambala", "Rohtak", "Sonipat"],
        "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga"],
        "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain"],
        "Uttarakhand": ["Dehradun", "Nainital", "Rudrapur", "Haridwar", "Roorkee"],
    },
    "Australia": {
        "New South Wales": ["Sydney", "Newcastle", "Wollongong"],
        "Victoria": ["Melbourne", "Geelong", "Ballarat"],
        "Queensland": ["Brisbane", "Gold Coast", "Cairns"],
        "Western Australia": ["Perth", "Bunbury", "Mandurah"],
    },
    "Canada": {
        "Ontario": ["Toronto", "Ottawa", "Hamilton"],
        "British Columbia": ["Vancouver", "Victoria", "Kelowna"],
        "Alberta": ["Calgary", "Edmonton", "Red Deer"],
    },
    "Germany": {
        "Bavaria": ["Munich", "Nuremberg", "Augsburg"],
        "Berlin": ["Berlin"],
        "North Rhine-Westphalia": ["Cologne", "Düsseldorf", "Dortmund"],
    },
    "United Kingdom": {
        "England": ["London", "Birmingham", "Manchester"],
        "Scotland": ["Edinburgh", "Glasgow", "Aberdeen"],
        "Wales": ["Cardiff", "Swansea", "Newport"],
    },
    "France": {
        "Île-de-France": ["Paris", "Versailles", "Saint-Denis"],
        "Provence-Alpes-Côte d'Azur": ["Marseille", "Nice", "Toulon"],
        "Auvergne-Rhône-Alpes": ["Lyon", "Grenoble", "Saint-Étienne"],
    },
    "Brazil": {
        "São Paulo": ["São Paulo", "Campinas", "Santos"],
        "Rio de Janeiro": ["Rio de Janeiro", "Niterói", "Petrópolis"],
        "Minas Gerais": ["Belo Horizonte", "Uberlândia", "Juiz de Fora"],
    },
    "Mexico": {
        "Jalisco": ["Guadalajara", "Puerto Vallarta", "Tlaquepaque"],
        "Mexico City": ["Mexico City"],
        "Nuevo León": ["Monterrey", "San Pedro Garza García", "Santa Catarina"],
    },
    "Italy": {
        "Lazio": ["Rome", "Viterbo", "Frosinone"],
        "Lombardy": ["Milan", "Bergamo", "Brescia"],
        "Campania": ["Naples", "Salerno", "Caserta"],
    },
    "Japan": {
        "Tokyo": ["Tokyo", "Yokohama", "Kawasaki"],
        "Osaka": ["Osaka", "Kobe", "Kyoto"],
        "Hokkaido": ["Sapporo", "Hakodate", "Otaru"],
    },
    "Russia": {
        "Moscow": ["Moscow"],
        "Saint Petersburg": ["Saint Petersburg"],
        "Siberia": ["Novosibirsk", "Omsk", "Krasnoyarsk"],
    },
    "South Africa": {
        "Gauteng": ["Johannesburg", "Pretoria", "Sandton"],
        "Western Cape": ["Cape Town", "Paternoster", "Stellenbosch"],
        "KwaZulu-Natal": ["Durban", "Pietermaritzburg", "Newcastle"],
    },
    "China": {
        "Beijing": ["Beijing"],
        "Shanghai": ["Shanghai"],
        "Sichuan": ["Chengdu", "Mianyang", "Deyang"],
    },
    "South Korea": {
        "Seoul": ["Seoul"],
        "Busan": ["Busan"],
        "Incheon": ["Incheon"],
    },
    "Argentina": {
        "Buenos Aires": ["Buenos Aires"],
        "Córdoba": ["Córdoba", "Villa María", "Río Cuarto"],
        "Santa Fe": ["Santa Fe", "Rosario", "Venado Tuerto"],
    },
    "Colombia": {
        "Bogotá": ["Bogotá"],
        "Antioquia": ["Medellín", "Envigado", "Itagüí"],
        "Valle del Cauca": ["Cali", "Palmira", "Buenaventura"],
    },
    "Nigeria": {
        "Lagos": ["Lagos"],
        "Abuja": ["Abuja"],
        "Rivers": ["Port Harcourt"],
    },
    "Turkey": {
        "Istanbul": ["Istanbul"],
        "Ankara": ["Ankara"],
        "Izmir": ["Izmir"],
    },
    "Vietnam": {
        "Hanoi": ["Hanoi"],
        "Ho Chi Minh City": ["Ho Chi Minh City"],
        "Da Nang": ["Da Nang"],
    },
    "Philippines": {
        "Metro Manila": ["Quezon City", "Makati", "Manila"],
        "Cebu": ["Cebu City", "Lapu-Lapu City", "Mandaue"],
    },
    "Sweden": {
        "Stockholm": ["Stockholm"],
        "Gothenburg": ["Gothenburg"],
        "Malmö": ["Malmö"],
    },
    "Finland": {
        "Helsinki": ["Helsinki"],
        "Espoo": ["Espoo"],
        "Vantaa": ["Vantaa"],
    },
    "Norway": {
        "Oslo": ["Oslo"],
        "Bergen": ["Bergen"],
        "Stavanger": ["Stavanger"],
    },
    "Denmark": {
        "Copenhagen": ["Copenhagen"],
        "Aarhus": ["Aarhus"],
        "Odense": ["Odense"],
    },
    "Switzerland": {
        "Zurich": ["Zurich"],
        "Geneva": ["Geneva"],
        "Bern": ["Bern"],
    },
    "Austria": {
        "Vienna": ["Vienna"],
        "Graz": ["Graz"],
        "Salzburg": ["Salzburg"],
    },
    "Ireland": {
        "Dublin": ["Dublin"],
        "Cork": ["Cork"],
        "Limerick": ["Limerick"],
    },
    "New Zealand": {
        "Auckland": ["Auckland"],
        "Wellington": ["Wellington"],
        "Christchurch": ["Christchurch"],
    },
    "Singapore": {
        "Central Region": ["Singapore"],
    },
    "Israel": {
        "Tel Aviv": ["Tel Aviv"],
        "Jerusalem": ["Jerusalem"],
        "Haifa": ["Haifa"],
    },
    "Saudi Arabia": {
        "Riyadh": ["Riyadh"],
        "Jeddah": ["Jeddah"],
        "Mecca": ["Mecca"],
    },
    "Qatar": {
        "Doha": ["Doha"],
    },
    "UAE": {
        "Dubai": ["Dubai"],
        "Abu Dhabi": ["Abu Dhabi"],
        "Sharjah": ["Sharjah"],
    },
}

# Function to update states based on selected country
def update_states(event):
    country = country_combobox.get()
    states = data.get(country, {}).keys()
    state_combobox['values'] = list(states)
    state_combobox.set("Select a state")
    city_combobox['values'] = []  # Clear city options

# Function to update cities based on selected state
def update_cities(event):
    country = country_combobox.get()
    state = state_combobox.get()
    cities = data.get(country, {}).get(state, [])
    city_combobox['values'] = cities
    city_combobox.set("Select a city")

# Function to fetch weather data
def get_weather():
    api_key = "91cf9df4f9cdb92a6ab2a86a1e5ecb68"  # Replace with your OpenWeatherMap API key
    country = country_combobox.get()
    state = state_combobox.get()
    city = city_combobox.get()

    if not city or city == "Select a city":
        messagebox.showwarning("Input Error", "Please select a city.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()  # Get JSON data from response
            temperature = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            result_label.config(text=f"Temperature: {temperature}°C\nDescription: {weather_desc.capitalize()}")
        else:
            messagebox.showerror("Error", data['message'])
    
    except Exception as e:
        messagebox.showerror("Error", "Could not fetch weather data. Please try again.")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("600x400")
root.configure(bg="#2c3e50")  # Set a background color

# GUI Layout
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=20)

# Left side for Country
country_label = tk.Label(frame, text="Select Country:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 14))
country_label.grid(row=0, column=0, padx=20, pady=10)

country_combobox = ttk.Combobox(frame, values=list(data.keys()), width=20, font=("Helvetica", 14))
country_combobox.grid(row=1, column=0, padx=20, pady=5)
country_combobox.set("Select a country")
country_combobox.bind("<<ComboboxSelected>>", update_states)  # Update states on selection

# Center for State
state_label = tk.Label(frame, text="Select State:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 14))
state_label.grid(row=0, column=1, padx=20, pady=10)

state_combobox = ttk.Combobox(frame, values=[], width=20, font=("Helvetica", 14))
state_combobox.grid(row=1, column=1, padx=20, pady=5)
state_combobox.set("Select a state")
state_combobox.bind("<<ComboboxSelected>>", update_cities)  # Update cities on selection

# Right side for City
city_label = tk.Label(frame, text="Select City:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 14))
city_label.grid(row=0, column=2, padx=20, pady=10)

city_combobox = ttk.Combobox(frame, values=[], width=20, font=("Helvetica", 14))
city_combobox.grid(row=1, column=2, padx=20, pady=5)
city_combobox.set("Select a city")

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 14), bg="#27ae60", fg="white")
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1")
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()