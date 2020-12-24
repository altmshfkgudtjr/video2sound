# video2sound
Video to sound module.

### video2sound.py

mp4 파일에서 wav 파일을 추출합니다.

### drawWaveform.py

wav 파일에서 waveform PNG 파일을 생성합니다.

### catchVoiceZone.py

wav 파일에서 peaks를 추출합니다. 그리고 해당 peaks의 리스트에서
오차 +1초, -1초를 포함한 SoundZone을 추출합니다.


```python
play_time = 25
time_list = [1, 3, 4, 7, 8, 10, 20, 22, 23]

sound_zone = [[0, 5], [6, 11], [19, 24]]
```


### 주의
각 파일마다 상단에 상수가 적혀있습니다.
해당 모듈을 사용하기 위해서 각 변수들을 변경하거나 혹은 환경변수로 등록하여 사용할 수 있습니다.
