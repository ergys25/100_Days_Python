from data_manager import DataManager
from pprint import pprint

Sheet_data = DataManager()
data = (Sheet_data.data_saver()["prices"])
pprint(data.City)