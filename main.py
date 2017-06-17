import network, badge, ugfx, json
import urequests as requests

apikey = "e502c2eb253e6a6712cb0a06906832d6"

sta_if = network.WLAN(network.STA_IF);
sta_if.active(True)
sta_if.connect("revspace-pub-2.4ghz")
sta_if.isconnected()

badge.init()
ugfx.init()


# loading screen
ugfx.clear();
ugfx.string(10,10,"calling the stars...","Roboto_Regular12", 0)
ugfx.flush()

# fetching forecast data
url = "https://api.darksky.net/forecast/"+apikey+"/37.8267,-122.4233?units=ca"
r = requests.get(url)
data = r.json()
r.close()

# displaying forecast
ugfx.clear();
ugfx.string(5, 5, "Vienna, 04.08.2017", "Roboto_Regular12", 0)

ugfx.string(9, 20, "MORNING", "Roboto_Regular12", 0)
ugfx.string(92, 20, "NOON", "Roboto_Regular12", 0)
ugfx.string(158, 20, "EVENING", "Roboto_Regular12", 0)
ugfx.string(240, 20, "NIGHT", "Roboto_Regular12", 0)

#xi = 2
#for point in data["hourly"]["data"]:
#    ugfx.area(xi, 0, 5, int(point["temperature"]) * 3, 0)
#    xi += 6

#for point in data["hourly"]["data"]:
#    print(point["icon"])

ugfx.box(5, 59, 64, 64, 0)
ugfx.box(5 + 1*10 + 1* 64, 59, 64, 64, 0)
ugfx.box(5 + 2*10 + 2* 64, 59, 64, 64, 0)
ugfx.box(5 + 3*10 + 3* 64, 59, 64, 64, 0)


ugfx.flush();
