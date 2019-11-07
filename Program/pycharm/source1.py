import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
start = time.time()

# 1) 파일 명
filename = "joo3"

# 2) 이미지 파일을 src라는 변수명을 가진 numpy로 읽어들임
src = cv2.imread(filename+".jpg")

# 3) 이미지 비율 줄이기. 
# 이미지가 너무 크면 분석에 시간이 오래거림.
# src.shape = (height, width, depth)
# 여기서 depth는 B,G,R 3차원을 의미함

r = 5 # 5분의 1로 줄이기
src = cv2.resize(src, dsize=(int(src.shape[1]/r), int(src.shape[0]/r)), interpolation=cv2.INTER_AREA)

# 4) 색공간 변환
# 처음 이미지를 읽어들이면 BGR로 읽어들임
# 분석을 하기 위해 색상/채도/명도를 나타내는 HSV 색공간으로 변환
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
height, width, channel = src.shape

# 5) 색상 히스토그램 쌓기
# 이미지의 색상 값은 0~180의 범위를 가짐. 히스토그램을 쌓기 위해 zeros로 데이터 생성
h_histogram = np.zeros((181, 1))


# 이미지의 row와 column을 쭉 이동하면서 밝기에 해당하는 히스토그램 +1
for i in range(height):
    for j in range(width):
        val = hsv[i, j, 0]
        h_histogram[val, 0] += 1

h_histogram = pd.DataFrame(h_histogram, columns=["histogram"])

# 여기서부터 새로 해야 함
# h_histogram에 대해 scikit learn의 k-means 클러스터링 적용시켜보기

############################################
'''


h_histogram = h_histogram.sort_values(["histogram"], ascending=[False])
h_histogram = h_histogram.reset_index()

err = 10
ncolor = 10
H = []

for i in range(ncolor):
    step = int((180-err) / ncolor)
    H.append(h_histogram.head(1+i*step)['index'].values[-1])

    if len(H) >= ncolor:
        break

# H.append(h_histogram.head(1).index.values.astype(int)[-1])
# max_idx = 1

# for i in range(1, 181):
#     if abs(
#         h_histogram.head(i).index.values.astype(int)[-1] - h_histogram.head(max_idx).index.values.astype(int)[-1]) > dist:
#         H.append(h_histogram.head(i).index.values.astype(int)[-1])
#         max_idx = i
#
#     if len(H) >= ncolor:
#         break

S, V = [], []
for k in range(ncolor):
    s_histogram = np.zeros((256, 1))
    v_histogram = np.zeros((256, 1))
    for i in range(height):
        for j in range(width):
            if hsv[i,j,0] == H[k]:
                s, v = hsv[i, j, 1], hsv[i, j, 2]
                s_histogram[s, 0] += 1
                v_histogram[v, 0] += 1
    S.append(s_histogram.argmax())
    V.append(v_histogram.argmax())

mat = hsv.copy()
cv2.circle(mat, (20, int(height/2)), 20, (int(H[0]), int(S[0]), int(V[0])), -1)
cv2.circle(mat, (80, int(height/2)), 20, (int(H[1]), int(S[1]), int(V[1])), -1)
cv2.circle(mat, (140, int(height/2)), 20, (int(H[2]), int(S[2]), int(V[2])), -1)
cv2.circle(mat, (200, int(height/2)), 20, (int(H[3]), int(S[3]), int(V[3])), -1)
cv2.circle(mat, (260, int(height/2)), 20, (int(H[4]), int(S[4]), int(V[4])), -1)

cv2.circle(mat, (320, int(height/2)), 20, (int(H[5]), int(S[5]), int(V[5])), -1)
cv2.circle(mat, (380, int(height/2)), 20, (int(H[6]), int(S[6]), int(V[6])), -1)
cv2.circle(mat, (440, int(height/2)), 20, (int(H[7]), int(S[7]), int(V[7])), -1)
cv2.circle(mat, (500, int(height/2)), 20, (int(H[8]), int(S[8]), int(V[8])), -1)
cv2.circle(mat, (560, int(height/2)), 20, (int(H[9]), int(S[9]), int(V[9])), -1)

dst = cv2.cvtColor(mat, cv2.COLOR_HSV2BGR)
print(time.time() - start)
cv2.imshow("src", src)
cv2.imshow("dst", dst)

# cv2.imwrite(filename+"_out.jpg", dst)
cv2.waitKey(0)
'''
