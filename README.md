# Democracy-Bot
디스코드 사다리타기, 투표기능 봇

### 투표 봇
* 간단한 투표 기능을 가진 봇
* 모든 작업을 텍스트로 처리
* 명령어
  * !투표설정 (0 or 1) (후보1)/(후보2)/.../(후보n)
    * 투표를 설정함
    * 공개 투표시 !투표설정 0
    * 비공개 투표시 !투표설정 1
    * 이전의 투표가 끝나지 않았다면 강제로 종료함
  * !투표참여
    * 투표에 참여함
    * ID값을 넘겨받음
  * !투표 (INDEX)
    * 투표함
  * !투표종료
    * 투표를 종료한 후 
    
### 사다리타기 봇
* 간단한 사다리타기 기능을 가진 봇
* 사다리를 텍스트 형식으로 출력(여유가 있을 시 이미지로 출력 또한 고려 가능)
* 명령어
  * !사다리설정 (0 or 1) (ID1)/(ID2)/.../(IDn)
    * 0일 시 사다리타기 윗 줄 설정
    * 1일 시 사다리타기 아랫 줄 설정
  * !사다리진행 (1~n)
    * 인덱스 값에 해당하는 ID의 사다리타기 결과 출력
  * !사다리결과
    * 사다리타기의 결과만을 간단하게  
