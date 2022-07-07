# CodestatesProject1(team)
ppt presentation: https://www.youtube.com/watch?v=rIngeviTLg8  
data : https://www.dacon.io/competitions/official/235713/overview/description   
  
    
강태경 morethanever31@gmail.com  
▶ 데이터 전처리 및 분석 학습  
▶ 데이터 시각화  
▶ 모델 학습  
  
김상혁 blingstarhamal@gmail.com  
▶ 모델링  
▶ 데이터 수집 및 가공  
▶ EDA  
  
남창석 ncs10042@gmail.com  
▶ 웹 서비스 구현  
▶ 데이터 가공 및 시각화  
▶ Mock-up 제작  
  
박지석 jsp2746@gmail.com  
▶ 대시보드 제작  
▶ 데이터 가공 및 시각화   
▶ 데이터 분석 및 인사이트 도출  
  

기획서 :  https://github.com/BlingstarHamal/codestatesProject1/blob/main/AI_12_3%ED%8C%80_CP1_%EA%B8%B0%ED%9A%8D%EC%84%9C.pdf


# Modeling
** plz run google colab **  
  
EDA_FIANL.ipynb  
Modeling_ALL.ipynb (catboost,xgboost,randomforest) => out put : cat model  

xgboost와 randomforest는 Optuna로 하이퍼파라미터 튜닝 진행  
catboost는 별도의 하이퍼파라미터 적용 안함  
최종적으로 catboost가 가장 높은 점수 LogLoss(0~1 0에가까울수록 좋은점수)  
  
# Web App  
flask_app  
Web App: https://uscredit.herokuapp.com/  
  
  
## 협업 메뉴얼
git clone https://github.com/BlingstarHamal/codestatesProject1.git  
git checkout -b 새로운브런치이름  
git checkout 새로운브런치이름  
--- 데이터수정후 --
git add .  
git commit '커밋내용'  
git push origin 새로운브런치이름  
