#  Push & Pull 정리

### (1) 원격 저장소로 코드 `git push`

- Github 원격 저장소에 push한다.

```shell
$ git push origin master
```



### (2) 원격 저장소에서 정보 받기 전 상태 확인 `git status`

- 현재 `git`의 상태를 조회한다. Pull하기 전 이상이 없는지 확인할 것.

```shell
$ git status
```



### (3) 최초로 원격 저장소에서 정보 받을 시 `git clone`

- 원격 저장소의 폴더를 그대로 복사하여 가져온다.

```shell
$ git clone (github 원격 저장소 주소)
```



### (4) 최초 이후 원격 저장소에서 정보 받을 시 `git pull`

- Github 원격 저장소에 pull한다.

```shell
$ git pull origin master
```



### (5) 그 외 명령어

- `git`의 달라진 차이를 표시 `git diff`

```shell
$ git diff
```

- 파일 만들기 `touch` 

```shell
touch 파일명
```

- 현재 폴더(.) 에서 비주얼 스튜디오 불러오기 `code .`

```shell
code .
```

