# DjangoとNext.jsの繋ぎ込みテスト用プロジェクト
## 使い方
- pip install pipenv
- pipenv --three

- cd front/next-django-demo
- npm run dev
- 別ターミナルを開く
- cd back
- pipenv shell
- (初回のみ)pipenv install
  - 一応requirements.txt作ったがPipfileにも同様の内容が保存されているはずのため上記で十分である
- python3 manage.py runserver
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)へアクセス
  - [こんな画面](https://imgur.com/Rub8uoR)になれば環境構築完了
- (仮想環境を終了したい場合)exit


- 画面の指示に従って1.csvファイルを選択 2.オプション（デモなので意味のない適当な内容です）を選択 3.編集開始をおす 4.オプションで選んだ内容が追加されたcsvファイルがダウンロードされる