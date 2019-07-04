# python-miniHeroku

## 功能

````
  用 flask 架一個可以部署 django app project 的 dev server
````

  1. dev server listen to 8080
  2. 部署完的 project listen port 5000
  3. 以單一檔案接收上傳
  4. 單一檔案可以手動打包
  5. 在 dev server 上解包, jango project 必須自動化
  6. 準備測試用的 application project

## 用法

##### 安裝套件

````
pip install flask
pip install django
````

可以自行決定是否使用 conda, virtualenv

##### 啟動 flask

````
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run -p 8080
````

##### 上傳範例 project 並開始使用 django project

1. 進入 URL :

````
http://localhost:8080/uploads/new
````

2. 上傳附加範例 ``pythonSalesplot.tar.gz `` 或是用自己的 django project ( 要確定是 python3 的專案 )
3. 直接開啟新 tab :

````
http://localhost:5000
````

