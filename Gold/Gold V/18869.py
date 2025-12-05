m, n = map(int, input().split()) #m, n input
scale_list = [] # 행성의 크기들을 모을 list 선언
for _ in range(m): # 행성 크기 받을 준비
  scale = list(map(int, input().split())) # 행성 크기들을 list로 받기
  cnt = 0 # dict에 쓸 cnt선언 
  scale_dict = {} # 작은 숫자를 0부터 라벨링 해줄거임
  for i in sorted(set(scale)): # scale을 정렬하고 중복을 제거한것중에
    scale_dict[i] = cnt # cnt를 1씩 증가시켜가며 라벨링
    cnt += 1 # cnt++
  
  scale = [scale_dict[i] for i in scale] # list comprehension으로 scale을 라벨링한것으로 변환
  scale_list.append(scale) #데이터를 scale_list에 넣기
  
result = 0 # 결과를 저장할 변수
for i in range(m): # 행성의 갯수 중
  for j in range(i+1, m): # i+1번째 행성부터 마지막까지(중복피하기)
    if scale_list[i] == scale_list[j]: # 행성의 라벨링된 크기 정보가 같다면
      result += 1 # 결과 1 더하고

print(result) #결과 출력
