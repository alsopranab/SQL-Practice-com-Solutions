# Intermediate SQL Practice

## 17. Unique Birth Years
---
### Problem Statement
Show unique birth years from patients and order them by ascending.

### Best Approach
Extract year from birth_date and use DISTINCT. Then sort ascending.

### Alternative Options
Use GROUP BY YEAR(birth_date).

### Solution
```sql
SELECT DISTINCT YEAR(birth_date) AS birth_year
FROM patients
ORDER BY birth_year;
```
---


## 18. Unique First Names Occurring Only Once
---
### Problem Statement
Show unique first names from the patients table that appear only once.

### Best Approach
Group by first_name and filter using HAVING COUNT = 1.

### Alternative Options
Use a subquery to count occurrences.

### Solution
```sql
SELECT first_name
FROM patients
GROUP BY first_name
HAVING COUNT(*) = 1;
```
---

## 19. First Names Starting and Ending with 'S'
---
### Problem Statement
Show patient_id and first_name where the name starts with 'S', ends with 'S', and has at least 6 characters.

### Best Approach
Use LIKE for pattern + length filter.

### Alternative Options
Regex pattern '^S.*S$' in supported SQL engines.

### Solution
```sql
SELECT patient_id, first_name
FROM patients
WHERE first_name LIKE 'S%S'
AND LENGTH(first_name) >= 6;
```
---

## 20. Patients Diagnosed with Dementia
---
### Problem Statement
Show patient_id, first_name, last_name for patients diagnosed with Dementia.

### Best Approach
Join patients and admissions and filter by diagnosis.

### Alternative Options
None needed.

### Solution
```sql
SELECT patients.patient_id, first_name, last_name
FROM patients
JOIN admissions ON admissions.patient_id = patients.patient_id
WHERE diagnosis = 'Dementia';
```
---

## 21. Order Names by Length then Alphabetically
---
### Problem Statement
Display first_name ordered by name length and then alphabetically.

### Best Approach
Order by LENGTH(first_name), then first_name.

### Alternative Options
Use CHAR_LENGTH instead.

### Solution
```sql
SELECT first_name
FROM patients
ORDER BY LENGTH(first_name), first_name;
```
---

## 22. Total Male and Female Patients
---
### Problem Statement
Show total male and total female patients in the same row.

### Best Approach
Use subqueries for each count.

### Alternative Options
Use conditional aggregation.

### Solution
```sql
SELECT
  (SELECT COUNT(*) FROM patients WHERE gender = 'M') AS male_count,
  (SELECT COUNT(*) FROM patients WHERE gender = 'F') AS female_count;
```
---

## 23. Patients Allergic to Penicillin or Morphine
---
### Problem Statement
Show first_name, last_name, allergies for patients allergic to Penicillin or Morphine.

### Best Approach
Filter using IN() and order results.

### Alternative Options
Use OR conditions.

### Solution
```sql
SELECT first_name, last_name, allergies
FROM patients
WHERE allergies IN ('Penicillin','Morphine')
ORDER BY allergies, first_name, last_name;
```
---

## 24. Patients Admitted Multiple Times for Same Diagnosis
---
### Problem Statement
Show patient_id and diagnosis for those admitted multiple times with the same diagnosis.

### Best Approach
Group by patient_id and diagnosis, then HAVING COUNT > 1.

### Alternative Options
None needed.

### Solution
```sql
SELECT patient_id, diagnosis
FROM admissions
GROUP BY patient_id, diagnosis
HAVING COUNT(*) > 1;
```
---

## 25. City-wise Patient Count
---
### Problem Statement
Show the city and total number of patients in each city.

### Best Approach
Group by city and sort by patient count.

### Alternative Options
None.

### Solution
```sql
SELECT city, COUNT(patient_id) AS pt_cnt
FROM patients
GROUP BY city
ORDER BY pt_cnt DESC, city ASC;
```
---

## 26. Show Patients and Doctors with Roles
---
### Problem Statement
Show first_name, last_name, and role for both patients and doctors.

### Best Approach
Use UNION ALL with a constant role column.

### Alternative Options
None.

### Solution
```sql
SELECT first_name, last_name, 'Patient' AS role FROM patients
UNION ALL
SELECT first_name, last_name, 'Doctor' AS role FROM doctors;
```
---

## 27. Allergies Ordered by Popularity
---
### Problem Statement
Show allergies sorted by how many patients have them. Exclude NULL.

### Best Approach
COUNT + GROUP BY + ORDER.

### Alternative Options
None.

### Solution
```sql
SELECT COUNT(allergies) AS alcnt, allergies
FROM patients
WHERE allergies IS NOT NULL
GROUP BY allergies
ORDER BY alcnt DESC;
```
---

## 28. Patients Born in the 1970s
---
### Problem Statement
Show patients born in the 1970s sorted by earliest birth_date.

### Best Approach
Filter using LIKE '197%'.

### Alternative Options
Use YEAR(birth_date) BETWEEN 1970 AND 1979.

### Solution
```sql
SELECT first_name, last_name, birth_date
FROM patients
WHERE birth_date LIKE '197%'
ORDER BY birth_date ASC;
```
---

## 29. Full Name (LASTNAME,FIRSTNAME)
---
### Problem Statement
Display full name with last_name in UPPERCASE and first_name in lowercase.

### Best Approach
Use CONCAT + UPPER + LOWER.

### Alternative Options
None.

### Solution
```sql
SELECT CONCAT(UPPER(last_name), ',', LOWER(first_name)) AS full_name
FROM patients
ORDER BY first_name DESC;
```
---

## 30. Provinces with Height Sum ≥ 7000
---
### Problem Statement
Show province_id where total height of patients is ≥ 7000.

