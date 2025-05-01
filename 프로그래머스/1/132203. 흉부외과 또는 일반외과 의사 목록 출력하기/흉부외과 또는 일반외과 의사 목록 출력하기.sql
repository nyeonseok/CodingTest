select DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD,"%Y-%m-%d") from DOCTOR where MCDP_CD = "CS" or MCDP_CD = "GS"
order by HIRE_YMD desc, DR_NAME asc