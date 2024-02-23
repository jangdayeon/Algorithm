-- 코드를 작성해주세요
#새로나온 문제
#일단 SKILL_CODE를 해석해서 테이블에 CODE만 다른 데이터들 넣고,
#마지막에 GROUP BY해주자
#비트 연산 -> &은 둘 다 1이면 1반환, |은 둘 중 하나만 1이면 1반환
SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS AS D, SKILLCODES AS S
WHERE D.SKILL_CODE & S.CODE = S.CODE AND S.CATEGORY = "Front End"
ORDER BY D.ID