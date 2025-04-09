SELECT
	*,
	COUNT(*) AS duplicated_values
FROM
	driven_raw.raw_batch_data
GROUP BY (
	person_name, user_name, email, personal_number,
	birth_date, address, phone, mac_address, ip_address,
	iban,accessed_at, session_duration, download_speed,
	upload_speed,consumed_traffic, unique_id
)
HAVING COUNT(*) > 1;


