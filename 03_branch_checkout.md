#  Branch &Checkout 정리

## 1. Add / Commit 취소, 수정

### (1) Add 취소 

- Add된 파일을 취소한다.

```shell
$ git rm --cached [파일명]
```



### (2) Commit 수정하기

- Commit된 log 기록을 변경한다.

1. `git commit --amend` 입력
2. 새롭게 뜨는 창에서 i를 눌러 누르면 commit message를 수정 가능하다.
3. 수정 후 Esc키를 누르고 :wq로 저장후 나가기

## 2. Branch

### (1) 브랜치 목록 확인하기

- 일반적으로 master가 main 브랜치이다.
- 현재 브랜치는 명령창 옆에서 바로 확인 가능하다. (ex: ~/TIL (master))
- HEAD는 현재 가르키고 있는 commit이다. 

```shell
$ git branch
```



### (2) 새로운 브랜치 만들기

```shell
$ git branch [새 브랜치 이름]
```



### (3) 브랜치 변경

- checkout 과 swithch 모두 가능하다. (동일한 기능)
- checkout은 log로도 이동 가능하다.  로그 코드는`git log --oneline`에서 확인 가능하다.
- checkout master로 현재 log 혹은 master 브랜치로 돌아올 수 있다.

```shell
$ git switch [브랜치 이름]
$ git checkout [브랜치 이름 or 로그 코드 7자리]
# 새로운 브랜치를 만들고 바로 이동
$ git checkout -b [새 브랜치 이름]
$ git checkout master
```



### (4) 브랜치 삭제하기

```shell
# 내용이 없을 시 
$ git branch -d [브랜치 이름]
# 내용이 있을 시 
$ git branch -D [브랜치 이름]
```



## 3. Merge

### (1) 브랜치 병합 과정 

1. 먼저 병합의 기준이 되는 브랜치로 이동한다.
2. `git merge [브랜치 이름]`으로 브랜치를 병합한다.

- `git log --oneline --graph`로 병합 과정을 그림으로 볼 수 있다.

```shell
git merge [브랜치 이름]
```



### (2) 브랜치 병합 종류

- Fast-forward : 병합 기준의 브랜치는 브랜치 분기 이후 어떠한 log도 쌓지 않았을 경우 자동으로 병합된다. (즉 새롭게 만든 브랜치에 대해서만 작업을 진행 했을경우)

- Auto-merge : 두 브랜치 사이에 충돌이 되는 요소가 없는 경우 자동으로 병합된다. (두 브랜치에 대해 각각 작업을 진행했으나 이름이 겹치나 내용이 같아서 충돌되는 경우가 없는 경우 등)
- Merge-conflict : 두 브랜치 사이에 충돌이 있는 경우 사용자가 직접 merge를 진행한 후 commit 하여야 병합된다. (두 브랜치에 대해 각각 작업을 진행했고 두 파일의 이름이 같고 내용이 달라 충돌이 되는 경우 등)



## 4. Stash

### (1) 임시로 변경분 저장

```shell
$ git stash list
```



### (2) Stash 목록 확인하기

```shell
$ git stash
```



### (3) Stash 다시 가져오기

- 했던 작업을 다시 가져온다.
- --index 옵션을 사용하면 Staged 상태까지 복원한다.
- Apply는  stash 목록에서 불러온 stash를 삭제하진 않는다.
- Pop을 사용하면 불러오는 동시에 삭제한다.

```shell
$ git stash apply [stash 이름]
```



### (4) Stash 제거하기

```shell
$ git stash drop [stash 이름]
```





## 5. 그 외 명령어 및 팁

### (1) 특정 로그로 리셋하기

- 특정 로그로 리셋한다.

```shell
$ git reset --hard [로그 코드 7자리]
```



###  (2) Add / Commit / Log에 대한 이해한 개념

- Add는 작업 중인 파일과 작업이 완료된 파일을 구별하여 commit하기 위해서 사용한다.(사진대에 올리는 개념)
- git status에서는 'add 전', 'add 후 commit' 전까지  보여준다.
- Commit은 로그를 남긴다. 로그가 남으면 파일도 함께 해당 로그를 따라간다. 즉 checkout으로 이전 로그로 간다면 해당 로그에 존재했던 파일만 남는다. (사진대에서 사진을 찍는 개념)



