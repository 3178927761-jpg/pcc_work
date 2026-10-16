def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("三体")

def calculate_sector (central_angle,radius):
    sector_area=central_angle/360*3.14*radius**2
    print(f"此扇形面积为：{sector_area}")
    return sector_area
sector_area_1=calculate_sector(160,30)
sector_area_2=calculate_sector(60,15)
sector_area_3=calculate_sector(30,16)




def city_county(city,county):
    return f"{city}, {county}"

print(city_county("深圳","中国"))
print(city_county("多伦多","加拿大"))
print(city_county("旧金山","美国"))

