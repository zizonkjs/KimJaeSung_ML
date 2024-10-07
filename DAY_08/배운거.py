# KNN알고리즘

# Linear-model : LinearRegression -> 다중(직선, feature 많은형태), 다항(곡선) -> 모델 과대적합 방지(매개변수 alpha : 0~강하게) : 릿지(영향력이 낮은 피쳐의 coef_0에 가깝게), 
#                                                                                                                            라쏘(영향력이 낮은걸 0으로 바꿔버림) 
#                                    분류 --> 선형식의 결과 --> 확률값(0.0~1.0) : 로지스틱회귀
#                                       OvR/OvA : 2진분류기를 여러개 -> 5개 분류하면 5개
#                                       OvO : 2진분류기를 여러개 : 클래수*((클래스수-1)/2)

# Tree-model : DecisionTree ( CART ) -> 회귀/분류  : sklearn(encoding필요)
#              - 하이퍼파라미터 많음.
# ENsemble-model : Voting, Bagging -> RandomForestC/R