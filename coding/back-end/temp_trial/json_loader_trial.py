import json

# The JSON data
json_data = '{"type":"chat2data_endpoint","data":{"columns":[{"col":"name","data_type":"VARCHAR","nullable":true},{"col":"average_age","data_type":"DOUBLE","nullable":true}],"rows":[{"average_age":"21","name":"Orduspor"},{"average_age":"21","name":"Akhisarspor"},{"average_age":"21.4","name":"Bursaspor"},{"average_age":"21.6","name":"FC Nordsjaelland"},{"average_age":"22","name":"Balikesirspor"}],"result":{"code":200,"message":"Query OK!","start_ms":1689643589903,"end_ms":1689643595333,"latency":"5.430048563s","row_count":5,"row_affect":0,"limit":50,"sql":"SELECT `name`, `average_age` FROM `Football_Club` WHERE `average_age` \u003e 0 AND `average_age` IS NOT NULL ORDER BY `average_age` ASC LIMIT 5;","ai_latency":"5.400326162s","databases":["Football_Club"]}}}'

# Parse the JSON data into a Python dictionary
data_dict = json.loads(json_data)

# Extract the "data" and "code" fields
data_column = data_dict.get('data', {}).get('columns', {}) 
data_row = data_dict.get('data', {}).get('rows', {})
code = data_dict.get('data', {}).get('result', {}).get('code')

# Print the extracted values
print("Data:")
# print(data_column)
print(data_row)
print("Code:", code)