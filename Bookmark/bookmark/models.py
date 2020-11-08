# 모델은 데이터베이스를 관리해주는 중간자

from django.db import models

# Create your models here.

# DB에 뭔가를 저장하고 싶다 -> 모델을 만든다.
# 모델을 만들었다 -> DB에 어떤 데이터들을 어떤 형태로 넣을지 결정!
# 마이그레이션(migrate) -> DB에 모델의 내용을 반영(테이블 생성!)
# 모델을 생성하고 마이그레이션을 꼭 해줘야한다!!!
# makemigrations -> 모델의 변경사항을 추적해서 기록! ,마이그레이션 할 정보가 만들어진다.

# 모델 : 데이터베이스를 SQL없이 다루려고 모델을 사용
# 우리가 데이터를 객체화해서 다루겠다.

# 모델 = 테이블(데이터베이스)
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값


class Bookmark(models.Model):
    # 이 안에 들어가는 필드들이 데이터베이스에 저장 될 컬럼 값
    # 타입을 명시해줘야 함
    site_name = models.CharField(max_length=100)  # 100글자까지 저장 가능!
    url = models.URLField('')  # '이 안의 이름'으로 필드명을 보여주겠다.
    # 필드의 종류가 결정하는 것
    # 1. DB의 Column 종류
    # 2. 제약 사항(몇 글자까지?, 한글도 들어가게 할 건지? 등등)
    # 3. Form의 종류
    # 4. Form에서 제약 사항