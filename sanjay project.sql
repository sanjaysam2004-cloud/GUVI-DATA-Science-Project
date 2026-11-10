use guvi_project;
show tables;
select count(*) from
cleaned_311_data;
select * from cleaned_311_data; 
SELECT * FROM cleaned_311_data LIMIT 10;
DESCRIBE Cleaned_311_data;
SELECT
COUNT(*) AS total_records,
SUM(CASE WHEN latitude IS NULL THEN 1 ELSE 0 END) AS missing_latitude,
SUM(CASE WHEN longitude IS NULL THEN 1 ELSE 0 END) AS missing_longitude,
SUM(CASE WHEN status IS NULL THEN 1 ELSE 0 END) AS missing_status
FROM Cleaned_311_data;
SELECT status, COUNT(*) AS total
FROM Cleaned_311_data
GROUP BY status
ORDER BY total DESC;
SELECT COUNT(*) FROM Cleaned_311_data;
SELECT status, COUNT(*) AS total
FROM Cleaned_311_data
GROUP BY status;
SELECT complaint_type, COUNT(*) AS total
FROM Cleaned_311_data
GROUP BY complaint_type
ORDER BY total DESC
LIMIT 10;
SELECT borough, COUNT(*) AS total
FROM Cleaned_311_data
GROUP BY borough
ORDER BY total DESC;
SELECT
AVG(resolution_hours) AS avg_resolution_hours,
MAX(resolution_hours) AS max_resolution_hours,
MIN(resolution_hours) AS min_resolution_hours
FROM Cleaned_311_data;
SELECT MIN(resolution_hours) AS minimum_hours
FROM Cleaned_311_data;
SELECT COUNT(resolution_hours) AS non_null_values,
       COUNT(*) AS total_records
FROM Cleaned_311_data;
SELECT MIN(resolution_hours) AS minimum_hours
FROM Cleaned_311_data;
SELECT
MIN(CAST(resolution_hours AS DECIMAL(10,5))) AS minimum_hours,
MAX(CAST(resolution_hours AS DECIMAL(10,5))) AS maximum_hours
FROM Cleaned_311_data;
SELECT MAX(CAST(resolution_hours AS DECIMAL(10,5))) AS maximum_hours
FROM Cleaned_311_data;
SELECT borough, COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY borough
ORDER BY total_complaints DESC;
SELECT status, COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY status
ORDER BY total_complaints DESC;
SELECT
    borough,
    ROUND(AVG(resolution_hours), 5) AS avg_resolution_hours
FROM Cleaned_311_data
GROUP BY borough
ORDER BY avg_resolution_hours DESC;
SELECT complaint_type, COUNT(*) AS total
FROM Cleaned_311_data
GROUP BY complaint_type
ORDER BY total DESC
LIMIT 5;
SELECT
    DATE_FORMAT(created_date, '%Y-%m') AS complaint_month,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY complaint_month
ORDER BY complaint_month;
SELECT
    YEAR(created_date) AS complaint_year,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY YEAR(created_date)
ORDER BY complaint_year;
SELECT
    DAYNAME(created_date) AS complaint_day,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY DAYNAME(created_date)
ORDER BY total_complaints DESC;
SELECT DISTINCT DAYNAME(created_date) AS complaint_day
FROM Cleaned_311_data;
SELECT created_date, DAYNAME(created_date)
FROM Cleaned_311_data
LIMIT 10;
SELECT
    MIN(created_date) AS first_date,
    MAX(created_date) AS last_date,
    COUNT(DISTINCT DATE(created_date)) AS total_days
FROM Cleaned_311_data;
SELECT
    HOUR(created_date) AS complaint_hour,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY HOUR(created_date)
ORDER BY complaint_hour;
SELECT
    borough,
    status,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY borough, status
ORDER BY borough, total_complaints DESC;
SELECT
    status,
    COUNT(*) AS total_complaints,
    ROUND(AVG(resolution_hours), 3) AS avg_resolution_hours
FROM Cleaned_311_data
GROUP BY status
ORDER BY avg_resolution_hours DESC;
SELECT
    complaint_type,
    COUNT(*) AS total_complaints,
    ROUND(AVG(resolution_hours), 3) AS avg_resolution_hours
FROM Cleaned_311_data
GROUP BY complaint_type
ORDER BY avg_resolution_hours DESC
LIMIT 10;
SELECT COUNT(*) AS total_records
FROM Cleaned_311_data;
SELECT
    status,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY status
ORDER BY total_complaints DESC;
SELECT
    borough,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY borough
