
update [admissions]
set attending_doctor_id = 29
where attending_doctor_id = 3;

update [admissions]
Set patient_id = 4
where patient_id = 35;

select * from admissions;





SELECT DISTINCT doc.doctor_id,doc.first_name, doc.last_name, doc.specialty
FROM DOCTORS doc, patients pat
JOIN ADMISSIONS adm ON doc.doctor_id = adm.attending_doctor_id;



SELECT doc.doctor_id, doc.first_name, doc.last_name, doc.specialty
FROM DOCTORS doc
left JOIN ADMISSIONS adm ON doc.doctor_id = adm.attending_doctor_id
WHERE adm.attending_doctor_id IS NULL;


select pat.patient_id,pat.first_name,pat.last_name,pat.gender,pat.birth_date,pat.city,pat.province_id,pat.allergies,pat.height,pat.weight from patients pat
left join admissions adm on pat.patient_id=adm.patient_id
where adm.attending_doctor_id is null;
