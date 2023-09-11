import pyodide_http
import requests
from datetime import datetime as dt
from datetime import timedelta as td
from matplotlib import pyplot as plt

        
pyodide_http.patch_all()
STATION = "KCLT"

def capture_historical_data():
    """Function to capture the last 36 hours of weather data (currently) from the CLT airport station"""
    # NWS api reports data using UTC time. The following 4 lines create a current datetime object (in utc), calculates the time 24 hours earlier, converts both to isoformat, then edits the isoformat to match the NWS api's expected parameter format
    now = dt.utcnow()
    zulu_now_raw = (now).isoformat()
    zulu_then_raw = (now + td(hours=-36)).isoformat()
    zulu_now = zulu_now_raw.replace(zulu_now_raw[19:], "Z")
    zulu_then = zulu_then_raw.replace(zulu_then_raw[19:], "Z")
   
    # format url to capture the last 24 hours data
    url = f"https://api.weather.gov/stations/{STATION}/observations?start={zulu_then}&end={zulu_now}"

    response = requests.get(url)
    return response.json()


def c_to_f(temp_c):
    """Convert celsius to fahrenheit"""
    return (temp_c * (9/5) + 32)


def pa_to_in(pa):
    """NWS reports barometric pressure in Paschals. This function converts Paschals to inches of Mercury (inHg)"""
    return (pa / 3386)
    # return (pa)


def plot_temps(times, temps):
    """Create plot of temperatures over the last 24 hours"""
    plt.plot(times, temps)
    plt.title("Temp History")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.xticks(rotation=90)
    plt.subplots_adjust(left=.12, right=1, bottom=.485)
    plt.grid()
    display(plt, target="display_temps")


def plot_pressures(times, pressures):
    """Create plot of barometric pressures over the last 24 hours"""
    plt.figure(figsize=(10,6))
    plt.plot(times, pressures)
    plt.title("Barometric Pressure History")
    plt.xlabel("Time")
    plt.ylabel("Pressure")
    plt.xticks(rotation=90)
    
    plt.subplots_adjust(left=.12, right=1, bottom=.485)
    plt.grid()
    display(plt, target="display_pressure")



def display_history():
    data = capture_historical_data()
    times = []
    temps = []
    pressures = []
    for n in data['features'][-1::-1]:
        zulu_timestamp = n['properties']['timestamp']
        # convert utc time to local time for the graph
        timestamp = str(dt.astimezone(dt.fromisoformat(zulu_timestamp)))

        # Try/except blocks handle gaps in data
        try:
            temp = c_to_f(float(n['properties']['temperature']['value']))
        except TypeError:
            temp = None
        try:
            pressure = pa_to_in(float(n['properties']['barometricPressure']['value']))
        except:
            pressure = None
        times.append(timestamp)
        temps.append(temp)
        pressures.append(pressure)
    # plot_temps(times, temps)
    plot_pressures(times, pressures)