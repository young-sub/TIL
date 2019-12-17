#  로지스틱 회귀분석 with R

## 1. 로지스틱 회귀분석 

###  (0) 정의

- 로지스틱 회귀분석은 종속변수가 명목형이자 이진형 변수일 때, 쓰이는 회귀분석 방법이다. 종속변수에 로짓변환을 실시하기 때문에 로지스틱 회귀분석이라고 불립니다.

- 종속변수가 특정 범주 i가 될 확률을 구하는 과정이다.

- 로짓(logit) 함수: **G(p)=log(p/(1-p))**

- **오즈(odds)** : p/(1-p)

- 오즈값을 비교한 것을 **오즈비**(odds ratio) 

  (ex) 오즈비=남자의 오즈/여자의 오즈)



### (1) 실습 코드 

- 종속변수가 Factor형 자료가 아니라면 Factor형으로 변환하고 진행해야 한다.
- 독립변수는 수치형, 명목형 자료 모두 가능하나 명목형인 경우에는 벡터화해서 자료를 입력해야 한다. (ex) [1,0,0], [0,1,0], [0,0,1])

``````R
# 로지스틱 회귀분석
# 예제 1
data(iris)

# 먼저 들어오는 데이터를 0으로 본다.(versicolor가 더 앞선 데이터이므로 0)
d <- subset(iris, Species == "versicolor"  |Species == "virginica")
str(d)
m <- glm(Species ~ ., data=d, family = "binomial" )
summary(m)
fitted(m)[c(1:5,51:55)]

# P(Y=1) : virginica가 될 확률
# 예측치를 virginica가 될 확률로 근사해서 간주할 수 있다. (완전히 같지는 않지만 해당 오차는 무시할만하다.)
f <- fitted(m)

# 예측치와 실제값을 비교
# 0이면 versicolor이고 1이면 virginica 만일 예측치와 실제값이 다르다면 False를 반환
is_correct <- ifelse(f>0.5,1,0) == as.numeric(d$Species) - 2
sum(is_correct)


# 예제 2 
# 여러 변수들을 통해 입학 여부를 예측하기 위한 모델
# 종속변수 입학 여부
# 독립변수 GRE, GPA, RANK
library(aod)
library(ggplot2)
# view the first few rows of the data
mydata <- read.csv("https://stats.idre.ucla.edu/stat/data/binary.csv")
head(mydata) 
summary(mydata) # 데이터의 대략적인 분포 확인
str(mydata) # 데이터 구조 확인
sapply(mydata, sd) # 변수별 표준편차 확인
xtabs(~admit+rank, data=mydata) # contingency table : xtabs(~ x + y, data)

mydata$rank <- factor(mydata$rank)
mylogit <- glm(admit ~ gre + gpa + rank, data = mydata, family =
                   "binomial")

summary(mylogit)
``````



### (2) 해석 

![image](https://user-images.githubusercontent.com/57510026/70965357-be879900-20d2-11ea-88b6-eb69aac243f9.png)

- 회귀계수가 변수가 한 단위 증가했을 때 log(odds)의 증가량으로 해석할 수 있다.

  - β<sub>1</sub> = Δlog(odds) / Δx

  

- **독립변수가 수치형**일 때 log(odds)이 양수이면 입학할 확률(성공)이 입학 못할 확률보다 크다고 해석된다.(log(odds)>0일때 odds>1)

  - 계수값이 양수일 시 Δlog(odds)>0이고 Δodds>1이다. 이때 odds는 실패할 확률 대비 성공할 확률이므로 성공할 확률에 좋은 영향을 준다.
  - **이때 계수값에 exp를 취해주면 Δ오즈비(OR)이 된다.**

  - 즉, gpa가 1증가하면 2.23배만큼 입학 확률이 상승한다고 할 수 있다. (exp(0.804038) = 약 2.23)

  - 또 이때 admission의 non-admission에 대한 오즈비가 2.23배 증가한다라고 해석할 수 있다. 

    (이는 수치형 변수의 경우 기준이 되는 오즈비가 1이기 때문이다.)

    

- **독립변수가 명목형**일 때 rank2의 회귀계수 -0.67은 rank1에서 rank2로 바뀌었을 때, log(odds)의 변화량이다. 즉, rank1에 비해 rank2가 admission에 안좋은 영향을 준다는 것을 알 수 있다

  - 즉, rank1의 입학할 확률에 비해 rank2의 입학할 확률이 0.51배라고 해석할 수 있다. 

    (exp(-0.675443) = 약 0.51)



## 2. Multinomial Logistic Regression

### (0) 정의 및 코드

- Multinomial Logistic Regression이란 y의 범주가 3개 이상(multi)이며 명목형(nomial)일 때 사용하는 로지스틱 회귀분석이다.

``````R
# Multinomial Logistic Regression
require(foreign)
require(nnet)
require(ggplot2)
require(reshape2)
ml <- read.dta("https://stats.idre.ucla.edu/stat/data/hsbdemo.dta")

ml$prog2 <- relevel(ml$prog, ref = "academic")
test <- multinom(prog2 ~ ses + write, data = ml)
summary(test)
``````



### (1) 해석 

![image](https://user-images.githubusercontent.com/57510026/70970220-22b15980-20e1-11ea-8145-c8667617f8ed.png)

![image](https://user-images.githubusercontent.com/57510026/70970408-a703dc80-20e1-11ea-9b7b-3239ded8cd6c.png)



- write가 1단위 증가할 때, academic이 general이 될 확률이 0.94배가 된다.  (exp(-0.058)=0.94)
  - 즉, general의 academic에 대한 오즈비가 0.94배 감소한다.
- ses:row에서 ses:middle로 변할 때, academic이 general가 될 확률이 0.59배가 된다. (exp(-0.5332)=0.59)

