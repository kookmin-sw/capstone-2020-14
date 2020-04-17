# Jetson TX2에 JetPack4.2.2 설치하기

[참고한 Youtube 영상](https://www.youtube.com/watch?v=s1QDsa6SzuQ&t=160s)

기준일자 2019년 11월 2일

본 글에서는 **SDK Manager** : sdkmanager_0.9.14-4964_amd64.deb 

​					**JetPack** : JetPack4.2.2

​					**Ubuntu18.04**인 환경을 기준으로 작성 

설치 전에 host 컴퓨터에 파이썬2를 설치해야함 : [참조](https://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/)

### **<<< 사전 준비 사항 >>>**

**host 컴퓨터(x86-64 프로세서, Ubuntu 18.04), TX2 보드, TX2보드와 연결할 모니터와 키보드 그리고 마우스가 필요**

host컴퓨터에 20GB이상의 여유 용량이 있는 지 확인,

**편의상 앞으로 다운 받을 파일들을 담을 JetPack폴더를 *host 컴퓨터에* 아래와 같이 만들어 놓고 시작** (JetPack이름뒤에 붙는 숫자는 다운받고자 하는 버전을 의미) 

![image](https://user-images.githubusercontent.com/33410490/67855651-29e2cf00-fb56-11e9-9dfa-5e4d17685f3d.png)



#### ** TX2에 기본적으로 flash 되어있는 Ubuntu 16.04 설치 **

- TX2에 전원을 연결하기 전에 마우스와 키보드, 모니터의 Hdmi 를 연결
- TX2에 전원을 연결
- 화면에 출력된 안내문에 따라 순서대로 커맨드를 입력

```
cd ~/NVIDIA-INSTALLER/
sudo ./installer.sh
password:nvidia
```



**초기로 설정된 id: nvidia, password : nvidia**

설치가 완료된 후 재부팅을 실행

```
reboot
```



### 1. [JetPack 사이트](https://developer.nvidia.com/embedded/jetpack)로 들어가서 아래의 "Download SDK Manager"버튼을 통해 사전에 만들어 놓은 JetPack4.2.2폴더에 sdkmanager_0.9.14-4964_amd64.deb을 다운받기

<주의> 로그인이 필요함!!!!!!

![image](https://user-images.githubusercontent.com/33410490/67855034-00757380-fb55-11e9-85a0-c6260c7c63df.png)

![image](https://user-images.githubusercontent.com/33410490/67856423-d96c7100-fb57-11e9-9576-f4fd3525e453.png)



### 2. sdkmanager_0.9.14-4964_amd64.deb를 다운받은 위치에서 terminal을 열고 아래 코드 실행

```
sudo apt install ./sdkmanager_0.9.14-4964_amd64.deb
```

**버전이 다를 경우** :  [참고](https://docs.nvidia.com/sdk-manager/download-run-sdkm/index.html#download-run)

```
sudo apt install ./[다운받은 sdkmanager deb파일]
```



### 3. 설치한 SDK Manager를 실행

```
sdkmanger
```

*terminal에서 위의 코드를 작성하여 실행하거나, 윈도우키를 눌러 검색 후 sdkmanager를 직접 실행*



### 4. SDK Manager에 로그인을 하고 아래의 화면에서 Target Hardware와 JetPack의 버전을 알맞게 설정한 후 STEP2로 CONTINUE

<설정 전>

![image](https://user-images.githubusercontent.com/33410490/67857793-040bf900-fb5b-11e9-8212-a94376970054.png)



<설정 후>

![image](https://user-images.githubusercontent.com/33410490/67857835-1dad4080-fb5b-11e9-89ef-cc9665684948.png)





### 5. (Optional) STEP 02에서 스크롤을 내려 Additional SDKs도 체크

![image](https://user-images.githubusercontent.com/33410490/67857931-58af7400-fb5b-11e9-9cd5-6ea81820dae3.png)

![image](https://user-images.githubusercontent.com/33410490/67858049-9a401f00-fb5b-11e9-905d-61bb44ebd826.png)





### 6. DONLOAD & INSTALL OPTIONS를 눌러 다운 경로를 지정

***다운 경로를 지정해주기 앞서 사전에 만들어 놓은 JetPack4.2.2폴더 안에 sdkm_downloads와 nvidia_sdk 폴더를 아래와 같이 생성***

![image](https://user-images.githubusercontent.com/33410490/67858244-22bebf80-fb5c-11e9-89cb-861d0836b1b4.png)



**하단과 같이 경로를 지정**

![image](https://user-images.githubusercontent.com/33410490/67858724-361e5a80-fb5d-11e9-9907-b7c56587cd40.png)





### 7. 하단과 같이 동의 버튼을 누른 후 STEP3로 CONTINUE

![image](https://user-images.githubusercontent.com/33410490/67999237-c7491a80-fc9e-11e9-8a35-d2ba063ce77b.png)





### 8. STEP 03의 과정 중 아래와 같은 화면이 나오면 Automatic Setup을 Manual로 바꿔주고 TX2 보드 준비하기(*Flash 버튼은 TX2 보드 준비가 다 된 후에 누를 것이므로 주의하기!!*)

![image](https://user-images.githubusercontent.com/33410490/68450686-3d192d00-022f-11ea-8765-e540e57f9e1f.png)





### 9. TX2 보드 준비과정 (TX2 보드 Force Recovery 모드)

 출처 : https://www.youtube.com/watch?v=s1QDsa6SzuQ&t=511s

![image](https://user-images.githubusercontent.com/33410490/68451477-448e0580-0232-11ea-8962-a41be03862a6.png)

- 위의 사진과 같이 TX2 보드를 준비 (전원선은 아직 연결하지 않음)
- 와이파이, 키보드 및 마우스, 모니터와 연결



![image](https://user-images.githubusercontent.com/33410490/68451309-9bdfa600-0231-11ea-8a51-02c0146ba0fe.png)

- Host컴퓨터와 TX2 보드 간에 위와 같이 연결을 해주고 전원선을 연결해줌



< 본 과정은 중요하므로 [영상](https://www.youtube.com/watch?v=s1QDsa6SzuQ&t=511s)을 참고하여 시행하는 것을 추천 >

![image](https://user-images.githubusercontent.com/33410490/68451905-042f8700-0234-11ea-906e-324ecae7d70c.png)

- 우선 전원 버튼을 눌러 전원을 켬
- 그리고 바로 Force Recovery 버튼을 누름(계속누르고 있어야 함)
- Force Recovery 버튼을 누르고 있는 상태에서 Reset버튼을 누름(Reset버튼은 눌렀다가 뗌, Force Recovery 버튼은 계속 누르고 있음)
- 약 2초가 지난 뒤에 Force Recovery 버튼에서 손을 뗌





### 10. TX2보드를 과정9에서와 같이 준비 후 다시 Host 컴퓨터로 돌아와서 Flash버튼을 누르기

![image](https://user-images.githubusercontent.com/33410490/68452761-d992fd80-0236-11ea-8de0-cc2fea5bdc48.png)

- TX2 보드가 Flash가 되며 host 컴퓨터에 아래와 같은 화면이 뜸

  ![image](https://user-images.githubusercontent.com/33410490/68452929-52925500-0237-11ea-8428-160069ec0d73.png)





### 11. Host 컴퓨터를 그대로 놔두고 다시 TX2 보드의 화면으로 가기

![image](https://user-images.githubusercontent.com/33410490/68453071-d9dfc880-0237-11ea-84df-f042d69fb160.png)

![image](https://user-images.githubusercontent.com/33410490/68453144-1e6b6400-0238-11ea-8c3c-71ac256ca57b.png)

![image](https://user-images.githubusercontent.com/33410490/68453154-2925f900-0238-11ea-91f7-9b5a734096ea.png)

- 위와 같이 언어와 키보드 언어에 대해 자신에게 맞게 설정 후 **하단의 이미지와 같이 computer의 이름과 비번을 설정해줌**

![image](https://user-images.githubusercontent.com/33410490/68453188-37741500-0238-11ea-88d3-bbca1309e5fd.png)

- 설정을 다 완료한 후에 continue버튼을 누르면 재부팅이 자동으로 됨



### 12.  다시 Host 컴퓨터로 돌아와서 방금 TX2보드에 설정한 computer 이름과 비번을 작성 후 install 버튼 누르면 *설치 완료!!*

![image](https://user-images.githubusercontent.com/33410490/68452929-52925500-0237-11ea-8428-160069ec0d73.png)


