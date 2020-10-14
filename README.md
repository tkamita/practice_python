# practice_python

anacondaのinstall
  anaconda.com
    mac gui 3.8

conda create -n pythonenv(環境名) python=3.8(バージョン指定)
conda env list    #作成された環境のリスト
source activate pythonenv(環境名)   #指定した環境を有効化する

#作成したpythonenvにパッケージを入れる
conda install flask(パッケージ名)
conda list    #パッケージ一覧

#環境の無効化
conda deactivate

#作成した環境の削除
conda remove -n pythonenv(環境名) --all


＃VSコードにpyhonのパスを通す
設定を開く(コマンド ＋ ,)
  アプリケーション
    settings.json(VSコードの設定)
      "python.pythonPath": "パス",
＃パスはconda env listで確認する
pythonenv(環境名)  /opt/---/---/---(パス)

#pythonの拡張機能を入れる