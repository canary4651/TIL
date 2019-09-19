# PYTHON3-10

- 공공데이터포털
    - [https://www.data.go.kr/](https://www.data.go.kr/)
- 전국동물보호센터정보표준데이터
    - [https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20190908/python/animal.ipynb](https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20190908/python/animal.ipynb)
- 전국전통시장표준데이터
    - [https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20190908/python/traditional-market.ipynb](https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20190908/python/traditional-market.ipynb)
- 전국 유치원
    - [https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20190908/python/child-house.ipynb](https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20190908/python/child-house.ipynb)

    - [https://github.com/ahastudio/CodingLife/blob/master/20190908/python/geocoder.py](https://github.com/ahastudio/CodingLife/blob/master/20190908/python/geocoder.py)
        - 카카오 주소 데이터 가져다 사용할 수 있는 문법

    [https://developers.kakao.com/docs/restapi/local](https://developers.kakao.com/docs/restapi/local) : 카카오 주소 데이터 

    [https://jsonformatter.curiousconcept.com/](https://jsonformatter.curiousconcept.com/)

        import os
        import requests
        
        
        key = os.environ['KAKAO_REST_API_KEY']
        
        
        def geocode(address):
            url = 'https://dapi.kakao.com/v2/local/search/address.json'
            params = {'query': address}
            headers = {'Authorization': 'KakaoAK ' + key}
            r = requests.get(url, params=params, headers=headers) #get: url 주소 쳐서 이동하는 것
            results = r.json()['documents']
            if not results:
                return None, None
            address = results[0]['address']
            return float(address['y']), float(address['x'])
        
        
        if __name__ == '__main__':
            lat, lng = geocode('서울특별시 마포구 백범로31길 21 창업허브')
            assert lat == 37.54674671893906
            assert lng == 126.94997413872638

    - api : 데이터를 쉽게 가져오기 위한 규칙
    - 지도 - 위도와 경도 값을 알아야 함

    ## 폰트를 찾아서 쓰고 싶어요

    import matplotlib.font_manager as fm

    [font for font in fm.fontManager.ttflist if 'Gothic' in font.name]

    ⇒ 결과 중에 'AppleGothic'이 보입니다.

    plt.rcParams['font.family'] = 'AppleGothic'

    ## 카카오맵 API의 키를 입력하고 싶어요

    # 터미널에서 주피터 노트북을 실행하기 전에 이걸 꼭 해주세요!

    export KAKAO_REST_API_KEY=카카오_앱_REST_API_키

    jupyter notebook

    a5ac7934267c122840d131cb73d12378

        from geocoder import geocode
        
        geocode('강원도 원주시 시청로 496-1 101동 102호(관설동, 코아루아파트)')

    → 무슨 말일까? 

    유치원 주피터에서 

    카카오톡 개발자포럼 가입 - reset api 키 발급 

    주피터 키기 전에 터미널에서 

    export KAKAO_REST_API_KEY=카카오_앱_REST_API_키 (a5ac7934267c122840d131cb73d12378) → 내가 발급받은 키 

    그리고 jupyter notebook