# windows環境なら動作確認済み
# pip install scikit-learn matplotlib

# 教師あり学習のプログラムの例

import numpy as np  # NumPyライブラリをインポート
import matplotlib.pyplot as plt  # Matplotlibライブラリをインポート
from sklearn.model_selection import train_test_split  # データ分割のための関数をインポート
from sklearn.linear_model import LinearRegression  # 線形回帰モデルのためのクラスをインポート
from sklearn.metrics import mean_squared_error  # 平均二乗誤差計算のための関数をインポート

# 日本語フォントの設定（Windows）
import matplotlib.font_manager as fm

# MS Gothic フォントを使用するように設定
font_path = 'C:\\Windows\\Fonts\\msgothic.ttc'
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# データセットの生成
# np.random.seed(0)  # 乱数生成のシードを設定して再現性を確保
X = 2 * np.random.rand(100, 1)  # 100個のランダムな値を持つ特徴量を生成
y = 4 + 3 * X + np.random.randn(100, 1)  # 特徴量に基づく目標値を生成（ノイズ付き）

# データセットをトレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  # データを80%トレーニング、20%テストに分割

# 線形回帰モデルの作成
model = LinearRegression()  # 線形回帰モデルのインスタンスを作成
model.fit(X_train, y_train)  # トレーニングデータを使ってモデルを訓練

# モデルの予測
y_pred = model.predict(X_test)  # テストデータに対する予測を実行

# モデルの評価
mse = mean_squared_error(y_test, y_pred)  # 平均二乗誤差を計算してモデルの性能を評価
print(f"平均二乗誤差: {mse}")  # 平均二乗誤差を出力

# プロット
plt.scatter(X, y, color='blue', label='データ')  # 元データを散布図としてプロット
plt.plot(X_test, y_pred, color='red', linewidth=2, label='予測')  # 予測結果を直線としてプロット
plt.title('線形回帰')  # プロットのタイトルを設定
plt.xlabel('特徴量')  # X軸のラベルを設定
plt.ylabel('目標値')  # Y軸のラベルを設定
plt.legend()  # 凡例を表示
plt.show()  # プロットを表示
