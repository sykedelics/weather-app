import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout    
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty  
from kivy.network.urlrequest import UrlRequest


API='a972a6382875b76deb5a618caca9de6c'

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/" + "find?q={}&type=like&APPID="+API
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url,self.found_location)

    def found_location(self, request, data):
        data=json.loads(data.decode()) if not isinstance(data, dict) else data
        cities=["{}({})".format(data['name'],data['sys']['country'])]
        self.search_results=[{'text':str(x)}for x in cities]
        print(f"self.search_results.data={self.search_results.data}")

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV,self).__init__(**kwargs)
        self.data=[]

class WeatherApp(App):
    pass

if __name__=='__main__':
    WeatherApp().run()
