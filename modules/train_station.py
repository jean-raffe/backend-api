import json

# 加载存储着站点映射关系的station.json
with open('station.json', 'r', encoding='utf-8') as f:
    station_mapping = json.load(f)

# 处理端点传入的数据，并返回映射后的结果
def train_station_mapping(data):

    # 获取日期、目的地和出发地点
    date = data.get('date')
    destination = data.get('destination')
    departure_point = data.get('departure_point')

    # 将中文站点名映射为标识符
    destination_code = station_mapping.get(destination, '未知站点')
    departure_point_code = station_mapping.get(departure_point, '未知站点')

    # 构建返回结果
    result = {
        'date': date,
        'destination': destination_code,
        'departure_point': departure_point_code
    }

    return result