### Best Approach
Group by province_id and filter with HAVING.

### Alternative Options
None.

### Solution
```sql
SELECT SUM(height) AS heights, province_id
FROM patients
GROUP BY province_id
HAVING SUM(height) >= 7000;
```
---

## 31. Weight Difference for Last Name "Maroni"
---
### Problem Statement
Show the difference between max and min weight for last name Maroni.

### Best Approach
Use MAX − MIN.

### Alternative Options
None.

### Solution
```sql
SELECT MAX(weight) - MIN(weight) AS diff
FROM patients
WHERE last_name = 'Maroni';
```
---

## 32. Admissions Per Day of Month
---
### Problem Statement
Show day (1–31) and how many admissions occurred on that day.

### Best Approach
Extract day + group.

### Alternative Options
None.

### Solution
```sql
SELECT DAY(admission_date) AS day_m,
COUNT(admission_date) AS visits
FROM admissions
GROUP BY day_m
ORDER BY visits DESC;
```
---

## 33. Most Recent Admission for Patient 542
---
### Problem Statement
Show all columns for patient_id 542's most recent admission.

### Best Approach
Order by admission_date DESC and LIMIT 1.

### Alternative Options
Use MAX(admission_date) with a subquery.

### Solution
```sql
SELECT *
FROM admissions
WHERE patient_id = '542'
ORDER BY admission_date DESC
LIMIT 1;
```
---

## 34. Multi-Condition Admissions Filter
---
### Problem Statement
Show admissions where:
1. patient_id is odd AND attending_doctor_id in (1,5,19)  
OR  
2. attending_doctor_id contains a 2 AND patient_id length = 3.

### Best Approach
Combine both conditions with OR.

### Alternative Options
Use REGEXP for digit matching.

### Solution
```sql
SELECT patient_id, attending_doctor_id, diagnosis
FROM admissions
WHERE (patient_id % 2 != 0
AND attending_doctor_id IN (1,5,19))
OR
(LENGTH(patient_id) = 3
AND attending_doctor_id LIKE '%2%');
```
---

## 35. Total Admissions per Doctor
---
### Problem Statement
Show first_name, last_name, and total admissions attended by each doctor.

### Best Approach
Join doctors with admissions and count rows.

### Alternative Options
None.

### Solution
```sql
SELECT doctors.first_name, doctors.last_name,
COUNT(admission_date) AS admissions_total
FROM doctors
JOIN admissions ON admissions.attending_doctor_id = doctors.doctor_id
GROUP BY doctors.first_name, doctors.last_name;
```
---

## 36. First and Last Admission Date per Doctor
---
### Problem Statement
Show doctor_id, full name, first admission, and last admission dates.

### Best Approach
Use MIN and MAX over grouped admissions.

### Alternative Options
None.

### Solution
```sql
SELECT CONCAT(doctors.first_name,' ',doctors.last_name) AS full_name,
doctor_id,
MIN(admission_date) AS first_admission_date,
MAX(admission_date) AS last_admission_date
FROM admissions
JOIN doctors ON admissions.attending_doctor_id = doctors.doctor_id
GROUP BY full_name;
```
---

## 37. Patient Count per Province
---
### Problem Statement
Display total number of patients per province ordered descending.

### Best Approach
Join patients with province_names and group.

### Alternative Options
None.

### Solution
```sql
SELECT COUNT(patient_id) AS patient_count,
province_name
FROM patients
JOIN province_names ON province_names.province_id = patients.province_id
GROUP BY province_name
ORDER BY patient_count DESC;
```
---

## 38. Admission Details with Patient and Doctor Names
---
### Problem Statement
Show patient's full name, diagnosis, and doctor's full name.

### Best Approach
Join patients + admissions + doctors.

### Alternative Options
None.

### Solution
```sql
SELECT CONCAT(patients.first_name,' ',patients.last_name) AS patient_name,
CONCAT(doctors.first_name,' ',doctors.last_name) AS doctor_name,
admissions.diagnosis
FROM patients
JOIN admissions ON patients.patient_id = admissions.patient_id
JOIN doctors ON doctors.doctor_id = admissions.attending_doctor_id;
```
---

## 39. Duplicate Patients Based on Name
---
### Problem Statement
Display number of duplicates based on first_name + last_name.

### Best Approach
Group by both fields and HAVING COUNT > 1.

### Alternative Options
None.

### Solution
```sql
SELECT first_name, last_name,
COUNT(*) AS num_of_dupes
FROM patients
GROUP BY first_name, last_name
HAVING COUNT(*) > 1;
```
---

## 40. Convert Height/Weight and Show Full Details
---
### Problem Statement
Show full_name, height(feet), weight(pounds), birth_date, and gender(non-abbreviated).

### Best Approach
Apply conversion formulas + CASE expression.

### Alternative Options
None.

### Solution
```sql
SELECT CONCAT(first_name,' ',last_name) AS full_name,
ROUND((height / 30.48),1) AS height,
ROUND((weight * 2.205),0) AS weight,
birth_date,
CASE WHEN gender = 'M' THEN 'MALE'
ELSE 'FEMALE' END AS gender
FROM patients;
```
---

## 41. Patients with No Admission Records
---
### Problem Statement
Show patients whose patient_id does not appear in admissions table.

### Best Approach
Use NOT IN with subquery.

### Alternative Options
Use LEFT JOIN + WHERE admissions.patient_id IS NULL.

### Solution
```sql
SELECT patients.patient_id, patients.first_name, patients.last_name
FROM patients
WHERE patients.patient_id NOT IN
(SELECT admissions.patient_id FROM admissions);
```
---

