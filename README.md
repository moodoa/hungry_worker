# hungry_worker
* 部屬訂飲料 app 到 deta 上，並連動 LINE bot。
![alt text](https://cdn-images-1.medium.com/max/1000/1*hwV0jr2O9CVcqSAZJiExZQ.png)

## usage
* 關於 line bot 的設定
* 1.Channel secret 在 Basic Settings 裡面可以找到，Channel access token 則是在 Messaging API 裡面。
![alt text](https://cdn-images-1.medium.com/max/1000/1*ZWscTYpEzFrDh25-C4DPUw.png)
* 2.Messaging API 裡面的 Use webhook 要打開。
* 3.Webhook URL 輸入由 deta 產生的url，後面要加/callback。
![alt text](https://cdn-images-1.medium.com/max/1000/1*-LbkJAAAtf-7EgIUJrWewQ.png)

* 關於 deta 的設定
* 1.申請帳號以及安裝 CLI 登入可參考：https://docs.deta.sh/docs/micros/getting_started
* 2.開啟 PowerShell ，創立一個新的作業資料夾。如創立 hungry_worker 資料夾為 `deta new --python hungry_worker` 。
* 3.此時會出現類似 ![alt text](https://cdn-images-1.medium.com/max/1000/1*D1dyv86VpQFsHTz_dr0nUA.png)，endpoint 上的 url 要輸入進 Webhook URL。
* 4.進入 hungry_worker 資料夾，將此 repo 中的 main.py (取代內建的) 和 requirements.txt 放進去。
* 5.PowerShell 輸入 deta deploy，如此便能完成布署。
