# ChuSomeChuSome
주섬주섬 : 오작교를 위한 주선 관리 서비스 입니다 

# 아키텍쳐

![chusome drawio](https://github.com/user-attachments/assets/f2b2b6b8-1d17-4152-af09-6e8d7a2e2dcf)

간단하게 서버리스 환경으로 구성했으며 코드 base가 되는 S3와 AI를 증강시켜줄 DataSource S3 두개의 저장소를 활용합니다.

생성형 AI와 증강시켜줄 지식기반 벡터DB는 bedrock에서 제공하는 기능을 사용합니다 (Claude 3.5 sonet, OpenSearch, S3)

### 여정

https://pages.awscloud.com/aws-ai-day-innovation-hackathon-anthropic.html
AWS AI Day: Innovation 해커톤 출품을 목표로 진행합니다.

~ 11. 15
