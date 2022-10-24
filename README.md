# Example
* Must be the same.
<img src="./image/HW01.png" style="zoom:70%" />

1. 男女性別人數
2. 年齡區間(0-80歲區分20塊)
3. 艙等有三個，長條圖個別的罹難人數和活著人數
4. 散佈圖，藍色方形是存活，紅色叉罹難，橫軸是年齡，縱軸是花多少錢買這船票花多少錢。
5. 預設的藍紅色就可以了。

## Use the data

1. Survived
2. Pclass 船艙等級
3. Sex
4. Age
5. Fare 船票價格

#Important program logic

##計算各個年齡區間有多少人
* 原先打算要一一比對，也就是該人符合哪個區間，且該區間人數加一。可是這樣判斷要寫非常多，用迴圈更會增加運算時間。
* 修正：用除法。先找出每個間隔多少，在用除法找出商數。接著在商數位置的區間加一，避免程式執行過長。