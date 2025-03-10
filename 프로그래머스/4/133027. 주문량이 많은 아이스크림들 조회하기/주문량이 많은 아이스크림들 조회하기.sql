# 7월에는 아이스크림 주문량이 많아 같은 아이스크림에 대하여 서로 다른 두 공장에서 아이스크림 가게로 출하를 진행하는 경우가 있습니다. 이 경우 같은 맛의 아이스크림이라도 다른 출하 번호를 갖게 됩니다.

SELECT F.FLAVOR
FROM FIRST_HALF AS F, (
    SELECT SHIPMENT_ID, FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM JULY
    GROUP BY FLAVOR
) AS J
WHERE F.FLAVOR = J.FLAVOR
ORDER BY F.TOTAL_ORDER+J.TOTAL_ORDER DESC
LIMIT 3