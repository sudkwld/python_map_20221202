#엑셀파일
import pandas as pd
#지도시각화
import folium
map_data = pd.read_csv('test.csv', encoding='cp949')

map =  folium.Map(
    location=[37.5609,127.0664425],
    zoom_start=15,
)

# 위도 정렬
cl_data_lat =  map_data.sort_values(by='latitude', ascending=True)
cl_data_lat_max = map_data.sort_values(by='latitude', ascending=False)
# 경도 정렬
cl_data_lon =  map_data.sort_values(by='longtitude', ascending=True)

#경도 제일 작은 값 : 127.057714, 큰 값 : 127.073711
#위도 제일 작은 값 : 37.55407732, 큰 값 : 37.56352858

#빈배열생성
location_data = []
# base_lat = map_data.values[0][2]

small_data = []

#중복제거(latitude 정렬 오름차순 기준)
for data in cl_data_lat.values:
    if [data[2],data[1]] not in location_data :
        location_data.append([data[2],data[1]])
print(location_data)
# 좌표 개수 : 276

smallest_lat = location_data[0][0]
smallest_lon = location_data[0][1]

for point in location_data :
    latitude = point[0] #'numpy.float64'
    longtitude = point[1] #'numpy.float64'
    folium.Marker (
                    [latitude,longtitude],
                    tooltip='hi'
    ).add_to(map)

    if latitude >= smallest_lat and longtitude >= smallest_lon:
        smallest_lat = latitude
        smallest_lon = longtitude
        small_data.append([latitude,longtitude])

folium.PolyLine(
        [small_data],
        tooltip='line number1'
    ).add_to(map)










location_data_max = []
small_data_max = []

#중복제거(latitude 정렬 내림차순 기준)
for data in cl_data_lat_max.values:
    if [data[2],data[1]] not in location_data_max :
        location_data_max.append([data[2],data[1]])

# 좌표 개수 : 276

smallest_lat_max = location_data_max[0][0]
smallest_lon_max = location_data_max[0][1]

for point in location_data_max :
    latitude_max = point[0] #'numpy.float64'
    longtitude_max = point[1] #'numpy.float64'

    if latitude_max <= smallest_lat_max and longtitude_max >= smallest_lon_max:
        smallest_lat_max = latitude_max
        smallest_lon_max = longtitude_max
        small_data_max.append([latitude_max,longtitude_max])

folium.PolyLine(
        [small_data_max],
        tooltip='line number3'
    ).add_to(map)








# 클릭시 위도,경도 알려줌
map.add_child(folium.LatLngPopup())

#중복제거(longtitude 정렬 기준)
location_data_lon = []

for data in cl_data_lon.values:
    if [data[2],data[1]] not in location_data_lon :
        location_data_lon.append([data[2],data[1]])

smallest_lat_2 = location_data_lon[0][0]
smallest_lon_2 = location_data_lon[0][1]

smallest_arr = []

for point2 in location_data_lon :
    latitude2 = point2[0] #'numpy.float64'
    longtitude2 = point2[1] #'numpy.float64'

    if latitude2 >= smallest_lat_2 and longtitude2 >= smallest_lon_2:
        smallest_lat_2 = latitude2
        smallest_lon_2 = longtitude2
        smallest_arr.append([latitude2,longtitude2])

folium.PolyLine(
        [smallest_arr],
        tooltip='line number2'
    ).add_to(map)

map.save('index.html')

