# PYTHON3_06

# Collection Element

- list : 순서가 존재 (키가 번호. 0 - 키)
- dictionary : 키-value가 같이 존재 (이름-뜻 같은 set)
- set: 집합 : 중복을 허락하지 않는 list 같은 역할

- [python_data_structure](https://docs.python.org/3/tutorial/datastructures.html)
- append (추가함수) : 값을 추가한다
- remove (제거함수) : 뭐를 지운다
- concatenate : 연결, 합쳐줌 (list를 합쳐줌) 그냥 + 로 쓰면 됨 → list + list /  약간의 주의점 : 판다스에서는 list라는 개념이 아니라 array 를 쓰는 데 벡터 기반이라 +를 하면 정말 '합'을 구해준다.
- union : set에서 많이 씀
- difference : 차집합 (요소를 빼줌)
- intersection : 교집합

[https://m.blog.naver.com/PostView.nhn?blogId=pgh7092&logNo=221103514790&proxyReferer=https%3A%2F%2Fwww.google.com%2F](https://m.blog.naver.com/PostView.nhn?blogId=pgh7092&logNo=221103514790&proxyReferer=https%3A%2F%2Fwww.google.com%2F) 

참고 

# 과제

- 국어 점수의 총합 (total 하고 class_scores를 넣고 국어를 같이 쓰기  total(class_scores, 국어)
1. class_total(class_socres, '국어') == 170
2. class_total_all(class_scores) == 430

1) 두 개의 set에서 국어 점수의 총 합은?=> assert class_total(class_scores, '국어') == 170 이렇게 확인할 수 있는 함수를 만들어보세요2) class_scores set에 있는 모든 점수의 합은 얼마인가요?=> class_total_all(class_scores) == 430

class_scores = [

{

'국어': 80,

'영어': 100,

'수학': 50

},

{

'국어': 90,

'영어': 70,

'수학': 40

}

]