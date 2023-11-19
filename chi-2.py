import scipy.stats as stats

observed_values = [float(input("1つ目の観測値を入力してください: ")), float(input("2つ目の観測値を入力してください: "))]

expected_values = [float(input("1つ目の期待値を入力してください: ")), float(input("2つ目の期待値を入力してください: "))]

alpha = float(input("有意水準を入力してください (通常は0.05を使用します): "))

while sum(observed_values) != sum(expected_values):
    print("観測値と期待値の合計が一致しません。最初からやり直してください。")
    
    observed_values = [float(input("1つ目の観測値を入力してください: ")), float(input("2つ目の観測値を入力してください: "))]

    expected_values = [float(input("1つ目の期待値を入力してください: ")), float(input("2つ目の期待値を入力してください: "))]

chi2_statistic, p_value = stats.chisquare(f_obs=observed_values, f_exp=expected_values)

degrees_of_freedom = len(observed_values) - 1

critical_value = stats.chi2.ppf(1 - alpha, degrees_of_freedom)

print(f"カイ二乗統計量: {chi2_statistic}")
print(f"P値: {p_value}")
print(f"自由度: {degrees_of_freedom}")
print(f"臨界値: {critical_value}")

if chi2_statistic > critical_value:
    print("帰無仮説を棄却：統計的な有意な差があります。")
else:
    print("帰無仮説は棄却されません：統計的な有意な差は見られません。")
