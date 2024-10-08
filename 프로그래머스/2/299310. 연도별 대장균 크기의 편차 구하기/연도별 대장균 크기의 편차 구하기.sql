SELECT EE.YEAR
      ,EE.MAX_SIZ - E.SIZE_OF_COLONY AS YEAR_DEV
      ,E.ID
  FROM ECOLI_DATA E
    JOIN (
        SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(E.SIZE_OF_COLONY) AS MAX_SIZ
          FROM ECOLI_DATA E
        GROUP BY YEAR(DIFFERENTIATION_DATE) ) EE
    ON YEAR(E.DIFFERENTIATION_DATE) = EE.YEAR
ORDER BY EE.YEAR, YEAR_DEV