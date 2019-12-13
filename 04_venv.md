#  가상환경

### (1) 가상환경 만들기

- Gitbash를 실행하고 다음의 코드를 입력한다.

```shell
$ python -m venv venv(가상환경명)
```



### (2)  가상환경 들어가기  / 나가기

- Gitbash를 실행하고 다음의 코드를 입력한다.

```shell
$ source venv/Scripts/activate #들어가기
$ deactivate
```



### (3) 가상환경 들어가기 쉽게 만들기

- 명령어 activate를 새로 생성하는 과정이다.

```shell
$ vi ~/.bashrc #1
# type i #2 해당 환경에 입력을 가능하게 만들어준다.
# type alias activate="source venv/Scripts/activate" #3
# type :wq #4
```



### (4)  Gitignore 만들기

- 먼저 https://www.gitignore.io/ 사이트에서 무시할 프로그래밍 언어, 패키지 등을 검색 후 생성된 글을 복사한다. (앞의 경우는 python, venv, Flask)
- 생성된 .gitignore 파일은 해당 목록의 파일, 폴더들이 git에 staged 되지 않도록 만든다.

```shell
$ vi .gitignore #1
# type shift + insert #2
# type :wq #3
```



### (5) 패키지 확인

- 현재 설치된 패키지 확인하기

```shell
$ pip freeze > [목록을 불러올 파일명]
```

- 해당 파일에 있는 패키지 모두 설치하기

```shell
$ pip install -r [설치한 파일 목록]
```

