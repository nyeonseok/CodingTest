select AI.ANIMAL_ID, AI.ANIMAL_TYPE, AI.NAME from ANIMAL_INS AI
inner join ANIMAL_OUTS AO on AI.ANIMAL_ID = AO.ANIMAL_ID
where AI.SEX_UPON_INTAKE like "Intact%" and AO.SEX_UPON_OUTCOME not like "Intact%" order by 1