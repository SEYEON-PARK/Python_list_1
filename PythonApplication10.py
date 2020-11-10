scores=[]
sum=0 ; goodScore=0

for i in range(5):
    score=int(input("성적을 입력하시오. : "))
    scores.append(score)
    sum+=score

print("성적 평균은 %d입니다." %(sum/5))

for x in range(5):
    if scores[x]>=80:
        goodScore+=1

print("80점 이상 성적을 받은 학생은 {}명 입니다.".format(goodScore))
