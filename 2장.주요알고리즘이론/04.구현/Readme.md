## 04. 구현


</br>
</br>

- 💡 **피지컬로 승부하는 구현파트**

>  머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정 

  흔히 문제 해결 분야에서 구현 유형이란, 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 의미한다. 흔히 개발할 때 프로그래밍 언어의 문법에 능숙하고 코드 작성 속도가 빠른 사람을 보고 '피지컬이 좋다'라고 이야기한다. 

 이 책에서는 완전 탐색, 시뮬레이션 유형을 모두 '구현' 유형으로 묶어서 다루고 있다. 완전 탐색은 모든 경우의 수를 주저없이 다 계산하는 해결방법이다. 시뮬레이션은 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야하는 문제 유형을 의미한다.

</br>

</br>


- 💡 **구현에서의 제약사항**

대체로 코딩 테스트에서는 128 ~ 512MB로 메모리를 제한한다. 알고리즘 문제 중 때로는 수백만 개 이상의 데이터를 처리해야 하는 문제가 출제되곤 한다. 이러한 경우 메모리 제한을 엄두에 두고 코딩을 해야한다. 

</br>

**파이썬에서 리스트 크기**

| 데이터의 개수( 리스트의 길이 ) | 메모리 사용량 |
| ------------------------------ | ------------- |
| 1,000                          | 약 4KB        |
| 1,000,000                      | 약 4MB        |
| 10,000,000                     | 약 40MB       |

</br>

 파이썬은 다른 언어에 비해서 구현상의 복잡함이 적은 편이지만 데이터 처리량이 많을 때를 꼭 메모리 제한을 고려하도록 하여야 한다.

>  데이터 처리량이 많을 때를 꼭 메모리 제한을 고려하도록 하여야 한다.

</br>

 즉, 리스트를 선언하고 , 그중에서 크기가 1,000만 이상인 리스트가 있다면 메모리 용량 제한으로 문제가 풀 수 없는 경우도 있다는 점을 기억하자. 하지만, 매우 드물다. 여러가지 문제점을 야기하며 , 출제자 입장에서도 매우 번거로운 작업이기 때문이다. 대회 문제가 아니라면 복잡한 최적화를 요구하지 않는 것이 일반적이므로 코딩 테스트 에서는 이 정도만 기억해도 문제를 푸는 데에 어려움은 없다. 

</br>

**1초에 2000만 번 연산을 수행하는 파이썬**

2020년을 파이썬 3.7을 기준으로 1초에 대략 2000만번을 수행한다. 하지만 Pypy3를 사용하면 실행시간이 더 짧아지게 되며, 최근에는 pypy3를 지원하는 코딩테스트가 늘어나는 추세이다.

</br>

</br>

- 💡 **코딩테스트에서자주 등장하는 구현예제**

</br>

**상하좌우**

```python
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

//또는

steps = [(0,-1), (0,1), (-1,0), (1,0)]
```



 상하좌우 문제나 동서남북 문제 (또는 방향이 정해진 문제)가 나온다면 위와 같이 리스트를 생성하고 접근하는 것이 매우매우 편하다!
 
</br>
</br>