ORDER BY total_complaints DESC;
SELECT
    COUNT(*) AS total_records,
    SUM(CASE WHEN latitude IS NULL THEN 1 ELSE 0 END) AS missing_latitude,
    SUM(CASE WHEN longitude IS NULL THEN 1 ELSE 0 END) AS missing_longitude,
    SUM(CASE WHEN status IS NULL THEN 1 ELSE 0 END) AS missing_status
FROM Cleaned_311_data;
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT unique_key) AS unique_records,
    COUNT(*) - COUNT(DISTINCT unique_key) AS duplicate_records
FROM Cleaned_311_data;
SELECT
    ROUND(AVG(resolution_hours), 3) AS average_hours,
    ROUND(MIN(resolution_hours), 3) AS minimum_hours,
    ROUND(MAX(resolution_hours), 3) AS maximum_hours
FROM Cleaned_311_data;
SELECT
    borough,
    COUNT(*) AS total_complaints,
    ROUND(AVG(resolution_hours), 3) AS avg_resolution_hours
FROM Cleaned_311_data
GROUP BY borough
ORDER BY avg_resolution_hours DESC;
SELECT
    complaint_type,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY complaint_type
ORDER BY total_complaints DESC
LIMIT 10;
SELECT
    DATE_FORMAT(created_date, '%Y-%m') AS complaint_month,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY complaint_month
ORDER BY complaint_month;
SELECT
    DAYNAME(created_date) AS complaint_day,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY complaint_day
ORDER BY total_complaints DESC;
SELECT
    HOUR(created_date) AS complaint_hour,
    COUNT(*) AS total_complaints
FROM Cleaned_311_data
GROUP BY complaint_hour
ORDER BY complaint_hour;
SELECT
    borough,
    SUM(status = 'Closed') AS closed_count,
    SUM(status = 'In Progress') AS in_progress_count,
    SUM(status = 'Open') AS open_count
FROM Cleaned_311_data
GROUP BY borough
ORDER BY borough;
WITH ranked AS (
    SELECT
        agency,
        resolution_hours,
        ROW_NUMBER() OVER (
            PARTITION BY agency
            ORDER BY resolution_hours
        ) AS rn,
        COUNT(*) OVER (
            PARTITION BY agency
        ) AS cnt
    FROM Cleaned_311_data
    WHERE resolution_hours IS NOT NULL
)
SELECT
    agency,
    ROUND(AVG(resolution_hours), 3) AS median_resolution_hours
FROM ranked
WHERE rn IN (
    FLOOR((cnt + 1) / 2),
    FLOOR((cnt + 2) / 2)
)
GROUP BY agency
ORDER BY median_resolution_hours DESC;
WITH ordered AS (
    SELECT
        resolution_hours,
        ROW_NUMBER() OVER (ORDER BY resolution_hours) AS rn,
        COUNT(*) OVER () AS total_count
    FROM Cleaned_311_data
    WHERE resolution_hours IS NOT NULL
),
quartiles AS (
    SELECT
        MAX(CASE WHEN rn = FLOOR((total_count + 1) * 0.25)
            THEN resolution_hours END) AS q1_low,
        MAX(CASE WHEN rn = CEIL((total_count + 1) * 0.25)
            THEN resolution_hours END) AS q1_high,
        MAX(CASE WHEN rn = FLOOR((total_count + 1) * 0.75)
            THEN resolution_hours END) AS q3_low,
        MAX(CASE WHEN rn = CEIL((total_count + 1) * 0.75)
            THEN resolution_hours END) AS q3_high,
        MAX(total_count) AS n
    FROM ordered
)
SELECT
    ROUND(q1_low + ((n + 1) * 0.25 - FLOOR((n + 1) * 0.25))
        * (q1_high - q1_low), 3) AS Q1,
    ROUND(q3_low + ((n + 1) * 0.75 - FLOOR((n + 1) * 0.75))
        * (q3_high - q3_low), 3) AS Q3,
    ROUND(
        (q3_low + ((n + 1) * 0.75 - FLOOR((n + 1) * 0.75))
        * (q3_high - q3_low))
        -
        (q1_low + ((n + 1) * 0.25 - FLOOR((n + 1) * 0.25))
        * (q1_high - q1_low)), 3
    ) AS IQR
FROM quartiles;
SELECT
    COUNT(*) AS total_outliers,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*)
         FROM Cleaned_311_data
         WHERE resolution_hours IS NOT NULL),
        2
    ) AS outlier_percentage
FROM Cleaned_311_data
WHERE resolution_hours > 1.83;


