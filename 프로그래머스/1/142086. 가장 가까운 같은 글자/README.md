# [level 1] 가장 가까운 같은 글자 - 142086 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/142086) 

### 성능 요약

메모리: 11.1 MB, 시간: 2774.99 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 04월 24일 00:05:36

### 문제 설명

<p style="user-select: auto !important;">문자열 <code style="user-select: auto !important;">s</code>가&nbsp;주어졌을 때, <code style="user-select: auto !important;">s</code>의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.<br style="user-select: auto !important;">
예를 들어, <code style="user-select: auto !important;">s</code>="banana"라고 할 때,&nbsp; 각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서&nbsp;다음과 같이 진행할 수 있습니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">b는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.</li>
<li style="user-select: auto !important;">a는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.</li>
<li style="user-select: auto !important;">n은 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.</li>
<li style="user-select: auto !important;">a는 자신보다 두 칸 앞에 a가 있습니다. 이는 2로 표현합니다.</li>
<li style="user-select: auto !important;">n도&nbsp;자신보다 두 칸 앞에 n이 있습니다. 이는 2로 표현합니다.</li>
<li style="user-select: auto !important;">a는 자신보다 두 칸, 네 칸 앞에 a가 있습니다. 이 중 가까운 것은 두 칸 앞이고, 이는 2로 표현합니다.</li>
</ul>

<p style="user-select: auto !important;">따라서 최종 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.</p>

<p style="user-select: auto !important;">문자열 <code style="user-select: auto !important;">s</code>이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">s</code>의 길이 ≤ 10,000

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">s</code>은 영어 소문자로만 이루어져 있습니다.</li>
</ul></li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">s</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">"banana"</td>
<td style="user-select: auto !important;">[-1, -1, -1, 2, 2, 2]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">"foobar"</td>
<td style="user-select: auto !important;">[-1, -1, 1, -1, -1, -1]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1<br style="user-select: auto !important;">
지문과 같습니다.</p>

<p style="user-select: auto !important;">입출력 예 #2<br style="user-select: auto !important;">
설명 생략</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges