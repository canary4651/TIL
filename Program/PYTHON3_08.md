# PYTHON3_08

- GOAL
    - 1. 문제 이해
    - 2. 계획 수립
    - 3. 계획 실행
    - 4. 반성

## git branch 생성하고 pull request 하는 법 다시 리뷰

- git checkout -b 브랜치이름 upstream/master → 업스트림의 마스터 라는 의미
- git reset HEAD^^ —HARD : git reset HEAD : 한단계 전으로 ^^ 한단계 전으로 → 2단계 전 —hard: 강제로
- git pull —rebase upstream master → 업스트림 마스터의 내용을 불러옴
- git.config → 에서 github 연결들을 고칠 수 있음
- origin master 코드 동일하게 하는 법
    - git checkout master
    - git pull --rebase upstream master
    - git push origin master
    - origin 브랜치 삭제하는 방법 :
        - git push origin :yeeunhan
    - 아니면 소스트리에서 origin에 있는 거 삭제하면 됌

### Merge 다 이루어진 상태에서 새로운 브랜치 만들고 최신 꺼 땡겨오기

- git branch -D 브랜치이름
- git remote add upstream 주소
- git pull upstream master
    - 이미 내 것이 다 pull request 가 된 상태, 다른 사람 것을 base로 할 필요 없으면 base옵션 필요 x
- git branch 새로운 브랜치이름 (ex)python0813)
- git checkout python0813
- 원래 하던 거~~ (add~~commit~~)
- git push origin python0813
    - (자기 브랜치로 안하고 master로 해도 아무 일도 일어나지않는다. 어차피 자기 브랜치에서만 작업했으니까.  master는 아무 변경사항이 없어서 아무것도 반영되지 않는다. 따라서 git push origin master를 했어도 악 소리 한번 지르고 다시 제대로 입력하면 된당)

### 내꺼 수정 중에 (이미 내 브랜치가 있고 master에서 pull request가 되지 않은 상태,

### 혹은 내가 작업 중에 다른 사람이 push 하고 merge 된 내용을 내가 필요로 할 때) base 옮겨야 할 때

- git checkout master
- git pull --rebase upstream master
    - 최신버전으로 base 변경
- git push -f origin master ( -f 옵션은 강제 push. 없어도 push 가능할 수 있다)

---

git checkout -b <새 브랜치 이름>

이건 현재 브랜치를 기준(base)으로 새 브랜치를 만드는 겁니다. 이렇게 하면 새 브랜치를 독립적으로 만들 수 없죠.

그래서 다음과 같이 어떤 브랜치를 기준(base)으로 새 브랜치를 만드는지 지정합니다.

git checkout -b <새 브랜치 이름> <기준 브랜치 이름>

기준 브랜치로 모두가 공유하는 가장 최신 브랜치를 사용하면 좋겠죠? 그게 바로 `upstream/master` 입니다.

git checkout -b <새 브랜치 이름> upstream/master

git rebase -i HEAD~2

- [https://github.com/dataitgirls3/TIL/pull/136](https://github.com/dataitgirls3/TIL/pull/136)
- 아샬님 설명 참조