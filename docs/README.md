# DjangoとNext.jsの繋ぎ込みテスト用プロジェクト
## 使い方
- pip install pipenv
- cd front/next-django-demo
- npm run dev
- 別ターミナルを開く
- cd back
- ./manage.py runserver
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)へアクセス
  - 8000番ポート(Django側)にアクセスしてもNext.jsのウェルカム画面が表示されている -> 繋ぎ込み成功