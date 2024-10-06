from flask import Flask, request, jsonify
from train_handler import train_station_mapping
# 新的导入

app = Flask(__name__)

# 火车票站点-标识符映射 /v1/train/direct 方法：POST
@app.route('/v1/train/station', methods=['POST'])
def train_station():
    try:
 
        data = request.get_json()


        result = train_station_mapping(data)


        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# 新的路由
# 新的路由函数

if __name__ == '__main__':
    app.run(port=422)
