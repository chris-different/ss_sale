import redis



r = redis.StrictRedis(host='127.0.0.1',port=6379,db=0)

keys = r.keys()


def get_data_json():
    datas = []
    for key in keys:
        key_data = {}
        key_data['f_id'] = int(str(r.hget(key,"f_id"),encoding='utf-8'))
        key_data['name'] = str(r.hget(key, "name"),encoding='utf-8')
        key_data['flow_market_price'] = str(r.hget(key, "flow_market_price"),encoding='utf-8')
        key_data['price'] = str(r.hget(key, "price"),encoding='utf-8')
        key_data['flow_amount'] = str(r.hget(key, "flow_amount"),encoding='utf-8')
        key_data['trade_amount'] = str(r.hget(key, "trade_amount"),encoding='utf-8')
        key_data['price_change'] = str(r.hget(key, "price_change"),encoding='utf-8')
        datas.append(key_data)
    return datas


if __name__ == '__main__':
    get_data = get_data_json()
    print(get_data)
