# 특강/HTML+CSS

- 특강 요약

    웹각화를 위해 미리 보면 좋을 것들* HTML :

    [https://www.w3schools.com/html/default.asp](https://www.w3schools.com/html/default.asp)

    * CSS :

    [https://www.w3schools.com/css/default.asp](https://www.w3schools.com/css/default.asp)

    * JavaScript

    *

    [https://www.w3schools.com/js/default.asp](https://www.w3schools.com/js/default.asp)

    *

    [https://www.youtube.com/watch?v=W6NZfCO5SIk](https://www.youtube.com/watch?v=W6NZfCO5SIk)

    * Chart.js

    *

    [https://www.chartjs.org](https://www.chartjs.org/)

    * 데이터 시각화 비교분석

    *

    [https://github.com/NeuroAssociates/DataVisualizationReport](https://github.com/NeuroAssociates/DataVisualizationReport)

    [w3schools.com](http://w3schools.com/)

    HTML TutorialWell organized and easy to understand Web building tutorials with lots of examples of how to use HTML, CSS, JavaScript, SQL, PHP, Python, Bootstrap, Java and XML.

    [w3schools.com](http://w3schools.com/)

    CSS TutorialWell organized and easy to understand Web building tutorials with lots of examples of how to use HTML, CSS, JavaScript, SQL, PHP, Python, Bootstrap, Java and XML.

    [w3schools.com](http://w3schools.com/)

    JavaScript TutorialWell organized and easy to understand Web building tutorials with lots of examples of how to use HTML, CSS, JavaScript, SQL, PHP, Python, Bootstrap, Java and XML.YouTube | Programming with MoshJavaScript Tutorial for Beginners: Learn JavaScript in 1 Hour [2019]

    [chartjs.org](http://chartjs.org/)

    Chart.js | Open source HTML5 Charts for your websiteSimple, clean and engaging HTML5 based JavaScript charts. Chart.js is an easy way to include animated, interactive graphs on your website for free.

- 웹 코딩의 기초
- chartjs

- world wide web : www
- 최초의 www
- 최초의 웹사이트
- 오늘 배울 영역 : 웹 브라우저

## HTML

- HyperText Markup Language
- 웹 페이지 모습을 기술하기 위한 규약
- 시작과 끝은 <> </>

![](Untitled-cb220001-4f61-405a-b8cf-b6822a4830cb.png)

- <TAG> ... </TAG>
- <TAG/>  (한 줄짜리 태그)

### html tags in head

- <title> : 제목
- <meta> : 문서의 특성 (인코딩 방식, 검색용 키워드)
- <link> : 연결된 정보 (css)
- <script> :  제어를 위한 스크립트 코드 또는 연결 정보
- 소문자로 하면 소문자로 쭉 가고, 대문자로 하면 대문자로 쭉 가기! 가급적이면 소문자를..!

![](Untitled-0cee218c-7eeb-4ef1-b721-768475911b20.png)

### html tags in body

![](Untitled-752f245d-80c7-41e4-8070-880bfcc0e795.png)

- <p> : 같은 문단이지만 자동으로 gap이 생김
- <div> : css적 특징 존재, 테이블을 대체하는 용도로도 사용함. 요즘엔 div를 많이 씀.
- <center> : 요즘엔 잘 안 씀. 요즘 html 5(개정판) 컨셉은 모양을 결정하는 특히 폰트 같은건 가급적 하지 말아라. 그런건 css가 따로 하게 하고, 태그들이 직접 난 이모양으로만 가는 태그야! 하는 일이 없게끔. 그냥 순수하게 내용만 남게. (제목/본문/이미지가 들어가는 내용) 모양은 css에서 지정하자 그렇게되면 서로 재활용이 가능하고, ai가 크롤링할 때 좀 더 의미 있는 분석을 빨리 할 수 있게 됨
- <style> : 스타일을 정의함
    - css 문법 사용을 사용하겠다는 뜻
- html이나 css는 코딩 스타일이 여러개라서 같이 작업하면 서로 맞추는 게 좋음
- 파이썬은 문서 형식이 딱 하나라서 오픈소스에서 인기가 많고 인정받음

### Attributes

- tag들의 세부 속성
- 표현 속성은 css로 대체, 조작 가능
- charset = "utf-8" # 특히 한글에서..!
- content = 'telephone=no' # 모바일

![](Untitled-11164523-93ab-457c-a318-33b26e798a13.png)

- 웹 표준은 자주 바뀌기 때문에 외우기보단 이해하자
- 공통된 웹 표준을 보고 싶을 때 : hettps://developer.mozilla.org/ko/docs/Web/HTMl

# Tools : 개발도구

- WEB BROWSER 개발자 도구
    - IE, EDGE
    - CHROME → 맥북에서 도구 더보기 - 개발자 도구 (alt+command+i)
    - FIREFOX DEVELOPER EDITION
    - SAFARI

### 개발도구

- web browser 개발자 도구
    - demo
- Editor (유료)
    - Coda (nova로 대체 예정)
    - sublime text
    - webstorm
- Editor(무료)
    - atom (github에서 만든건데, ms사가 인수해서 미래가 불투명,,ms는 brackets가 있음)
    - vsc (비스코) - 추천! 플러그 인이 많음. 웹 개발 도움되는 익스텐션이 많다. → 산업 표준 정도의 위치라서 익숙해지면 좋음
    - visual studio community edition
    - brackets (디자이너에게 유용)

### 이건 뭐죠?

- xml
    - eXtensible Markup Language
    - 구조화된 문서를 주고 받는 데 사용
    - 주로 상업적 목적으로 주고받는 데이터 활용
    - DTD, Scheme 등의 형식 정의로 특정 목적으로 제약 가능
    - 사전 형식 문제 파악 가능(Validation)
- JSON
    - JavaScript Object Notation
    - js에서 주고받는 축약된 형식
    - 공개 데이터에 많이 활용
    - xml의 복잡한 형식을 탈피하기 위해 만들어 냄
    - tip! JSON beautifier & Validator (아샬님 수업때 해봤던거!)

# CSS

- css 또는 캐스케이딩 스타일 시트는 마크업 언어가 실제 표시되는 방법을 기술하는 언어로 html과 xhtml에 주로 쓰이며 xml에서도 사용할 수 있다. w3c의 표준이며, 레이아웃과 스타일을 정의할 때의 자유도가 높다.
- 반응형 (웹/모바일) : 모양을 결정 짓게 해주는 css
- html에서 style을 지정 → 더 효율적으로 style을 바디로 빼자! → 더더더 효율적으로 아예 style을 빼고 css로 지정하자! (반복되는 재활용 가능)
- 내용 - 스타일

![](Untitled-0c46a8b6-83e7-43da-ac53-c84a4e8932e7.png)

- 뒤에 놓여진 순서대로 우선권 존재
    - font-family: → 산세리프로 먼저 커버하고, 안되는 한글 글꼴 같은 경우는 돋움으로!// noto sans 많이 쓰세용 범용적으로 어디서든 많이 쓸 수 있게 한거니까 때문! (한글 폰트에 대해서는)
    - @import url("http://fonts.googleapis.com.earlyaccess.notosanskr.css"); → kr와 eng 가능
    - 비스코가 좋은 이유! color 값에 마우스 커서 가져가 되면 색상명 알려줌
    - 그리고 일부 색상들은 영문화가 되어있음 (blac, red, blue, white 등등...)

![](Untitled-ff30a657-1a76-4f7c-be84-5d8ac3c3ee12.png)

### important의 선언

- css 자체가 선언
- 가끔 어떤 선언이 너무 중요해서 다른 모든 조건보다 우선시 해야할 때, css 2.1에서는 important 선언 이라고 부름 . 선언 끝을 나타내는 세미콜론 앞에 !important를 추가해서 표현
- p.dark {color: #333 !important; background: white;}
    - 색상값 #333에는 !important를 붙였지만 배경색상 화이트에는 붙이지 않았다. 두 선언 모두 선언하려면 각각 !important를 개별적으로 붙여야 한다.
    - 제 위치에 놓이지 않으면 선언이 무효가 될 수 있음. 그래서 세미콜론 바로 앞에 위치해야함. 특히 Font처럼 다중 키워드 값이 허용되는 속성을 사용할 경우 중요
    - important선언과 일반적인 선언이 충돌할 때에는 언제나 important선언이 우선권을 갖는다.
    - 클래스를 쓸 때는 위에 .title 을 붙여야함
    - gray에 임포턴트 선언이 있기 때문에, 블루여도 그레이로 그려짐
    - important가 여러개가 있을 때 뭐가 우선? → 브라우져마다 다름..!

    ![](Untitled-ea91894b-4feb-4022-8167-273e13d88fdd.png)

    - * : 와일드 카드 (다 적용해버리겠다! )

    ![](Untitled-1539b9b4-61f2-4b66-ba23-a321eafdc955.png)

### CASCADE

- h1 {color:red;}
- h1 {color:blue,}
- 브라우저는 이런 스타일 충동을 어떻게 해결할까?  → 브라우저마다 해결책이 다르니까 왠만하면 충돌이 안되게 만들어라 (가급적 하나씩..!) 임포턴트는 가급적 안 쓰는 게 좋다!!
    - 우선순위
    - 1. 사용자 !important 선언
    - 2. 제작자 !important 선언
    - 3. 제작자 일반 선언
    - 4. 사용자 일반 선언
    - 5. 사용자 에이전트 선언
- 주어진 요소를 선택하는 선택자가 포함된 모든 규칙을 찾는다.
- 요소에 적용되는 모든 선언을 명시적인 중요도에 따라 분류
- !important로 선언된 모든 규칙은 그렇지 않은 규칙보다 더 높은 우선순위.
- 요소에 적용될 모든 선언을 선언의 출처(origin)에 따라 분류한다.
- 선언에는 제작자(author), 사용자 reader, 사용자 에이전트 user agent의 세가지 출처가 존재.
- 일반적 상황에서는 제작자 스타일시트가 사용자 스타일시트 보다 우선하지만 !important는 반대.
- 요소에 적용되는 모든 선언을 구체성에 따라 분류 (구체성이 더 높은 선언 > 안 높은 선언)
- 요소에 적용되는 모든 선언은 순서대로 분류
- 스타일시트나 문서에서 선언이 뒤에 위치할수록 더 높은 우선순위.
- important로 불러온 스타일시트는 해당 스타일시트를 불러오는 스타일시트의 그 어떤 선언보다 앞에 있는 것으로 간주.

### 절대 길이 단위

![](Untitled-8394b19b-c6d1-434a-9521-c0dca9a08312.png)

![](Untitled-7b869384-1bc6-4c96-96f7-5ab097c7da8d.png)

![](Untitled-529c190e-ea06-436e-848c-cf574b5e2fd2.png)

![](Untitled-dbc82557-fd57-4ecf-a938-cd8e04ee722d.png)

### 키워드

- 어떤 값을 특정한 단어로 설명해야할 때 사용
- ex) html 문서 링크에 생기는 밑줄을 없애려면 다음과 같이 지정
    - a:link, a:visited {text-decoration: none;} # 텍스트에 어떠한 장식도 하지 않는다는 뜻
    - 없는 값 → null, zero가 아니라 none 으로 표기
    - a: 링크를 걸 때 사용하는 html 언어
- 링크에 마우스 포인트를 둘 때 색이 바꾸거나 밑줄 치게 하고 싶으면 키워드로 지정해서 만듬

# RESONSIVE WEB

### media query

- px 단위의 화면 폭 지정
- **@media** screen and (min-width: 1024px) and (max-width: 1366px)

![](Untitled-85aacd76-d8fc-4a61-9494-a11441fef909.png)

- 사파리 - 개발자용 도구 탭 - 응답자형 미디어 만들기 하면 이미 지정된 해상도가 나옴!!
- 물론 크롬에도 있음 ㅎㅎ 도구에 폰이랑 네모박스 클릭하면 여기서도 다 볼 수 있음

![](Untitled-9b7d1a96-c665-4f6f-b5cd-4890ae531df1.png)

- 구글웹디자이너 툴도 존재

# 실습

- ex 폴더

![](Untitled-fce51486-8e87-460c-9c72-7e9bd89aba27.png)

- class 와 ID
    - . 말고 id라는 것도 있음
    - id는 문서에서 딱! 하나만 있어야 함. 아이디는 딱 하나만 존재하기 때문에 한정된 곳에 씀
    - 대표적으로 시각화 할때. 그려야할 영역 지정
    - 아이디는 #을  쓴다

        <style type="text/css">
        <!--
        #red {color:red}
        //-->
        </style>
        
        <p id="red">이 문단의 id는 red입니다.</p>
        
        <p>일반적인 문단입니다.</p>

- 한 폴더 안에 html이 여러개 있어도 일단 Index.html 을 가장 먼저 불러오는 게 문법 규칙
- 만약 다른 것도 띄우고 싶다면, 주소를 변경해주면 된다. 일일이 쳐서 들어가야 함

    ![](Untitled-eb3bc48e-e860-4416-a174-11c0f12f7129.png)

# Java script

## chart js

- 캔버스 방식

## D3

- sgv 방식