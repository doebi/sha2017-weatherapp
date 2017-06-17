import network, badge, ugfx, json
from time import *
import urequests as requests

apikey = ""

sta_if = network.WLAN(network.STA_IF);
sta_if.active(True)
sta_if.connect("revspace-pub-2.4ghz")
sta_if.isconnected()

badge.init()
ugfx.init()

icons = {
"clear-day": "\uf00d",
"clear-night": "\uf02e",
"rain": "\uf019",
"snow": "\uf01b",
"sleet": "\uf0b5",
"wind": "\uf050",
"fog": "\uf021",
"cloudy": "\uf041",
"partly-cloudy-day": "\uf002",
"partly-cloudy-night": "\uf086"
}

def getDisplayName(time):
    #if time[3] == 0:
    #    n = "Night"
    #if time[3] == 6:
    #    n = "Morning"
    #if time[3] == 12:
    #    n = "Noon"
    #if time[3] == 18:
    #    n = "Evening"
    #return str(time[2]) + "." + str(time[1]) + ". " + n
    return str(time[2]) + "." + str(time[1]) + ". " + str(time[3]) + ":00"

# loading screen
ugfx.clear();
ugfx.string(10,10,"calling the stars...","Roboto_Regular12", 0)
ugfx.flush()

# fetching forecast data
url = "https://api.darksky.net/forecast/"+apikey+"/52.3451,5.4581?units=ca"
r = requests.get(url)
data = r.json()
r.close()

# aligning according to time
hourly = data["hourly"]["data"]
starttime = localtime(hourly[0]["time"])
if starttime[3] > 6:
    index = 12 - starttime[3]

if starttime[3] > 12:
    index = 18 - starttime[3]

if starttime[3] > 18:
    index = 24 - starttime[3]

timepos = (10, 30)
iconpos = (10, 44)
temppos = (0, 100)

# displaying forecast
ugfx.clear();
ugfx.line(0, 26, 296, 26, 0)
ugfx.line(0, 44, 296, 44, 0)
ugfx.string(5, 5, "Weather Forecast for: Zeewolde, NL", "pixelade13", 0)

dp = hourly[index]
time = localtime(dp["time"])
ugfx.string(timepos[0], timepos[1], getDisplayName(time), "pixelade13", 0)
ugfx.string(iconpos[0], iconpos[1], icons[dp["icon"]], "weather42", 0)
ugfx.string(temppos[0], temppos[1], str(int(dp["temperature"]))+"°C", "DejaVuSansMono20", 0)

dp = hourly[index+6]
time = localtime(dp["time"])
ugfx.string(timepos[0] + 1*11 + 1*64, timepos[1], getDisplayName(time), "pixelade13", 0)
ugfx.string(iconpos[0] + 1*11 + 1*64, iconpos[1], icons[dp["icon"]], "weather42", 0)
ugfx.string(temppos[0] + 1*11 + 1*64, temppos[1], str(int(dp["temperature"]))+"°C", "DejaVuSansMono20", 0)

dp = hourly[index+12]
time = localtime(dp["time"])
ugfx.string(timepos[0] + 2*11 + 2*64, timepos[1], getDisplayName(time), "pixelade13", 0)
ugfx.string(iconpos[0] + 2*11 + 2*64, iconpos[1], icons[dp["icon"]], "weather42", 0)
ugfx.string(temppos[0] + 2*11 + 2*64, temppos[1], str(int(dp["temperature"]))+"°C", "DejaVuSansMono20", 0)

dp = hourly[index+18]
time = localtime(dp["time"])
ugfx.string(timepos[0] + 3*11 + 3*64, timepos[1], getDisplayName(time), "pixelade13", 0)
ugfx.string(iconpos[0] + 3*11 + 3*64, iconpos[1], icons[dp["icon"]], "weather42", 0)
ugfx.string(temppos[0] + 3*11 + 3*64, temppos[1], str(int(dp["temperature"]))+"°C", "DejaVuSansMono20", 0)

ugfx.flush();

while True:
    pass
