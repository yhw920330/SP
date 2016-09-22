Sp Proj 6 NoSQL을 이용한 대용량 N-Gram 언어모델 검색 시스템 
------------------------------------------------------------

실행방법: 
	DynamoDB생성 방법 : python DynamoDB_Import.py
	DynamoDB검색 방법 : python DynamoDB_Query_CLI.py


환경   :
	1)AWS EC2 instance
	2)AWS S3
	3)AWS DynamoDB
	Boto로 python interface를 이용하였다. 
	AWS에서 제공하는 No SQL DB 인 dynamoDB서비스를 이용하였다

프로젝트 설명: 두단어의 빈도수를 저장하고 있는file을 input으로 받아, 이를 단어 + 빈도로 나누고, 단어를 hash key로 하는 DynamoDB에 word와count를 저장하였다.
저장한 TAble을 검색하는 검색시스템도 CLI에서 만들었다.

Read Capacity Unit 120이고 Write Capacity Units은 100이다.




