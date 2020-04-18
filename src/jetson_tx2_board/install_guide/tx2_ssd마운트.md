# Jetson_tx2_ssd_mount

### 1. `Disks`를 검색하여 클릭

![s1](https://user-images.githubusercontent.com/61573968/79543677-d430bd80-80c8-11ea-991c-d6bcd8fadf02.png)



### 2. 오른쪽 상단의 ![s5](https://user-images.githubusercontent.com/61573968/79543687-d72bae00-80c8-11ea-9378-f3dd551dbf18.png)를 누르고 `Format Disk`를 클릭 후 `Format`

![s2](https://user-images.githubusercontent.com/61573968/79543680-d5fa8100-80c8-11ea-81d1-70786081336e.png)

- 계속 `Format`버튼을 누르면 됨

![s3](https://user-images.githubusercontent.com/61573968/79543682-d5fa8100-80c8-11ea-81bf-11e11c8f058c.png)



- Format이 완료된 후

![s4](https://user-images.githubusercontent.com/61573968/79543683-d6931780-80c8-11ea-9584-70e6b573750d.png)





### 3. Volumes 에 있는 `+` 버튼을 클릭

- `Next`를 클릭

![s7](https://user-images.githubusercontent.com/61573968/79543691-d7c44480-80c8-11ea-9c20-699511f42b7d.png)



- `volume name`을 지정하고 `creat`

![s8](/home/roje/79543692-d85cdb00-80c8-11ea-87b4-fdb0e2f5f30e.png)





### 4. ![s10](https://user-images.githubusercontent.com/61573968/79543695-d8f57180-80c8-11ea-9174-e54bfff1425b.png) 버튼을 누르고 `Format Partition` 클릭

- `volume name`을 지정하고 `next`

![s11](https://user-images.githubusercontent.com/61573968/79543697-d98e0800-80c8-11ea-9287-04459d2bd014.png)



- Format 된 ssd

![s12](https://user-images.githubusercontent.com/61573968/79543698-d98e0800-80c8-11ea-911d-0d7553211ea8.png)





### 5. 바탕화면의 왼쪽 메뉴바에서 ![s13](https://user-images.githubusercontent.com/61573968/79543700-da269e80-80c8-11ea-8c4e-b9b4b34bf958.png)를 클릭

### 6. Terminal 실행

`sudo cp -ax / '{ssd의 위치와 ssd폴더}' && sync` 입력

{} 안의 ssd의 위치는 mount한 ssd의 위치 (속성을 통해서도 확인이 가능함)

![s14](https://user-images.githubusercontent.com/61573968/79543701-dabf3500-80c8-11ea-851e-648b7afda94d.png)







