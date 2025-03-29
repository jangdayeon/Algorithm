SELECT ANIMAL_ID, ANIMAL_TYPE, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID IN (
    SELECT ANIMAL_ID
    FROM ANIMAL_INS
    WHERE SEX_UPON_INTAKE IN ('Intact Female', 'Intact Male')
    )
    AND
    SEX_UPON_OUTCOME IN ('Spayed Female', 'Spayed Male', 'Neutered Female', 'Neutered Male')
ORDER BY 1;