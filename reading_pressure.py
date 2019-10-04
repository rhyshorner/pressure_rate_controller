
import MCP3201
import time

mcp = MCP3201.MCP3201(0,0)
highest_value = 0
lowest_value = 100

while True:
	pressure = round(mcp.filtered_pressure(), 3)
	if pressure > highest_value:
		highest_value = pressure
	if pressure < lowest_value:
		lowest_value = pressure
	error_margin = round(highest_value - lowest_value, 3)
	print("pressure_ave: " + str(pressure) + " high: " + str(highest_value) + " low: " + str(lowest_value) + " error: " + str(error_margin))

	time.sleep(0.25)
